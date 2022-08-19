#!/usr/bin/env python
import os
import pika
import sys
import formatter as ft


def main():
    # Make connection, channel and queue
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='views')

    # Message receive callback
    def callback(ch, method, properties, body):

        # Create the json files with the urls
        ft.writeViews(body)
        ft.writeTotalViews(body)

        print("Received message: %r" % body)

    # Take messages from the callback function
    channel.basic_consume(queue='views', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os.exit(0)



