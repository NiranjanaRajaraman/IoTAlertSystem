WS2223
# Internet of Things - LAB exercises 

This document contains tasks, hints and examples for the lab exercicses of the course on Internet of Things (IoT).

## Lab 1 - Getting started with MQTT
[https://www.hivemq.com/blog/mqtt-essentials-part-1-introducing-mqtt/](https://www.hivemq.com/blog/mqtt-essentials-part-1-introducing-mqtt/)

In the first lab exercises we will learn how to use the MQTT-protocol. First we will use Python and the Thonny IDE to program a client that sends data and receives data from an online broker. Therefore we need to install an MQTT package (library) for Python and program the client. As a next step we set up our own MQTT broker and try to send and receive data.

### Install Thonny and the Eclipse Paho

Thonny is an easy to use Python IDE

Download and install Thonny from [https://thonny.org/] (https://thonny.org/)

Thonny provides a simple pip GUI. To install the MQTT package Ecllipse Paho select <code>Tools</code> --><code> Manage Packages</code>. Search for paho, choose the <code>paho-mqtt</code> package and click on <code>Install</code>

### Program the client

for usage of the API refer to (https://pypi.org/project/paho-mqtt/)

and [https://github.com/eclipse/paho.mqtt.python](https://github.com/eclipse/paho.mqtt.python)

Publishing messages to a topic and subscribing to the topic

<code>
import paho.mqtt.client as mqtt

brokerURL = "mqtt.eclipseprojects.io"
brokerPort = 1883 # port number for unencrypted connections

def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
   print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")

mqttclient = mqtt.Client() #create cliet object

mqttclient.on_connect = on_connect
mqttclient.on_disconnect = on_disconnect
mqttclient.on_message = on_message

mqttclient.connect(brokerURL, brokerPort) #call connect function with URL and port number

mqttclient.subscribe("TestingTopic", qos=1)

mqttclient.loop_start()
# now we can publish topics in the console#

mqttclient.publish(topic="TestingTopic", payload="TestingPayload", qos=0, retain=False)

# to stop use mqttclient.loop_stop()

#Try sending messages: mqttclient.publish("TestingTopic", "Hello")
</code>




