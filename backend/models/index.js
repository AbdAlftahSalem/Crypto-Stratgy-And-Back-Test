const Sequelize = require('sequelize');
const db = require('../config/database');

//  models
const BackTestModel = require('./back_test');
const FeaturesModel = require('./features');
const OnBoardingModel = require('./on_boarding');
const PlanModel = require('./plan');
const SignalModel = require('./signal');
const SignalBackTestModel = require('./signal_back_test');
const UserModel = require('./user');


//  create objects
const BackTest = BackTestModel(db, Sequelize);
const Features = FeaturesModel(db, Sequelize);
const OnBoarding = OnBoardingModel(db, Sequelize);
const Plan = PlanModel(db, Sequelize);
const Signal = SignalModel(db, Sequelize);
const SignalBackTest = SignalBackTestModel(db, Sequelize);
const User = UserModel(db, Sequelize);


// Associations
// create associations between plan and user by plan_id
User.hasOne(Plan, {foreignKey: 'plan_id'});
Plan.belongsTo(User, {foreignKey: 'plan_id'});

User.hasMany(Signal, {foreignKey: 'user_id'});
Signal.belongsTo(User, {foreignKey: 'user_id'});

Plan.hasMany(Features, {foreignKey: 'plan_id'});
Features.belongsTo(Plan, {foreignKey: 'plan_id'});

BackTest.hasMany(SignalBackTest, {foreignKey: 'back_test_id'});
SignalBackTest.belongsTo(BackTest, {foreignKey: 'back_test_id'});


db.sync({force: true}).then(_ => console.log("db synced")).catch(e => console.log(e))

module.exports = {
    BackTest,
    Features,
    OnBoarding,
    Plan,
    Signal,
    SignalBackTest,
    User,
};
