const express = require("express")
const validator = require("../validators/signal_validator")

const {
    addSignal, getSignals, updateSignal
} = require("../services/signals_controller")


const router = express.Router();


router.route("/add-signal").post(validator.addSignal, addSignal)
router.route("/edit-status-signal").post(validator.editStatusSignal, updateSignal)
router.route("/get-signals").get(getSignals)
module.exports = router;
