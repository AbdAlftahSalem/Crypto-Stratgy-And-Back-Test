'use strict';
/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('signals', {
      id: {
        type: Sequelize.BIGINT.UNSIGNED,
        primaryKey: true,
        autoIncrement: true,
        allowNull: false
      },
      ticker: {
        type: Sequelize.STRING(255),
        allowNull: false
      },
      interval: {
        type: Sequelize.STRING(255),
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
        type: Sequelize.STRING(255),
        allowNull: false
      },
      sl: {
        type: Sequelize.STRING(255),
        allowNull: false
      },
      status: {
        type: Sequelize.ENUM(''),
        allowNull: false,
        defaultValue: 'progress'
      },
      vwap21: {
        type: Sequelize.BIGINT,
        allowNull: false
      },
      vwap48: {
        type: Sequelize.BIGINT,
        allowNull: false
      },
      vwap84: {
        type: Sequelize.BIGINT,
        allowNull: false
      }
    });
  },
  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('signals');
  }
};