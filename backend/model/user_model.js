const {Sequelize, DataTypes} = require('sequelize');
const sequelize = new Sequelize('mysql::memory:');

module.exports = sequelize.define('users_table', {
    id: {
        type: DataTypes.BIGINT.UNSIGNED,
        primaryKey: true,
        autoIncrement: true,
        allowNull: false,
    },
    first_name: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    last_name: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    email: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    password: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    phone_number: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    telegram_id: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    active_telegram: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        defaultValue: false
    },
    plan_id: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    role: {
        type: DataTypes.ENUM('user', 'admin', 'manger'),
        defaultValue: 'user',
        allowNull: false
    },
    signals: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    language: {
        type: DataTypes.ENUM('en', 'ar'),
        allowNull: false,
        defaultValue: 'en'
    },
    theme: {
        type: DataTypes.ENUM('dark', 'light'),
        allowNull: false,
        defaultValue: 'dark'
    },
    api_key: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    secret_key: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    user_name_telegram: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    balance_trade: {
        type: DataTypes.BIGINT,
        allowNull: false
    }
});