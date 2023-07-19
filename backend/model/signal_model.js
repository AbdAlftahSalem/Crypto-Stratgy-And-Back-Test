const {Sequelize, DataTypes} = require('sequelize');
const sequelize = new Sequelize('mysql::memory:');

module.exports = sequelize.define('signals', {
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
    entry_date: {
        type: DataTypes.DATE,
        allowNull: false
    },
    out_date: {
        type: DataTypes.DATE,
        allowNull: false
    },
    tp: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    sl: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    status: {
        type: DataTypes.ENUM(''),
        allowNull: false,
        defaultValue: 'progress'
    },
    vwap21: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    vwap48: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    vwap84: {
        type: DataTypes.BIGINT,
        allowNull: false
    }
});