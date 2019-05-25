from network import LoRa
import socket
import time

# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

from mqtt import MQTTClient
from network import WLAN
import machine
import time


def sub_cb(topic, msg):
    print(msg)


wlan = WLAN(mode=WLAN.STA)
wlan.connect("A4-WiFi", auth=(WLAN.WPA2, "AFourtech@321$"), timeout=5000)

while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")

client = MQTTClient("device_id", "192.168.3.144", port=1883)

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="youraccount/feeds/lights")

while True:
    print(s.recv(64))
    time.sleep(2)
    # if s.recv(64) == b'Ping':
    # s.send('Pong')
    time.sleep(5)
    print("Sending ON MQTT")
    client.publish(topic="cona", msg=s.recv(64))
    client.check_msg()
    time.sleep(1)
