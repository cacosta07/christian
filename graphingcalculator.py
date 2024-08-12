import sys
import random
import time
import math as m
import numpy as np

# if numpy doesnt import use cmd to install
#      py -3 -m  pip install numpy

# WINDOW CALIBRATION SOON

############ OPTIONS #############

darkmode = 0 # 0-1
coordinates = 1 # 0-1

decimals_place = 1 # 0-1

########z#### CAMERA #############

x_scale = 1
y_scale = 1

x_offset = 0
y_offset = 52

x_clamp = 52
y_clamp = 100

center_x = 1 # 0-1

##################################

x_scale = float(x_scale)
y_scale = float(y_scale*2)

def nlprint(a): # easier to type non line print
    sys.stdout.write(str(a))

for i in range(x_clamp):
    if center_x == 1: #x coordinate calculation
        x = ((i+x_offset)-(x_clamp/2))/x_scale
    else:
        x = (i+x_offset)/x_scale

    try:
        ############# GRAPH #############
        #linear     # x
        #sine wave  # m.sin(x)
        #parabola   # x**2
        #steps      # m.floor(x/4)*3

        expression = x
        #################################
    except:
        print("Expression invalid.")

    y = float(round((expression)*y_scale))

    for i in np.arange(np.clip(y+y_offset, None, y_clamp)):
        if round(i) == y_offset: #draw center line
            nlprint("\b▒")
        if y+y_offset < y_clamp: #not clamped
            if darkmode == 0:
                nlprint("█")
            else:
                nlprint("┄")
        else:                   #clampededed
            if darkmode == 0:
                nlprint("┄")
            else:
                nlprint(" ")

    if coordinates == 1: #coordinates enable/disable
        print("▓▒"+">┄┄┄┄┄<[" + str(round((x)*10**decimals_place)/10**decimals_place) + ", " + str(round((expression)*10**decimals_place)/10**decimals_place) + "]")
    else:
        print("▓▒")