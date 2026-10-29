# Exemplo de MQTT em Python

Exemplo simples de comunicação via MQTT, usando a biblioteca `paho-mqtt`.

No MQTT os programas não conversam diretamente entre si. Todos se conectam a um
servidor intermediário, o **broker**:

- o **publicador** (`pub.py`) envia mensagens para um **tópico** no broker;
- o **assinante** (`sub.py`) se inscreve nesse tópico e recebe tudo o que for publicado nele.

O publicador não sabe quem vai receber, e o assinante não sabe quem enviou. Os dois só
precisam combinar o broker e o tópico.

## Pré-requisitos

- Python 3
- Biblioteca `paho-mqtt`:

```
pip install paho-mqtt
```

## Arquivos

| Arquivo  | O que faz                                        |
|----------|--------------------------------------------------|
| `sub.py` | Assina o tópico e mostra as mensagens recebidas  |
| `pub.py` | Publica no tópico as mensagens digitadas         |

Os dois usam o broker público `test.mosquitto.org` e o tópico `fatec/ipc/g1/`.

## Passo a passo

Terminal do assinante:

```
python3 sub.py
```

```
Assinante MQTT
Conectado ao broker: Success
```

Terminal do publicador:

```
python3 pub.py
```

```
Publicador MQTT
Para sair use CTRL+X

Ola turma
```

No terminal do assinante:

```
fatec/ipc/g1/ Ola turma
```

Para sair do publicador pressione CTRL+X e depois Enter. Para sair do assinante pressione CTRL+C.

## Exercícios sugeridos

1. Abra dois assinantes e um publicador. Quem recebe as mensagens?
2. Abra dois publicadores e um assinante. O que acontece?
3. Altere o `TOPICO` em um dos programas. As mensagens continuam chegando? Por quê?

## Observações importantes

**Broker e tópico.** O endereço do broker (`BROKER`), a porta (`PORT`) e o tópico
(`TOPICO`) ficam no início de cada arquivo. Se a rede bloquear o `test.mosquitto.org`,
troque o `BROKER` nos dois arquivos, por exemplo para `broker.hivemq.com`.

**Broker público.** Qualquer pessoa conectada ao mesmo broker e tópico recebe as
mensagens. Por isso podem aparecer mensagens de colegas.

**Uso didático.** Este exemplo é para estudo: não possui autenticação nem criptografia
e não deve ser usado como base para sistemas em produção.

## Referências

https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html

## Autor

* **Diogo Branquinho Ramos** - [diogobranquinho](https://github.com/diogobranquinho)
