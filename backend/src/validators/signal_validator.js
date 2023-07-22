const {check, validationResult} = require('express-validator');

const validator = require("../middlewere/validator")
const {Signal} = require("../models");
const {ApiError} = require("../util/error_handeler");

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

    // check if interval in [ 1m , 5m , 15m , 30m , 1h , 2h , 4h , 1d , 1W , 1M]
    // if true => next()
    // else => throw error
    (req, res, next) => {
        if (['1m', '5m', '15m', '30m', '1h', '2h', '4h', '1d', '1W', '1M'].includes(req.body.interval)) {
            return next()
        }
        return next(new ApiError("Enter valid interval", 400))
    },

    // check if database contain signal with trade_type = progress and ticker = req.body.ticker and interval = req.body.interval
    // if true => throw error
    // else => next()
    async (req, res, next) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({errors: errors.array()});
        }

        const {ticker, interval} = req.body;
        console.log(ticker, interval)
        try {
            // Check if the signal with trade_type = "progress" and matching ticker and interval exists
            const existingSignal = await Signal.findOne({
                where: {
                    status: 'progress',
                    ticker: ticker,
                    interval: interval,
                }
            });
            console.log(existingSignal)
            if (existingSignal) {
                return next(new ApiError('Signal already exists', 400));
            }
            // If the signal doesn't exist, continue with the next middleware
            next();
        } catch (err) {
            console.log(err)
            return next(new ApiError('Something went wrong', 500));
        }
    },


    validator,
]
