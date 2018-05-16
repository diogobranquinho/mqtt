#MQTT Pub example

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(con, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    con.subscribe("fatec/bdd/g1/")

# The callback for when a PUBLISH message is received from the server.
def on_message(con, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

con = mqtt.Client()
con.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
con.loop_start()

while True:
	msg = raw_input()
	print(msg)
	con.publish("fatec/bdd/g1/",str(msg))