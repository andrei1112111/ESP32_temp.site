import esp32
import network
from machine import Pin
from time import sleep
import urequests as requests

led = Pin(2, Pin.OUT)
    

print('...')
led.on()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ess32', 'ess12rd6')
sleep(10)
print(wlan.ifconfig())
led.off()

k = 0

while True:
    sleep(1)
    response = requests.get(
        "http://esp32tempsite.herokuapp.com/command"
        ).text
    if not response:
        continue
    if response == 'temp':
        temp = (5/9)*(int(esp32.raw_temperature())-32)
        requests.post(
            'http://esp32tempsite.herokuapp.com/send',
            json={'temperature': temp}
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
        