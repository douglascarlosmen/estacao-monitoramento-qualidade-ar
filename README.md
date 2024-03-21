# Estação de Monitoramento para Aplicação de Monitoramento de Qualidade do Ar IoT

Este projeto implementa a Estação de Monitoramento responsável por receber dados de qualidade do ar enviados por sensores IoT. A estação coleta esses dados através de um broker MQTT, podendo realizar um pré-processamento básico antes de encaminhá-los para a Central de Dados para análises mais aprofundadas.

## Funcionalidades

- Conexão com um broker MQTT para receber dados de sensores IoT.
- Inscrição no tópico específico `sensor/data` para coleta de dados.
- Impressão dos dados recebidos no terminal (demonstração de recebimento de dados).
- Estrutura pronta para a integração de processamento ou agregação de dados.

## Pré-requisitos

Para rodar a Estação de Monitoramento, você precisará de:

- Python 3.x instalado em sua máquina.
- Biblioteca `paho-mqtt` instalada.

## Instalação das Dependências

Instale a biblioteca `paho-mqtt` usando pip para permitir a comunicação com o broker MQTT:

```bash
pip install paho-mqtt
```

## Configuração

Configure as seguintes variáveis no início do script para corresponder à configuração do seu broker MQTT:

```bash
broker = 'localhost'
port = 1883
topic = "sensor/data"
```

Se o seu broker MQTT requer autenticação, certifique-se de configurar o nome de usuário e a senha dentro do script:

```python
client.username_pw_set("username", "password")
```

Substitua "username" e "password" pelas credenciais apropriadas para o seu broker MQTT.

## Execução

Para iniciar a Estação de Monitoramento, execute o script Python:

```python
python estacao_monitoramento.py
```

O script se conectará ao broker MQTT, se inscreverá no tópico sensor/data e começará a imprimir os dados recebidos no terminal.