var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){

var amqp = require('amqp');


var connection = amqp.createConnection({ host: "localhost", port: 5672 });

connection.on('ready', function(){
    connection.queue('task_queue', {autoDelete: false,
                                    durable: true}, function(queue){

        queue.subscribe({ack: true, prefetchCount: 1}, function(msg){
            var body = msg.data.toString('utf-8'); 

              console.log(" [x] Received %s", body);

              io.emit('chat message', body);

            setTimeout(function(){
                console.log(" [x] Done");
                queue.shift();
            }, (body.split('.').length - 1) * 1000);
        });
    });


});



});

http.listen(3000, function(){
  console.log('listening on *:3000');
});
