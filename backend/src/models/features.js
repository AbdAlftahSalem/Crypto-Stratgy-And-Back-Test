module.exports = (db, type) => db.define('Features', {
    title: {
        type: type.STRING,
        allowNull: false,
    },
    description: {
        type: type.BIGINT,
        allowNull: false,
    },
}, {
    freezeTableName: true,
    timestamps: true,
    tableName: 'features',
});
