const {User} = require("../models/index")

const users_seeder = [{
    "first_name": "Abd Alftah",
    "last_name": "Salem",
    "email": "a@gmail.com",
    "password": "123456789",
    "passwordConfirm": "123456789",
    "phone_number": "0598045064",
    "api_key": "1111111111111111",
    "secret_key": "1111111111111111"
}, {
    "first_name": "Abd Alftah",
    "last_name": "Salem",
    "email": "a2@gmail.com",
    "password": "123456789",
    "passwordConfirm": "123456789",
    "phone_number": "05980450642",
    "api_key": "1111111111111111",
    "secret_key": "1111111111111111"
}]

module.exports = async () => {

    for (const plan of users_seeder) {
        await User.create(plan)
    }
}