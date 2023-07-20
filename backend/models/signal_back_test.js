'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class signal_back_test extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  signal_back_test.init({
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
  }, {
    sequelize,
    modelName: 'signal_back_test',
  });
  return signal_back_test;
};