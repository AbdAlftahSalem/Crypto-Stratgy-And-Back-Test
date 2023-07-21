const {Plan, Features} = require("../models/index")
const bcrypt = require("bcrypt")
const jwt = require("jsonwebtoken")

const successResponse = require("../util/success_handel")
const {ApiError} = require("../util/error_handeler");

const env = require("dotenv");
env.config({path: "./config.env"})

exports.getPlans = async (req, res, next) => {
    let plans = await Plan.findAll({
        include: [
            {
                model: Features,
            }

        ]
    })

    if (plans == null) {
        return next(new ApiError("Plans not found", 404))
    }

    return successResponse(res, plans, 200, "Plans found successfully")

}

exports.addPlan = async (req, res, next) => {

    let plan = await Plan.create(req.body)

    if (plan == null) {
        return next(new ApiError("Plan not created", 404))
    }
    for (const element of req.body.features) {
        await Features.create(
            {
                plan_id: plan["dataValues"]["id"],
                title: element.title,
                description: element.description,
            }
        )
    }
    const planNew = await Plan.findOne({
            where: {
                id: plan["dataValues"]["id"]
            },

            include: [
                {
                    model: Features,
                }
            ]

        }
    )

    return successResponse(res, planNew, 200, "Plan created successfully")

}