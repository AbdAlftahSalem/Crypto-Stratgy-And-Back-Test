module.exports = (db, type) => db.define('SignalBackTest', {
    entry_date: {
        type: type.DATE,
        allowNull: false,
    },
    out_date: {
        type: type.DATE,
        allowNull: false,
    },
    tp: {
        type: type.BIGINT,
        allowNull: false,
    },
    sl: {
        type: type.BIGINT,
        allowNull: false,
    },
    status: {
        type: type.TINYINT(1),
        allowNull: false,
    },
    change: {
        type: type.BIGINT,
        allowNull: false,
    },
    vwap_value: {
        type: type.BIGINT,
        allowNull: false,
    },
    ema_value: {
        type: type.BIGINT,
        allowNull: false,
    },
}, {
    freezeTableName: true,
    timestamps: true,
    tableName: 'signals_back_test',
});
