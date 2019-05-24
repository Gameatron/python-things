from adafruit_circuitplayground.express import cpx
import time
while True:
    cpx.red_led = True
    time.sleep(.1)
    cpx.red_led = False
    time.sleep(.1)