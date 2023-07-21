module.exports = (db, type) => db.define('OnBoarding', {
    title: {
        type: type.STRING,
        allowNull: false,
    },
    description: {
        type: type.STRING,
        allowNull: false,
    },
    image: {
        type: type.STRING,
        allowNull: false,
    },
}, {
    freezeTableName: true,
    timestamps: true,
    tableName: 'on_boarding',
});
