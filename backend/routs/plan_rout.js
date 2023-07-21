const express = require("express")
const validator = require("../validators/plan_validator")

const {
    addPlan, getPlans
} = require("../services/plan_controller")

const {protectRout} = require("../services/auth_controllers")

const router = express.Router();


router.route("/plan").post(validator.addPlan, addPlan)
router.route("/plan").get(getPlans)
module.exports = router;
