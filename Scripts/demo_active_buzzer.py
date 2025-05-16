from time import sleep

from machine import Pin


class Beeper:
    def __init__(self, pin: int):
        self.pin = Pin(pin, mode=Pin.OUT)
        self.duration = 0.1

    def dot(self):
        self.pin.value(1)
        sleep(self.duration)
        self.pin.value(0)
        sleep(self.duration)

    def dash(self):
        self.pin.value(1)
        sleep(self.duration * 2)
        self.pin.value(0)
        sleep(self.duration)


beeper = Beeper(15)
beeper.dot()
# beeper.dot()
# beeper.dot()
# beeper.dash()
# beeper.dash()
# beeper.dash()
# beeper.dot()
# beeper.dot()
# beeper.dot()
