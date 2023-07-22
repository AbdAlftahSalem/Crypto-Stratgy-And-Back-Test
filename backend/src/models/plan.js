module.exports = (db, type) => db.define('Plan', {
    title: {
        type: type.STRING,
        allowNull: false,
    },
    description: {
        type: type.STRING,
        allowNull: false,
    },
    price: {
        type: type.BIGINT,
        allowNull: false,
    },
    duration: {
        type: type.BIGINT,
        allowNull: false,
    }
}, {
    freezeTableName: true,
    timestamps: true,
    tableName: 'plans',
});
