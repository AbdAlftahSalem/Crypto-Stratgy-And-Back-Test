function sendSuccessResponse(res, data, statusCode = 200, message = "success") {
    return res.status(statusCode).json({success: true, message, data});
}

module.exports = sendSuccessResponse;
