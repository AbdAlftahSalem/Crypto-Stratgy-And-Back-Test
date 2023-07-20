const {UserModel} = require("../model")
const bcrypt = require("bcrypt")
const jwt = require("jsonwebtoken")
const ApiSuccess = require("../util/success_handel")

const env = require("dotenv");
const {ApiError} = require("../util/error_handeler");
env.config({path: "./config.env"})

exports.registerUser = async (req, res) => {

    const user = await UserModel.create(req.body)

    const token = generateToken(user["id"])

    ApiSuccess(res, {date: user, token})
}

exports.loginUser = async (req, res, next) => {
    let user = await UserModel.findOne({
            where: {email: req.body["email"]},
        }
    )

    if (!user) {
        return next(new ApiError(404, " Email or password incorrect"))
    }

    if (await bcrypt.compare(req.body.password, user["password"])) {
        const token = generateToken(user["id"])
        ApiSuccess(res, {date: user, token})
    }

    return next(new ApiError(404, " Email or password incorrect"))

}


exports.getMe = async (req, res, next) => {
    let user = await UserModel.findOne({
            where: {
                id: req.body.user["id"]
            },
        }
    );
    if (!user) {
        return next(new ApiError(404, "user not found"))
    }
    ApiSuccess(res, user)

}

exports.protectRout = async (req, res, next, role = []) => {
    try {
        //  get token form headers
        const token = req.headers.authorization?.split(" ")[1];

        if (!token) {
            return next(new ApiError(401, "You are not logged in"))
        }

        //  verify token if valid expired token
        const decodeToken = jwt.verify(token, process.env.TOKEN_SECRET);

        //  check if user in Database
        const currentUser = await UserModel.findOne({where: {id: decodeToken.user_id}});

        //  check found user success
        if (!currentUser) {
            return next(new ApiError(401, "You are not logged in"))
        }

        //  check role for user
        if (role.length !== 0 && !role.includes(currentUser["role"])) {
            return next(new ApiError(403, "You don't have permission to access this route"))
        }

        //  add user in body of request
        req.body.user = currentUser;
        next();
    } catch (error) {
        return next(new ApiError(404, "User not found"))
    }
};

const generateToken = (userId) => {
    return jwt.sign({user_id: userId}, process.env.TOKEN_SECRET, {
        expiresIn: "30d",
    })
}