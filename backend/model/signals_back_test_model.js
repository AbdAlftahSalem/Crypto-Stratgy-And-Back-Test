const {Sequelize, DataTypes} = require('sequelize');
const sequelize = new Sequelize('mysql::memory:');

module.exports = sequelize.define('signals_back_test_table', {
    id: {
        type: DataTypes.BIGINT.UNSIGNED,
        primaryKey: true,
        autoIncrement: true,
        allowNull: false
    },
    entry_date: {
        type: DataTypes.DATE,
        allowNull: false
    },
    out_date: {
        type: DataTypes.DATE,
        allowNull: false
    },
    tp: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    sl: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    status: {
        type: DataTypes.BOOLEAN,
        allowNull: false
    },
    change: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    vwap_value: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    ema_value: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    ticker_id: {
        type: DataTypes.BIGINT,
        allowNull: false
    }
});