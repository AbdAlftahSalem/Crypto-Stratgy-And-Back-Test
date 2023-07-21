const AuthRout = require("../routs/auth_rout");
const PlansRout = require("../routs/plan_rout");


const mountRoutes = (app) => {
    app.use('/api/v1/auth', AuthRout)
    app.use('/api/v1/plan', PlansRout)
};

module.exports = mountRoutes;
