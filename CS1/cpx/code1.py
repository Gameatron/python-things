from adafruit_circuitplayground.express import cpx
import time
count = 0
something = 0
while True:

    if cpx.touch_A1:
        cpx.start_tone(1000)
    else:
        cpx.stop_tone()

    if cpx.button_a:
        if cpx.switch:
            cpx.play_file('Fanfare.wav')
        else:
            cpx.play_file('Coin.wav')

    if cpx.button_b:
        cpx.red_led = True
    else:
        cpx.red_led = False