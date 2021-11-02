import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

import numpy as np
import matplotlib.pyplot as plt
def build_E_example(n_tiles):
    xx, yy = np.meshgrid(range(n_tiles), range(n_tiles))
    
    vstick_start_x = int (n_tiles * 2 / 8)
    vstick_stop_x = int(n_tiles * 3 / 8)
    vstick_start_y = int(n_tiles * 1 / 8)
    vstick_stop_y = int(n_tiles * 7 / 8)
    vstick = (xx>=vstick_start_x) & (xx<vstick_stop_x) & (yy>=vstick_start_y) & (yy<vstick_stop_y)
    
    upstick_start_x = int (n_tiles * 2 / 8)
    upstick_stop_x = int(n_tiles * 6 / 8)
    upstick_start_y = int(n_tiles * 1 / 8)
    upstick_stop_y = int(n_tiles * 2 / 8)
    upstick = (xx>=upstick_start_x) & (xx<upstick_stop_x) & (yy>=upstick_start_y) & (yy<upstick_stop_y)
    
    midstick_start_x = int (n_tiles * 2 / 8)
    midstick_stop_x = int(n_tiles * 5 / 8)
    midstick_start_y = int(n_tiles * 4 / 8)
    midstick_stop_y = int(n_tiles * 5 / 8)
    midstick = (xx>=midstick_start_x) & (xx<midstick_stop_x) & (yy>=midstick_start_y) & (yy<midstick_stop_y)

    botstick_start_x = int (n_tiles * 2 / 8)
    botstick_stop_x = int(n_tiles * 6 / 8)
    botstick_start_y = int(n_tiles * 6 / 8)
    botstick_stop_y = int(n_tiles * 7 / 8)
    botstick = (xx>=botstick_start_x) & (xx<botstick_stop_x) & (yy>=botstick_start_y) & (yy<botstick_stop_y)

    capital_E = vstick | upstick | midstick | botstick

    return capital_E

n_tiles = 50
x= np.linspace(-0.5,0.5,n_tiles)
y= np.linspace(-0.5,0.5,n_tiles)
XX, YY = np.meshgrid(x,y)
plt.contourf(XX,YY, build_E_example(n_tiles), 1)  
plt.show()
