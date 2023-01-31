from machine import Pin
import time
import network
import urequests

ssid = 'pythom'
password = 'bebesitobebelin'

led = Pin("LED", Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# nets = wlan.scan()
wlan.connect(ssid, password)

#for wlan in nets:
#    print(wlan)

print(wlan.isconnected())

print("=======>")

if wlan.isconnected() is False:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )


# DOING
# test how to consume an api
# Get current time
r = urequests.get('http://worldtimeapi.org/api/ip')
result = str(r.content)
startTime = result[int(result.find("datetime")) + 11:30 + result.find("datetime")]


print('Start Time', startTime)


## rest of the code

while True:
    led.value(not led.value())
    print("hello from time", time.time())
    time.sleep(3)
