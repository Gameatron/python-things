from adafruit_circuitplayground.express import cpx
import time
RED = 0x050000
GREEN = 0x000500
BLUE = 0x000005
YELLOW = 0x050500
BLACK = 0x000000
def yellow():
    cpx.pixels[5] = YELLOW
    cpx.pixels[6] = YELLOW
    cpx.play_tone(1, 2)
    cpx.pixels[5] = BLACK
    cpx.pixels[6] = BLACK
while True:
    colors = (GREEN, GREEN, None, RED, RED,
              YELLOW, YELLOW, None, BLUE, BLUE)
    for i in range(10):
        if i == 2 or i == 7:
            pass
        else:
            cpx.pixels[i] = colors[i]
    cpx.pixels.fill(0)
    yellow()
    time.sleep(1)