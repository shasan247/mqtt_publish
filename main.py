import mqtt
import time

while 1:
    print("This is the "+ __name__+"function\n")
    print("calling mqtt function")
    result = mqtt.publish()
    print("mqtt returned with publish code:", result)
    time.sleep(4)