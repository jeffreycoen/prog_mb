from microbit import *
from random import *

track = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

car_position = 2
delay = 500
score = 0
    
while True:
    x, y, z = accelerometer.get_values()
    print('x={}, y={}, z={}'.format(x, y, z))
    
    #  Plot the accelerometer reading for x-axis
    print((x, ))
    sleep(10)
    track.set_pixel(randint(0, 4), 0, 5)
    if x >=25 and car_position < 4:
        car_position += 1
    if x <=(-25) and car_position > 0:
        car_position -= 1    
    if track.get_pixel(car_position, 4) > 0:
        display.scroll("GAME OVER!" + str(score))
        break
    track.set_pixel(car_position, 4, 9)
    display.show(track)
    track = track.shift_down(1)
    sleep(delay)
    delay -= 1
    score += 1