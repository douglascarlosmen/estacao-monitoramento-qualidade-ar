import random
import json
import requests
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "sensor/data"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
api_url = "http://localhost:5000/dados"

# Função para lidar com a chegada de uma mensagem
def on_message(client, userdata, message):
    print(f"Received `{message.payload.decode()}` from `{message.topic}` topic")
    data = json.loads(message.payload.decode())
    enviar_para_api(data)

def enviar_para_api(data):
    # Envia os dados recebidos para a API
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        print("Dados enviados com sucesso para a API.")
    else:
        print(f"Erro ao enviar dados para a API: {response.status_code}")

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    client.username_pw_set("teste", "teste")
    client.on_connect = on_connect
    client.on_message = on_message  # Define o callback para a chegada de mensagens
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    client.subscribe(topic)
    client.loop_forever()  # Inicia o loop para escutar por mensagens

if __name__ == '__main__':
    print("Starting the Station...")
    mqtt_client = connect_mqtt()
    subscribe(mqtt_client)
