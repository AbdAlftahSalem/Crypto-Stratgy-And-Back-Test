module.exports = (db, type) => db.define('Signal', {
    ticker: {
        type: type.STRING, allowNull: false,
    }, interval: {
        type: type.STRING, allowNull: false,
    }, entry_date: {
        type: type.DATE, allowNull: false,
    }, out_date: {
        type: type.DATE, allowNull: true,
    }, type_signal: {
        type: type.ENUM('long', 'short'), allowNull: false, defaultValue: 'long',
    }, enter_price: {
        type: type.BIGINT, allowNull: false,
    }, tp: {
        type: type.STRING, allowNull: false,
    }, sl: {
        type: type.STRING, allowNull: false,
    }, status: {
        type: type.ENUM('progress', 'success', 'fail'), allowNull: false, defaultValue: 'progress',
    }, vwap21: {
        type: type.BIGINT, allowNull: false,
    }, vwap48: {
        type: type.BIGINT, allowNull: false,
    }, vwap84: {
        type: type.BIGINT, allowNull: false,
    },
}, {
    freezeTableName: true, timestamps: true, tableName: 'signals',
});
