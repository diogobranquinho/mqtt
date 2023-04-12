'''
    MQTT Sub example
'''

import os
import paho.mqtt.client as mqtt


TOPIC = os.environ.get("TOPIC")
MOSQUITTO_HOST = os.environ.get("MOSQUITTO_HOST")
MOSQUITTO_PORT = int(
    os.environ.get("MOSQUITTO_PORT", "1883"))
MOSQUITTO_KEEPALIVE = int(
    os.environ.get("MOSQUITTO_KEEPALIVE", "60"))


def on_connect_fail(con, userdata, err):
    '''
        The callback for when the client receives an error response from the server connection.
    '''
    print("Error connecting with error "+str(err))

def on_connect(con, userdata, flags, rc):
    '''
        The callback for when the client receives a CONNACK response from the server connection.
    '''
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    con.subscribe(TOPIC)


def on_message(con, userdata, msg):
    '''
        The callback for when a PUBLISH message is received from the server.
    '''
    print(msg.topic+" "+str(msg.payload))


print("Running sub")

con = mqtt.Client()
con.on_connect_fail = on_connect_fail
con.on_connect = on_connect
con.on_message = on_message

con.connect(MOSQUITTO_HOST, MOSQUITTO_PORT, MOSQUITTO_KEEPALIVE)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
con.loop_forever()
