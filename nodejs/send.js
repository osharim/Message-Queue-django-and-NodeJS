var amqp       = require('amqp');
var amqp_hacks = require('./amqp-hacks');

var connection = amqp.createConnection({ host: "localhost", port: 5672 });

connection.on('ready', function(){
    connection.publish('task_queue', 'Hello World!');
    console.log(" [x] Sent from nodeJS 'Hello World!'");

    amqp_hacks.safeEndConnection(connection);
});