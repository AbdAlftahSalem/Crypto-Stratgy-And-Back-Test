'use strict';
/** @type {import('sequelize-cli').Migration} */
module.exports = {
    async up(queryInterface, Sequelize) {
        await queryInterface.createTable('back_tests', {
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
            exchange: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            column_5: {
                type: Sequelize.BIGINT,
                allowNull: false
            },
            signals_back_test_id: {
                type: Sequelize.BIGINT,
                allowNull: false
            }
        });
    },
    async down(queryInterface, Sequelize) {
        await queryInterface.dropTable('back_tests');
    }
};