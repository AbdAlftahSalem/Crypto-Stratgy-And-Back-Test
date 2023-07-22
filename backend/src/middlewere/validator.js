const {validationResult} = require("express-validator");
const validatorMiddleWare = (req, res, next) => {
    // Finds the validation errors in this request and wraps them in an object with handy functions
    // middleware to catch error
    const errors = validationResult(req);
    if (!errors.isEmpty()) {

        return res.status(400).json({errors: updatedData(errors.array())});
    } else {
        next()
    }
}

const updatedData = (data) => data.map((dict) => {
    const {value, ...rest} = dict;
    return rest;
});

module.exports = validatorMiddleWare