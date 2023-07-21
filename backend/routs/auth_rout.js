const express = require("express")
const validator = require("../validators/auth_validator")

const {
    loginUser, registerUser, getMe, protectRout, activeTelegram, activePlan
} = require("../services/auth_controllers")


const router = express.Router();


router.route("/register").post(validator.registerUser, registerUser)
router.route("/login").post(validator.loginUser, loginUser)
router.route("/get-me").get(protectRout, getMe)
router.route("/active-telegram").post(validator.activeTelegram, activeTelegram)
router.route("/active-plan").post(protectRout, validator.activePlan, activePlan)
module.exports = router;
