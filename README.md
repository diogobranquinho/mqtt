# Exemplo de MQTT em Python usando Paho-Mqtt

Este é um exemplo de como realizar comunicação via MQTT em Python utilizando a biblioteca `paho-mqtt`.

Como Executar
-------------

Para executar este exemplo, é necessário ter o Python 3 e o pipenv instalados na máquina. 

### Rodando o container do broker (Eclipse Mosquitto)

Para facilitar a execução do Mosquitto, criamos um arquivo Makefile com duas regras: `run_mosquitto` e `remove_mosquitto`. 

Para executar o Mosquitto, basta digitar o comando `pipenv run make run_mosquitto` no terminal. Certifique-se de que o Docker esteja instalado em sua máquina antes de executar o comando. Se você ainda não tiver o Docker instalado, siga as instruções na [documentação oficial do Docker](https://docs.docker.com/get-docker/) para instalá-lo.

O comando `pipenv run make run_mosquitto` irá baixar a imagem do Eclipse Mosquitto e executará o container com o nome mosquitto. O container será iniciado em modo iterativo (-it) e exporá a porta 1883.

Para parar e remover o container, digite o comando `pipenv run make remove_mosquitto` no terminal.

O Mosquitto estará pronto para ser utilizado e poderá ser acessado pelo endereço localhost:1883. Certifique-se de que nenhuma outra aplicação esteja utilizando a porta 1883 antes de executar o container.


### Instalando as Dependências

Para instalar as dependências, abra o terminal na pasta onde o arquivo `Pipfile` se encontra e execute o seguinte comando:

`pipenv install`

### Executando o exemplo Sub

Para se inscrever no tópico, execute o comando abaixo:

`pipenv run python sub.py`

### Executando o exemplo Pub

Para publicar no tópico, execute o comando abaixo:

`pipenv run python pub.py`

Configurações
-------------

O broker utilizado neste exemplo foi o `Eclipse Mosquitto`, com o tópico `fatec/bdd/g1/`. Para utilizar outro broker ou tópico, basta alterar as configurações no `.env`.

Autor
-----

-   Diogo Branquinho Ramos - *Trabalho inicial* - [diogobranquinho](https://github.com/diogobranquinho)