const {check} = require('express-validator');

const validator = require("../middlewere/validator")
const {User, Plan} = require("../models/index")

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
        .withMessage("Too long email").custom((email) => {
        return User.findOne({
            where: {email: email}
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
        .withMessage("password at lease have 6 char"),
    validator,
]

exports.activeTelegram = [

    check("email").notEmpty().isEmail().withMessage("Enter valid email"),

    check("password")
        .notEmpty()
        .isLength({min: 6})
        .withMessage("password at lease have 6 char"),

    check("telegram_id").notEmpty().withMessage("Enter valid telegram id"),
    check("user_name_telegram").notEmpty().withMessage("Enter valid username telegram"),


    validator,
]


exports.activePlan = [

    check("plan_id").notEmpty().withMessage("Enter valid plan id")
        .custom((plan_id) => {
            return Plan.findOne({
                where: {id: plan_id}
            }).then((value) => {
                if (value == null) {
                    return Promise.reject("plan is not defined");
                }
            })
        }).withMessage("plan is not defined"),
    validator,
]
