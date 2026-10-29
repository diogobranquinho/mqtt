#Publicador MQTT
import paho.mqtt.client as mqtt

print('Publicador MQTT')
# Endereco do broker MQTT
BROKER = 'test.mosquitto.org'
# Porta do broker
PORT = 1883
# Topico onde as mensagens serao publicadas
TOPICO = 'fatec/bdd/g1/'

con = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
con.connect(BROKER, PORT, 60)
# Trata a comunicacao com o broker em segundo plano
con.loop_start()

print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    con.publish(TOPICO, msg)
    msg = input()
con.loop_stop()
con.disconnect()
