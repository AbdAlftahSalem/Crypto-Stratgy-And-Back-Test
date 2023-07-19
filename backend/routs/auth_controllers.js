const {UserModel} = require("../model/index")
const bcrypt = require("bcrypt")
const jwt = require("jsonwebtoken")
const ApiSuccess = require("../util/success_handel")

const env = require("dotenv");
env.config({path: "./config.env"})

exports.registerUser = async (req, res) => {

    const user = await UserModel.create(req.body)

    const token = generateToken(user["id"])

    ApiSuccess(res, {date: user, token})
}

exports.loginUser = async (req, res) => {
    let user = await UserModel.findOne({email: req.body.email})

    if (!user) {
        return res.status(404).json({"status": false, "error": [{"msg": " Email or password incorrect"}]})
    }

    if (await bcrypt.compare(req.body.password, user["password"])) {
        const token = generateToken(user["_id"])
        user["posts"] = await getPostsUser(req, res, user["_id"])
        return res.status(200).json({data: user, token})
    }

    return res.status(404).json({"status": false, "error": [{"msg": " Email or password incorrect"}]})

}


exports.getMe = async (req, res) => {
    const user = await User.findById(req.body.user._id).populate("categories")
        .populate("sub_categories").select('-__v -password')
    if (!user) {
        res.status(404).json({"message": "user not found , please login again"})
    } else {
        user["posts"] = await getPostsUser(req, res, user["_id"])

        res.status(200).json(user)

    }

}

exports.protectRout = async (req, res, next, role = []) => {
    try {
        //  get token form headers
        const token = req.headers.authorization?.split(" ")[1];

        if (!token) {
            return res.status(401).json({
                message: "You are not logged in", status: false,
            });
        }

        //  verify token if valid expired token
        const decodeToken = jwt.verify(token, process.env.TOKEN_SECRET);

        //  check if user in Database
        const currentUser = await User.findById(decodeToken.user_id);

        //  check found user success
        if (!currentUser) {
            return res.status(401).json({
                message: "You are not logged in", status: false,
            });
        }

        //  check role for user
        if (role.length !== 0 && !role.includes(currentUser["role"])) {
            return res.status(403).json({
                message: "You don't have permission to access this route", status: false,
            });
        }

        //  add user in body of request
        req.body.user = currentUser;
        next();
    } catch (error) {
        return res.status(404).json({
            status: false, msg: "User not found",
        });
    }
};

const generateToken = (userId) => {
    return jwt.sign({user_id: userId}, process.env.TOKEN_SECRET, {
        expiresIn: "30d",
    })
}