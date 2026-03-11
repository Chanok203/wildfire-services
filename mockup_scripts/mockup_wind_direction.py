import paho.mqtt.client as mqtt
import time
import random
import json

MQTT_BROKER = "192.168.10.100"
MQTT_PORT = 1883
MQTT_TOPIC = "winds_direction"

client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")


client.on_connect = on_connect

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    print(f"Starting Mock Sensor... Sending data to {MQTT_TOPIC}")

    while True:
        # จำลองค่าลม 0.0 - 10.0 m/s (ทศนิยม 2 ตำแหน่ง)
        wind_direction = random.randint(0, 359)

        # ส่งค่าไปยัง MQTT
        client.publish(MQTT_TOPIC, str(wind_direction))

        print(f"Published: {wind_direction} m/s")
        time.sleep(5) 

except KeyboardInterrupt:
    print("\nStopping Mock Sensor...")
    client.loop_stop()
    client.disconnect()
