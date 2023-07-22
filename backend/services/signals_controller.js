const {Signal} = require("../models/index")

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

    let signal = await Signal.create(req.body)

    if (signal == null) {
        return next(new ApiError("Signal not created", 404))
    }

    return successResponse(res, signal, 200, "Signal created successfully")

}