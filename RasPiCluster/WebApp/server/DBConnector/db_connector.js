const mariadb = require('mariadb');

const pool = mariadb.createPool({
    host: 'mariadb',
    port: '3306', 
    user:'root', 
    password: 'password',
    connectionLimit: 5,
    database: 'RatDetections'
});

pool.getConnection((err, connection) => {
    if(err){
        if (err.code === 'PROTOCOL_CONNECTION_LOST'){
            console.error('Database connection lost');
        }
        if (err.code === 'ER_CON_COUNT_ERROR'){
            console.error('Database has too many connection');
        }
        if (err.code === 'ECONNREFUSED'){
            console.error('Database connection was refused');
        }
    }
    if(connection) connection.release();

    return;
});

module.exports = pool;