#encoding:utf-8
#/usr/bin/env/python

import pika
import sys
import time
 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
 
channel.queue_declare(queue='task_queue', durable=True)

LIMIT_MESSAGES = 50
SENT_MESSAGES = 0
while SENT_MESSAGES <= LIMIT_MESSAGES:

    _message = 'Hola desde RabbitMQ en Python #{0}'.format(SENT_MESSAGES)
    
    channel.basic_publish(exchange = '',
              routing_key ='task_queue' ,
              body = _message,
              properties=pika.BasicProperties(
                 delivery_mode = 2, # make SENT_MESSAGES persistent
              ))

    print "Send notify %s from python"  % (SENT_MESSAGES,)
    SENT_MESSAGES += 1
    time.sleep( 1 )


connection.close()
