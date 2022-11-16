#MQTT Pub example

import paho.mqtt.client as mqtt

con = mqtt.Client()
con.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
con.loop_start()

print("Running pub")
while True:
	msg = input()
	con.publish("fatec/bdd/g1/",str(msg))