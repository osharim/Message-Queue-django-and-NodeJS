# Node.js && Python code throught RabbitMQ 

 
To successfully use the examples you will need a running RabbitMQ server.

 

## Requirements

To run this example you need `python`> v2. *, `nodeJS` 0.8 (currently it runs on nodeJS 0.11.1-pre). Have installed `RabbitMQ`. Python 0.9.8 using the `pika` and `amqp` client and client nodeJS:


## Installing amqp NodeJS

 	npm install amqp

## pika 0.9.8 Python client 

 	sudo pip install pika==0.9.8

 The installation depends on pip and git-core packages, you may need to install them first.

 	on ubuntu

 	$ sudo apt-get install python-pip git-core

 on debian

	$ sudo apt-get install python-setuptools git-core
	$ sudo easy_install pip

	on windows

	Castigado contra la pared.

	> easy_install pip
	>  pip install pika==0.9.8


## Code

To run the worker rabbitMQ 

	`node receive.js`

	`python receive.py`

To run the producer rabbitMQ 

	`python send.py` || `node send.js` 
 