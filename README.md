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
QoS 0 fatec/ipc/g1/ Ola turma
```

Para sair do publicador pressione CTRL+X e depois Enter. Para sair do assinante pressione CTRL+C.

## Testando o QoS

O **QoS** (*Quality of Service*) define a garantia de entrega de cada mensagem:

| QoS | Garantia                                  |
|-----|-------------------------------------------|
| 0   | No máximo uma vez: pode se perder         |
| 1   | Pelo menos uma vez: pode chegar repetida  |
| 2   | Exatamente uma vez                        |

Os dois programas têm a variável `QOS` no início do arquivo (padrão `0`). O assinante
mostra o QoS com que cada mensagem chegou:

```
QoS 0 fatec/ipc/g1/ Ola turma
```

Com o assinante ligado, as mensagens chegam com qualquer QoS. A diferença aparece quando o
assinante está **desligado**: o broker só guarda mensagens para ele se o assinante tiver
uma **sessão persistente**. Para isso, altere no `sub.py` a linha que cria a conexão,
trocando `seunome` pelo seu nome:

```python
con = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='fatec-seunome', clean_session=False)
```

O `client_id` identifica o assinante no broker. Ele precisa ser único: dois programas com o
mesmo `client_id` derrubam a conexão um do outro.

Roteiro:

1. No `sub.py`, coloque `QOS = 1`, execute e depois saia com CTRL+C. Neste momento o broker
   registra a sua sessão.
2. Com o assinante desligado, publique três mensagens, uma com cada QoS: no `pub.py`, coloque
   `QOS = 0`, execute, envie `mensagem qos0` e saia. Repita com `QOS = 1` e `QOS = 2`.
3. Execute o `sub.py` novamente. Resultado esperado:

```
Assinante MQTT
Conectado ao broker: Success
QoS 1 fatec/ipc/g1/ mensagem qos1
QoS 1 fatec/ipc/g1/ mensagem qos2
```

A mensagem com QoS 0 se perdeu, e a mensagem publicada com QoS 2 chegou com QoS 1: o QoS
efetivo é sempre o **menor** entre o da publicação e o da assinatura.

Como o tópico é compartilhado, mensagens de colegas também ficam guardadas e podem aparecer.
Para um teste limpo, use um tópico só seu nos dois programas, por exemplo
`fatec/ipc/g1/seunome`.

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
