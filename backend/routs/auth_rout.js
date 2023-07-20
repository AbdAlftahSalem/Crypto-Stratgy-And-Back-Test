const express = require("express")
const validator = require("../validators/auth_validator")

const {
    loginUser, registerUser, getMe, protectRout,
} = require("../services/auth_controllers")


const router = express.Router();


router.route("/register").post(validator.registerUser, registerUser)
router.route("/login").post(validator.loginUser, loginUser)
router.route("/get-me").get(protectRout, getMe)
module.exports = router;
