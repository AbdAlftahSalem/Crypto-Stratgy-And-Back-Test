'use strict';
/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('signal_back_tests', {

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
  },
  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('signal_back_tests');
  }
};