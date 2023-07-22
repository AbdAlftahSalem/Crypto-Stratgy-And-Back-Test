'use strict';
/** @type {import('sequelize-cli').Migration} */
module.exports = {
    async up(queryInterface, Sequelize) {
        await queryInterface.createTable('Users', {
            id: {
                type: Sequelize.BIGINT.UNSIGNED,
                primaryKey: true,
                autoIncrement: true,
                allowNull: false,
            },
            first_name: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            last_name: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            email: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            password: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            phone_number: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            telegram_id: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            active_telegram: {
                type: Sequelize.BOOLEAN,
                allowNull: false,
                defaultValue: false
            },
            plan_id: {
                type: Sequelize.BIGINT,
                allowNull: false
            },
            role: {
                type: Sequelize.ENUM('user', 'admin', 'manger'),
                defaultValue: 'user',
                allowNull: false
            },
            signals: {
                type: Sequelize.BIGINT,
                allowNull: false
            },
            language: {
                type: Sequelize.ENUM('en', 'ar'),
                allowNull: false,
                defaultValue: 'en'
            },
            theme: {
                type: Sequelize.ENUM('dark', 'light'),
                allowNull: false,
                defaultValue: 'dark'
            },
            api_key: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            secret_key: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            user_name_telegram: {
                type: Sequelize.STRING(255),
                allowNull: false
            },
            balance_trade: {
                type: Sequelize.BIGINT,
                allowNull: false
            }
        });
    },
    async down(queryInterface, Sequelize) {
        await queryInterface.dropTable('Users');
    }
};