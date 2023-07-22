module.exports = (db, type) => db.define('User', {
    first_name: {
        type: type.STRING, allowNull: false,
    }, last_name: {
        type: type.STRING, allowNull: false,
    }, email: {
        type: type.STRING, allowNull: false, unique: true,
    }, password: {
        type: type.STRING, allowNull: false,
    }, phone_number: {
        type: type.STRING, allowNull: false,
    }, telegram_id: {
        type: type.STRING, allowNull: true, defaultValue: null,
    }, active_telegram: {
        type: type.BOOLEAN, allowNull: true, defaultValue: false,
    }, role: {
        type: type.ENUM('user', 'admin', 'super_admin', 'manger'), defaultValue: 'user', allowNull: true,
    }, signals: {
        type: type.BIGINT, allowNull: true,
    }, language: {
        type: type.ENUM('en', 'ar'), allowNull: false, defaultValue: 'en',
    }, theme: {
        type: type.ENUM('dark', 'white'), allowNull: false, defaultValue: 'dark',
    }, api_key: {
        type: type.STRING, allowNull: false,
    }, secret_key: {
        type: type.STRING, allowNull: false,
    }, user_name_telegram: {
        type: type.STRING, allowNull: true, defaultValue: null,
    }, balance_trade: {
        type: type.BIGINT, allowNull: false, defaultValue: 0,
    },

    plan_id: {
        type: type.BIGINT, allowNull: true, defaultValue: null,
    }, last_subscription_date: {
        type: type.DATE, allowNull: true, defaultValue: null,
    }, last_subscription_price: {
        type: type.BIGINT, allowNull: true, defaultValue: null,
    }, end_subscription_date: {
        type: type.DATE, allowNull: true, defaultValue: null,
    }

}, {
    freezeTableName: true, timestamps: true, tableName: 'users',
});
