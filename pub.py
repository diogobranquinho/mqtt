'''
    MQTT Pub example
'''

import os
import paho.mqtt.client as mqtt


TOPIC = os.environ.get("TOPIC")
MOSQUITTO_HOST = os.environ.get("MOSQUITTO_HOST")
MOSQUITTO_PORT = int(
    os.environ.get("MOSQUITTO_PORT", "1883"))
MOSQUITTO_KEEPALIVE = int(
    os.environ.get("MOSQUITTO_KEEPALIVE", "60"))

con = mqtt.Client()
con.connect(MOSQUITTO_HOST, MOSQUITTO_PORT, MOSQUITTO_KEEPALIVE)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
con.loop_start()

print("Running pub")
while True:
    msg = input()
    con.publish(TOPIC, str(msg))
