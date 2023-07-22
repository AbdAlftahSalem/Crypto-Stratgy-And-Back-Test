const {Plan} = require("../models/index")
const {Features} = require("../models");
const plan_seeder = [
    {
        "id": 1,
        "title": "Plan 1",
        "description": "Description 1",
        "features": [
            {
                "title": "Title features 1",
                "description": "Description features 1"
            }
        ],
        "price": "30",
        "duration": 15
    },
    {
        "id": 2,
        "title": "Plan 2",
        "description": "Description 2",
        "features": [
            {
                "title": "Title features 2",
                "description": "Description features 2"
            }
        ],
        "price": "40",
        "duration": 20
    }
]

module.exports = async () => {

    for (const plan of plan_seeder) {

        for (const feature of plan_seeder["features"]) {
            await Features.create({
                plan_id: plan["id"],
                title: feature.title,
                description: feature.description,
            })

            Plan.create(plan)
        }


    }


}