import requests
from gpiozero import LED
from signal import pause
import time

def openDoor():
    print("Opening the door")
    doorOpenTime = 5
    led.off
    #TODO: Put door opening buzzer sound
    countXSeconds(doorOpenTime)
    print("Closing the door")
    led.on
    requests.put('http://vmedu116.mtacloud.co.il:8080/openDoorApproval?isDoorOpenApproval=false')
    return

def countXSeconds(timeToCount):
    start = time.time()
    end = time.time()
    while end-start < timeToCount:
        end = time.time()
    return

led = LED(20)
timeToCount = 5
requests.put('http://vmedu116.mtacloud.co.il:8080/openDoorApproval?isDoorOpenApproval=false')
while True:
    countXSeconds(timeToCount)
    sp = requests.get('http://vmedu116.mtacloud.co.il:8080/openDoorApproval')
    if "true" == sp.text:
        openDoor()
    
