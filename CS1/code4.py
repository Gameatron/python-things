from adafruit_circuitplayground.express import cpx
import time
while True:
    count = 0
    colors = ((10, 10, 0), (10, 0, 0), (0, 10, 0), (10, 0, 10),
              (0, 10, 10), (0, 0, 10), (10, 10, 10))
    touch_things = (cpx.touch_A1, cpx.touch_A2, cpx.touch_A3,
                    cpx.touch_A4, cpx.touch_A5, cpx.touch_A6, cpx.touch_A7)
    for thing in touch_things:
        index = touch_things.index(thing)
        final_color = [0, 0, 0]
        if thing:
            color = colors[index]
            final_color = [final_color[0] += color[0], final_color[1] += color[1], final_color[2] += color[2]]
            cpx.red_led = True
            cpx.pixels.fill(color)
            count += 1
            cpx.red_led = False
    if count == 0:
        cpx.red_led = True
        cpx.pixels.fill(0)
    print(count)