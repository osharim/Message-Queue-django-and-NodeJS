var amqp       = require('amqp');
var amqp_hacks = require('./amqp-hacks');

var connection = amqp.createConnection({ host: "localhost", port: 5672 });

connection.on('ready', function(){
    connection.publish('hellowww', 'Hello World!');
    console.log(" [x] Sent 'Hello World!'");

    amqp_hacks.safeEndConnection(connection);
});