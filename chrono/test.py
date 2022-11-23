# Imports go at the top
from microbit import *

# setup the pinmodes
pin0.write_digital(1)
pin1.write_digital(1)

display.show(Image.YES)

while True:
    # when the a button pressed simulate about a 1.5 ms projectile
    if button_a.is_pressed():
        pin0.write_digital(0)
        sleep(1.5)
        pin1.write_digital(0)
        display.clear()