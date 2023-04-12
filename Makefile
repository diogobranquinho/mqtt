# Porta padrão utilizada pelo mosquitto
DEFAULT_PORT = 1883

# Comando para parar e remover o container
remove_mosquitto:
	docker stop mosquitto
	docker rm mosquitto

# Comando para criar o container
run_mosquitto:
	docker run --name mosquitto -p $(MOSQUITTO_PORT):$(DEFAULT_PORT) -v ${PWD}/mosquitto/config:/mosquitto/config eclipse-mosquitto
