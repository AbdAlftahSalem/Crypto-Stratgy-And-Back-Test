globalError = (error, req, res, next) => {
    error.statusCode = error.statusCode || 500
    error.message = error.message || "Some thing error , please try again"


    res.status(error.statusCode).send({
        error: {
            error: error.message, "statusCode": error.statusCode, "statusRequest": false, "stack": error.stack,
        }
    });
}

module.exports = globalError;