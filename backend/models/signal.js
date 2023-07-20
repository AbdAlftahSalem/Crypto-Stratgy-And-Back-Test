'use strict';
const {
    Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
    class signal extends Model {
        /**
         * Helper method for defining associations.
         * This method is not a part of Sequelize lifecycle.
         * The `models/index` file will call this method automatically.
         */
        static associate(models) {
            // define association here
        }
    }

    signal.init({
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
    }, {
        sequelize,
        modelName: 'signal',
    });
    return signal;
};