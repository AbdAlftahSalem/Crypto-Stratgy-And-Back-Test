'use strict';
/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('signal_back_tests', {

      id: {
        type: Sequelize.BIGINT.UNSIGNED,
        primaryKey: true,
        autoIncrement: true,
        allowNull: false
      },
      entry_date: {
        type: Sequelize.DATE,
        allowNull: false
      },
      out_date: {
        type: Sequelize.DATE,
        allowNull: false
      },
      tp: {
        type: Sequelize.BIGINT,
        allowNull: false
      },
      sl: {
        type: Sequelize.BIGINT,
        allowNull: false
      },
      status: {
        type: Sequelize.BOOLEAN,
        allowNull: false
      },
      change: {
        type: Sequelize.BIGINT,
        allowNull: false
      },
      vwap_value: {
        type: Sequelize.BIGINT,
        allowNull: false
      },
      ema_value: {
        type: Sequelize.BIGINT,
        allowNull: false
      },
      ticker_id: {
        type: Sequelize.BIGINT,
        allowNull: false
      }

    });
  },
  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('signal_back_tests');
  }
};