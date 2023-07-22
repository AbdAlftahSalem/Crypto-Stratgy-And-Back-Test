const express = require("express")
const validator = require("../validators/signal_validator")

const {addSignal, getSignals, updateSignal, deleteSignal} = require("../services/signals_controller")
const {protectRout} = require("../services/auth_controllers")

const router = express.Router();


router.route("/add-signal").post(validator.addSignal, addSignal)
router.route("/edit-status-signal").post(validator.editStatusSignal, updateSignal)
router.route("/delete-signal").post((req, res, next) => protectRout(req, res, next, ["manger"]), validator.deleteSignal, deleteSignal)
router.route("/get-signals").get(getSignals)
module.exports = router;
