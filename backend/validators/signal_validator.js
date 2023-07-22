const {check} = require('express-validator');

const validator = require("../middlewere/validator")

exports.addSignal = [
    check("ticker").notEmpty().withMessage("Enter valid tikcer"),
    check("interval").notEmpty().withMessage("Enter valid interval"),
    check("entry_date").notEmpty().withMessage("Enter valid entry date"),
    check("type_signal").notEmpty().withMessage("Enter valid entry date"),
    check("enter_price").notEmpty().isNumeric().withMessage("Enter valid enter price"),
    check("tp").notEmpty().isNumeric().withMessage("Enter valid tp"),
    check("sl").notEmpty().isNumeric().withMessage("Enter valid sl"),
    check("vwap21").notEmpty().isNumeric().withMessage("Enter valid vwap21"),
    check("vwap48").notEmpty().isNumeric().withMessage("Enter valid vwap48"),
    check("vwap84").notEmpty().isNumeric().withMessage("Enter valid vwap84"),
    validator,
]
