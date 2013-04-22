#RabbitMQ
RabbitMQ speaks a protocol called AMQP. To use Rabbit you'll need a library that
understands the same protocol as Rabbit. There is a choice of libraries for almost
every programming language. For python it's no different and there are a bunch of 
libraries to choose from:


# Node.js && Python code throught RabbitMQ 

 
To successfully use the examples you will need a running RabbitMQ server.

 

## Requirements

To run this example you need `python`> v2. *, `nodeJS` 0.8 (currently it runs on nodeJS 0.11.1-pre). Have installed `RabbitMQ`. Python 0.9.8 using the `pika` and `amqp` client and client nodeJS:


## Installing amqp NodeJS in the work directory.

 	npm install

## pika 0.9.8 Python client 

 	sudo pip install pika==0.9.8

 The installation depends on pip and git-core packages, you may need to install them first.

 Ubuntu

 	$ sudo apt-get install python-pip git-core

 Debian

	$ sudo apt-get install python-setuptools git-core
	$ sudo easy_install pip

 Windows

	Castigado contra la pared.

	> easy_install pip
	>  pip install pika==0.9.8


## Code

To run the worker rabbitMQ 

	`node receive.js`

	`python receive.py`

To run the producer rabbitMQ 

	`python send.py` || `node send.js` 
 
