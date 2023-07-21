const {check} = require('express-validator');

const validator = require("../middlewere/validator")
const {Plan} = require("../models/index")

exports.addPlan = [

    check("title")
        .notEmpty()
        .isLength({min: 3})
        .withMessage("password at lease have 3 char"),

    check("description")
        .notEmpty()
        .isLength({min: 6})
        .withMessage("password at most have 6 char"),

    check("features").notEmpty().withMessage("features is required"),

    validator,
]
