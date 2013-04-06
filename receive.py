#encoding:utf-8
# usr/bin/env/python 
#http://www.rabbitmq.com/tutorials/tutorial-one-python.html

#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hellowww', durable=True)

 
#our callback
def suscriber(ch,method , properties , body):
	print "[Y] received %r " % (body,)
	time.sleep( body.count('.') )
	print " [x] Done"
	ch.basic_ack(delivery_tag = method.delivery_tag)

 

channel.basic_qos(prefetch_count=1)
channel.basic_consume(suscriber,
					  queue = 'hellowww' )

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()