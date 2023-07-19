const {Sequelize} = require('sequelize');
const sequelize = new Sequelize('mysql::memory:');

const BackTestModel = require('./back_test_model');
const FeaturesModel = require('./features_model');
const OnBoardingModel = require('./on_boarding_model');
const PlanModel = require('./plan_model');
const SignalModel = require('./signal_model');
const SignalsBackTestModel = require('./signals_back_test_model');
const UserModel = require('./user_model');

UserModel.hasMany(SignalModel, {foreignKey: 'signals'});
SignalModel.belongsTo(UserModel, {foreignKey: 'signals'});

UserModel.belongsTo(PlanModel, {foreignKey: 'plan_id'});
PlanModel.hasMany(UserModel, {foreignKey: 'plan_id'});

PlanModel.belongsTo(FeaturesModel, {foreignKey: 'features_id'});
FeaturesModel.hasMany(PlanModel, {foreignKey: 'features_id'});

SignalsBackTestModel.belongsTo(BackTestModel, {foreignKey: 'ticker_id'});
BackTestModel.hasMany(SignalsBackTestModel, {foreignKey: 'ticker_id'});

sequelize.sync({force: false}).then(() => {
    console.log('Tables are created successfully ...........');
}).catch((error) => {
    console.log('Error creating tables:', error);
});

module.exports = {
    UserModel,
    PlanModel,
    FeaturesModel,
    SignalModel,
    BackTestModel,
    SignalsBackTestModel,
    OnBoardingModel,
}