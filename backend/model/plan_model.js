const {Sequelize, DataTypes} = require('sequelize');
const sequelize = new Sequelize('mysql::memory:');

module.exports = sequelize.define('plan_table', {
    id: {
        type: DataTypes.BIGINT.UNSIGNED,
        primaryKey: true,
        autoIncrement: true,
        allowNull: false
    },
    title: {
        type: DataTypes.STRING(255),
        allowNull: false
    },
    description: {
        type: DataTypes.BIGINT,
        allowNull: false
    },
    features_id: {
        type: DataTypes.BIGINT,
        allowNull: false
    }
});