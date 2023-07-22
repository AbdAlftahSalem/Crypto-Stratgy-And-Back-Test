module.exports = (db, type) => db.define('BackTest', {
    ticker: {
        type: type.STRING,
        allowNull: false,
    },
    interval: {
        type: type.STRING,
        allowNull: false,
    },
    exchange: {
        type: type.STRING,
        allowNull: false,
    },
    column_5: {
        type: type.BIGINT,
        allowNull: false,
    },
}, {
    freezeTableName: true,
    timestamps: true,
    tableName: 'back_test',
});
