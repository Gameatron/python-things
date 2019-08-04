from adafruit_circuitplayground.express import cpx
import time
WHITE = 0xFFFFFF
WHITE0 = 0x050505
WHITE1 = 0x101010
WHITE2 = 0x151515
WHITE3 = 0x1A1A1A
WHITE4 = 0x2B2B2B
WHITE5 = 0x3C3C3C
WHITE6 = 0x4D4D4D
WHITE7 = 0x5F5F5F
WHITE8 = 0x9F9F9F
WHITE9 = 0xFFFFFF
RED = 0x200000
BLACK = 0x000000
class Application:
    def __init__(self, cpx):
        self.cpx = cpx
        self.brights = (WHITE0, WHITE1, WHITE2, WHITE3,
                        WHITE4, WHITE5, WHITE6, WHITE7,
                        WHITE8, WHITE9)
        self.brightness = 1
        self.color = self.brights[self.brightness]

    def switch_(self):
        if self.cpx.switch:
            self.cpx.pixels.fill(self.brights[self.brightness-1])
        else:
            self.cpx.pixels.fill(BLACK)

    def light_sensor(self):
        if self.cpx.light < 10:
            self.cpx.pixels.fill(self.brights[self.brightness-1])
        else:
            self.cpx.pixels.fill(BLACK)

    def setup(self):
        self.cpx.pixels.fill(BLACK)
        run = True
        print("Setup active!")
        time.sleep(.5)
        while run:
            if self.cpx.button_b:
                if self.brightness%10 == 0:
                    self.cpx.pixels.fill(BLACK)
                    self.brightness = 0
                self.brightness += 1
                print(self.brightness)
                for i in range(self.brightness):
                    self.cpx.pixels[i] = RED
                time.sleep(1)
            if self.cpx.button_a:
                self.cpx.pixels.fill(BLACK)
                time.sleep(.5)
                print("Setup over.")
                break
        print(self.brightness)

    def run(self):
        if self.cpx.light < 10:
            pass
        else:
            self.switch_()

        if self.cpx.switch:
            pass
        else:
            self.light_sensor()

        if self.cpx.button_a:
            self.setup()

if __name__ == "__main__":
    app = Application(cpx)
    while True:
        app.run()