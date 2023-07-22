const express = require("express")
const validator = require("../validators/signal_validator")

const {
    addSignal, getSignals
} = require("../services/signals_controller")


const router = express.Router();


router.route("/add-signal").post(validator.addSignal, addSignal)
router.route("/get-signals").get(getSignals)
module.exports = router;
