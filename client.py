import esp32
import network
from machine import Pin
from time import sleep
import urequests as requests
import json

led = Pin(2, Pin.OUT)
    

print('...')
led.on()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ess32', 'ess12rd6')
sleep(8)
print(wlan.ifconfig())
led.off()

k = 0

while True:
    sleep(1)
    response = requests.get(
        "http://192.168.1.104:5000/command"
        ).text
    if not response:
        continue
    if response == 'temp':
        temp = str((5/9)*(int(esp32.raw_temperature())-32))
        data={"temperature": temp}
        requests.post(
            'http://192.168.1.104:5000/send',
            data=json.dumps(data)
            )
        print('SEND TEMPERATURE')
    elif response == 'led':
        if k:
            led.off()
            k = 0
        else:
            led.on()
            k = 1
        print('CHANGE LED VALUE')
        
