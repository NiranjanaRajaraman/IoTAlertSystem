
import os, machine
import gc
gc.collect()
import network
import time
from machine import Pin,WDT
import dht
import ujson
import config
from umqtt.simple import MQTTClient

# MQTT Server Parameters
MQTT_CLIENT_ID = config.MQTT_client_id
MQTT_BROKER    = config.MQTT_broker
# MQTT_BROKER    = "broker.f4.htw-berlin.de"
MQTT_USER      = config.MQTT_userName
MQTT_PASSWORD  = config.MQTT_password
MQTT_TOPIC         = config.MQTT_topic_base
MQTT_TOPIC_TEMP    = config.MQTT_topic_temp
MQTT_TOPIC_HUMI    = config.MQTT_topic_humi
MQTT_TOPIC_STATUS = config.MQTT_topic_status

sensor = dht.DHT22(Pin(2))


print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(config.Wifi_NAME, config.Wifi_PASSWORD)
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

print("Connecting to MQTT server... ", end="")
client = MQTTClient(
    MQTT_CLIENT_ID,
    MQTT_BROKER,
    user = MQTT_USER,
    password = MQTT_PASSWORD,
    keepalive=60)  # must ping broker at least every 60 sec

status_offline_msg = ujson.dumps({
    "client_id": MQTT_CLIENT_ID,
    "status": "offline"
})
status_online_msg = ujson.dumps({
    "client_id": MQTT_CLIENT_ID,
    "status": "online"
})
# Set Last Will: broker publishes "offline" if client disconnects unexpectedly
client.set_last_will(topic=MQTT_TOPIC_STATUS, msg= status_offline_msg, retain=True)

client.connect()

print("Connected!")

# Announce online status
client.publish(MQTT_TOPIC_STATUS, msg= status_online_msg , retain=True)
while True:
    try: 
        
        sensor.measure() 
        mytemp= sensor.temperature()
        myhumi = sensor.humidity()
        print("Updated! my temp: ", mytemp, " my humi", myhumi)
        client.publish(MQTT_TOPIC_TEMP, str(mytemp))
        client.publish(MQTT_TOPIC_HUMI, str(myhumi))
        time.sleep(10)

    except Exception as e:
        print("Error:", e)

