const AuthRout = require("./auth_rout");
const PlansRout = require("./plan_rout");
const SignalRout = require("./signal_rout");


const mountRoutes = (app) => {
    app.use('/api/v1/auth', AuthRout)
    app.use('/api/v1/plan', PlansRout)
    app.use('/api/v1/signal', SignalRout)
};

module.exports = mountRoutes;
