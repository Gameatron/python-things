from adafruit_circuitplayground.express import cpx
import time
x = 0
y = 1
z = 2
pink = (20, 0, 20)
cyan = (0, 20, 20)
red = (20, 0, 0)
blue = (0, 0, 20)
speed = .5
while True:
    if cpx.switch:
        color1 = red
        color2 = cyan
    else:
        color1 = blue
        color2 = pink

    if cpx.button_a:
        speed = .1
    else:
        speed = .5

    if x%10 == 0:
        x = 0
    if y%10 == 0:
        y = 0
    if z%10 == 0:
        z = 0
    cpx.pixels.fill(color2)
    cpx.pixels[x] = color1
    cpx.pixels[y] = color1
    cpx.pixels[z] = color1
    time.sleep(speed)
    x += 1
    y += 1
    z += 1
