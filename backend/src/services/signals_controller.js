const {Signal} = require("../models")

const successResponse = require("../util/success_handel")
const {ApiError} = require("../util/error_handeler");

const env = require("dotenv");
env.config({path: "./config.env"})

exports.getSignals = async (req, res, next) => {

    let signals = await Signal.findAll()

    if (signals == null) {
        return next(new ApiError("Signals not found", 404))
    }

    return successResponse(res, signals, 200, "Signals found successfully")


}

exports.addSignal = async (req, res, next) => {

    // check if type signal is empty or not equal to long or short
    if (req.body["type_signal"] === "" || (req.body["type_signal"] !== "long" && req.body["type_signal"] !== "short")) {
        return next(new ApiError("Type signal is not correct", 400))
    }
    // check if signal is long
    if (req.body["type_signal"] === "long") {
        //  check if stop loss is less than entry price and tp is greater than entry price
        if (req.body["stop_loss"] < req.body["entry_price"] || req.body["take_profit"] < req.body["entry_price"]) {
            return next(new ApiError("Stop loss or take profit is not correct", 400))
        }
    }

    // check if signal is short
    if (req.body["type_signal"] === "short") {

        //  check if stop loss is greater than entry price and tp is less than entry price
        if (req.body["stop_loss"] > req.body["entry_price"] || req.body["take_profit"] > req.body["entry_price"]) {
            return next(new ApiError("Stop loss or take profit is not correct", 400))
        }
    }


    let signal = await Signal.create(req.body)

    if (signal == null) {
        return next(new ApiError("Signal not created", 404))
    }

    return successResponse(res, signal, 200, "Signal created successfully")

}

exports.updateSignal = async (req, res, next) => {
//     update status in signal to req.body.status
    const filter = {id: req.body["signal_id"]}
    await Signal.update({
        status: req.body.status,
    }, {
        where: filter,
    })
    return successResponse(res, {}, 200, "Signal updated successfully")
}