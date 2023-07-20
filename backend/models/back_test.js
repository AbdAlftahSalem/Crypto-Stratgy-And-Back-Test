'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class back_test extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  back_test.init({
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
  }, {
    sequelize,
    modelName: 'back_test',
  });
  return back_test;
};