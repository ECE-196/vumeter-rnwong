print("hello world")
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
    # do the rest...
]


leds = [DigitalInOut(pin) for pin in led_pins]
topLED = 0
recentMaxLED = 0
recentMaxTimer = 0.00

for led in leds:
    led.direction = Direction.OUTPUT


# main loop
while True:
    recentMaxTimer = recentMaxTimer + 0.01
    if recentMaxTimer > 0.1:
        recentMaxLED = recentMaxLED - 1
        recentMaxTimer = 0

    curLED = 0
    volume = microphone.value
    topLED = ((volume-23000)*(len(leds)))/20000
    if topLED > recentMaxLED:
        recentMaxLED = topLED

    for led in leds:
        if recentMaxLED > curLED:
            leds[curLED].value = True
        else:
            leds[curLED].value = False
        curLED = curLED + 1

    sleep(.01)