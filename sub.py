#Assinante MQTT
import paho.mqtt.client as mqtt

print('Assinante MQTT')
# Endereco do broker MQTT
BROKER = 'test.mosquitto.org'
# Porta do broker
PORT = 1883
# Topico que sera assinado
TOPICO = 'fatec/bdd/g1/'

# Executado quando a conexao com o broker e estabelecida
def on_connect(con, userdata, flags, reason_code, properties):
    print('Conectado ao broker:', reason_code)
    # Assinar aqui garante que a assinatura volta se a conexao cair
    con.subscribe(TOPICO)

# Executado a cada mensagem recebida no topico
def on_message(con, userdata, msg):
    print(msg.topic, msg.payload.decode())

con = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
con.on_connect = on_connect
con.on_message = on_message
con.connect(BROKER, PORT, 60)
# Fica esperando mensagens (para sair use CTRL+C)
con.loop_forever()
