import paho.mqtt.client as mqtt
from threading import Timer
import time
import json



def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print("topic: "+message.topic+"	"+"payload: "+str(message.payload))
    print('\n')

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    return result
    


# tempSensorData={
#   "msg": "advData",
#   "gmac": "D03304000182",
#   "obj": [
#     {
#       "dmac": "9833000A33DD",
#       "rssi": "-78",
#       "data1": "0201060303AAFE1116AAFE200009D70C00002A5696002A82DA"
#     },
#     {
#       "dmac": "3904000A33DD",
#       "rssi": "-70",
#       "data1": "0201060303AAFE1116AAFE20000B17150000592D5D00599354"
#     }
#   ],
#   "seq": 2896
# }
tempSensorData = "hello"
data = json.dumps(tempSensorData)


# client.subscribe("sensor/data")
# print ("subscribed")


def publish():

    client =mqtt.Client("Zakir1")
    broker= "broker.hivemq.com"
    port=1883

    client.on_connect = on_connect  #attach the callback function to the client object 
    client.on_message = on_message	#attach the callback function to the client object 
    client.on_publish = on_publish

    client.connect(broker, port, 60)
    print ("connecting to broker")
    # client.loop_start() #start the loop
    
    result = client.publish("sensor/data", data )  # publish

    # Timer(2.0, publish).start() # publish every 2 seconds
    time.sleep(4) # wait
    # client.loop_stop() #stop the loop
    client.disconnect() # disconnect

    if result[0] == 0:
        pub_state = "Data Published"
        return pub_state
    else:
        pub_state = "Data isn't Published"
        return pub_state


# client.loop_forever() # to maintain continuous network traffic flow with the broker


