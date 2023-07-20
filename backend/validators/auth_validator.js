const {check} = require('express-validator');

const validator = require("../middlewere/validator")
const {UserModel} = require("../model/index")

exports.registerUser = [

    check("user_name")
        .isLength({min: 3})
        .withMessage("Too Short username")
        .isLength({max: 20}).withMessage("Too long username"),

    check("email").notEmpty().isEmail().withMessage("Enter valid email")
        .isLength({min: 3})
        .withMessage("Too Short email")
        .isLength({max: 18})
        .withMessage("Too long email"),

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

    check("email").notEmpty().isEmail().withMessage("Enter valid email")
        .isLength({min: 3})
        .withMessage("Too Short email")
        .isLength({max: 18})
        .withMessage("Too long email").custom((v) => {
        return UserModel.findOne({
            where: {email: v}
        }).then((r) => {
            if (r) {
                return Promise.reject("email is already in database");
            }
        })
    }).withMessage("The email is already exists"), validator,]

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
