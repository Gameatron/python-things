from adafruit_circuitplayground.express import cpx
import time
from simpleio import map_range

def light_sensor():
    while True:
        light = map_range(cpx.light, 0, 90, 0, 10)
        for i in range(int(light)):
            cpx.pixels[i] = 0x000050
        cpx.pixels.fill(0)

def temp_sensor():
    while True:
        f_temp = cpx.temperature*1.8 + 32
        heat = map_range(f_temp, 70, 90, 1, 10)
        for i in range(int(heat)):
            cpx.pixels[i] = 0x500000
        cpx.pixels.fill(0)

def acc_sensor():
    while True:
        x, y, z = cpx.acceleration
        print(cpx.acceleration)
        if x > 7:
            for i in range(1, 4):
                cpx.pixels[i] = (0, 0, 5)
        else:
            for i in range(1, 4):
                cpx.pixels[i] = (0, 0, 0)
        if y > 5:
            for i in range(4, 6):
                cpx.pixels[i] = (0, 0, 5)
        else:
            for i in range(4, 6):
                cpx.pixels[i] = (0, 0, 0)
        if x < -6:
            for i in range(6, 9):
                cpx.pixels[i] = (0, 0, 5)
        else:
            for i in range(6, 9):
                cpx.pixels[i] = (0, 0, 0)
        if y < -4:
            cpx.pixels[9] = (0, 0, 5)
            cpx.pixels[0] = (0, 0, 5)
        else:
            cpx.pixels[9] = (0, 0, 0)
            cpx.pixels[0] = (0, 0, 0)



def main():
    #light_sensor()
    #temp_sensor()
    acc_sensor()
    pass

if __name__ == "__main__":
    main()