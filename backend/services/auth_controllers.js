const {User, Plan} = require("../models/index")
const bcrypt = require("bcrypt")
const jwt = require("jsonwebtoken")

const successResponse = require("../util/success_handel")
const {ApiError} = require("../util/error_handeler");

const env = require("dotenv");
env.config({path: "./config.env"})

exports.registerUser = async (req, res) => {

    req.body["password"] = await bcrypt.hash(req.body["password"], 10)
    const user = await User.create(req.body, {
        include: [
            {
                model: Plan,
            }
        ]
    })

    const token = generateToken(user["id"])

    return successResponse(res, {user, token}, 201, "User created successfully")
}

exports.loginUser = async (req, res, next) => {
    let user = await User.findOne({
        where: {email: req.body["email"]},
        include: [
            {
                model: Plan,
            }
        ]
    })

    if (user == null) {
        return next(new ApiError("Email or password incorrect", 404))
    }

    if (await bcrypt.compare(req.body.password, user["password"])) {
        const token = generateToken(user["id"])
        return successResponse(res, {user, token}, 200, "User logged in successfully")
    }

    return next(new ApiError("Email or password incorrect", 404))
}

exports.activeTelegram = async (req, res, next) => {
    const filter = {email: req.body["email"]}
    let user = await User.findOne({
        where: filter
    })

    // check if user is null
    if (user == null) {
        return next(new ApiError("Can`t active telegram , email or password is not correct", 404))
    }

    // check if telegram is already active
    if (user["dataValues"]["active_telegram"]) {
        return next(new ApiError("Telegram is already active", 400))
    }

    // check if password is correct
    if (await bcrypt.compare(req.body.password, user["password"])) {
        await User.update({
            telegram_id: req.body.telegram_id,
            active_telegram: true,
            user_name_telegram: req.body.user_name_telegram,
        }, {
            where: filter
        })


        return successResponse(res, {"user": "updated telegram successfully"}, 200, "User logged in successfully")
    }

    return next(new ApiError("Email or password incorrect", 404))

}

exports.activePlan = async (req, res, next) => {
    const filter = {id: req.body.user["id"]}
    let user = await User.findOne({
        where: filter,
    })


    if (user == null) {
        return next(new ApiError("Email or password incorrect", 404))
    }

    const plan = await Plan.findOne({
        where: {id: req.body.plan_id}
    })

    if (plan == null) {
        return next(new ApiError("Plan not found", 404))
    }

    // add to end_subscription_date in user, the number of days in plan
    let end_subscription_date = new Date()
    end_subscription_date.setDate(end_subscription_date.getDate() + plan["dataValues"]["duration"])

    // update user
    await User.update({
        plan_id: req.body.plan_id,
        last_subscription_date: new Date(),
        end_subscription_date: end_subscription_date,
        last_subscription_price: plan["price"],
    }, {
        where: filter,
    })

    return successResponse(res, {data: "updated successfully"}, 200, "User logged in successfully")
}

exports.getMe = async (req, res, next) => {
    let user = await User.findOne({
        where: {
            id: req.body.user["id"]
        }, attributes: {
            exclude: ['password']
        }, include: [{
            model: Plan,
        },]
    });
    if (!user) {
        return next(new ApiError("User not found", 404))
    }

    return successResponse(res, user, 200, "User found successfully")

}

exports.protectRout = async (req, res, next, role = []) => {
    try {
        //  get token form headers
        const token = req.headers.authorization?.split(" ")[1];

        if (!token) {
            return next(new ApiError("You are not logged in", 401))
        }

        //  verify token if valid expired token
        const decodeToken = jwt.verify(token, process.env.TOKEN_SECRET);

        //  check if user in Database
        const currentUser = await User.findOne({where: {id: decodeToken.user_id}});

        //  check found user success
        if (!currentUser) {
            return next(new ApiError("You are not logged in", 401))
        }

        //  check role for user
        if (role.length !== 0 && !role.includes(currentUser["role"])) {
            return next(new ApiError("You don't have permission to access this route", 403))
        }

        //  add user in body of request
        req.body.user = currentUser;
        next();
    } catch (error) {
        return next(new ApiError("You are not logged in", 401))
    }
};

const generateToken = (userId) => {
    return jwt.sign({user_id: userId}, process.env.TOKEN_SECRET, {
        expiresIn: "30d",
    })
}