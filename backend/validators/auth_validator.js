const {check} = require('express-validator');

const validator = require("../middlewere/validator")
const {User} = require("../models/index")

exports.registerUser = [

    check("first_name")
        .isLength({min: 3})
        .withMessage("Too Short first_name")
        .isLength({max: 20}).withMessage("Too long first_name"),

    check("last_name")
        .isLength({min: 3})
        .withMessage("Too Short last_name")
        .isLength({max: 20}).withMessage("Too long last_name"),

    check("email").notEmpty().isEmail().withMessage("Enter valid email")
        .isLength({min: 3})
        .withMessage("Too Short email")
        .isLength({max: 18})
        .withMessage("Too long email").custom((v) => {
        return User.findOne({
            where: {email: v}
        }).then((r) => {
            if (r) {
                return Promise.reject("email is already in database");
            }
        })
    }).withMessage("The email is already exists"),

    check("password")
        .notEmpty()
        .isLength({min: 6})
        .withMessage("password at lease have 6 char")
        .custom((password, {req}) => {
            if (password !== req.body["passwordConfirm"]) {
                throw  new Error("password confirm not correct")
            }
            return true;
        }),

    check("passwordConfirm")
        .notEmpty().withMessage("password confirm required")
        .isLength({min: 6})
        .withMessage("password at lease have 6 char"),

    check("phone_number")
        .isLength({min: 7})
        .withMessage("Too Short phone_number")
        .isLength({max: 12}).withMessage("Too long phone_number"),

    check("api_key").notEmpty().withMessage("api_key is empty"),
    check("secret_key").notEmpty().withMessage("secret_key is empty"),


    validator,
]

exports.loginUser = [

    check("email").notEmpty().isEmail().withMessage("Enter valid email"),

    check("password")
        .notEmpty()
        .isLength({min: 6})
        .withMessage("password at lease have 6 char"), validator,]

exports.resetPassword = [check("currentPassword").notEmpty().withMessage("Enter password"), check("newPassword")
    .notEmpty()
    .isLength({min: 6})
    .withMessage("password at lease have 6 char"),

    validator,]

exports.activeTelegram = [

    check("email").notEmpty().isEmail().withMessage("Enter valid email"),

    check("password")
        .notEmpty()
        .isLength({min: 6})
        .withMessage("password at lease have 6 char"),
    validator,]

exports.resetPassword = [check("currentPassword").notEmpty().withMessage("Enter password"), check("newPassword")
    .notEmpty()
    .isLength({min: 6})
    .withMessage("password at lease have 6 char"),

    validator,]
