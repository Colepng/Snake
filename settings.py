import json
from calc_for_json import calc_in_grid

# size = 35
# win_x = calc_in_grid(1000,size)
# win_y = calc_in_grid(800,size)
# starting_x = calc_in_grid(win_x/2,size)
# starting_y = calc_in_grid(win_y/2,size)
# length = 4

def write(size, length = 4):
    win_x = calc_in_grid(1000,size)
    win_y = calc_in_grid(800,size)
    print(win_x/2, win_y/2, win_x, win_y)
    starting_x = calc_in_grid(win_x/2,size)
    starting_y = calc_in_grid(win_y/2,size)
    print(starting_x, starting_y)
    x = {
        "win_x" : win_x,
        "win_y" : win_y,
        "starting_x" : starting_x,
        "starting_y" : starting_y,
        "size" : size,
        "length" : length
    }
    setting = open('settings.json','w')
    json.dump(x,setting,indent=4)