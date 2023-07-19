const {Sequelize, DataTypes} = require('sequelize');
const sequelize = new Sequelize('mysql::memory:');

module.exports = sequelize.define('back_test_table', {
    id: {
        type: DataTypes.BIGINT.UNSIGNED,
        primaryKey: true,
        autoIncrement: true,
        allowNull: false
    },
    ticker: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    interval: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    exchange: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    column_5: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    signals_back_test_id: {
        type: DataTypes.BIGINT,
        allowNull: false
    }
});