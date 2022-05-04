import json
from calc_for_json import calc_in_grid
#head_colour = "#0000FF", snake_colour_1 = "#00FF00", snake_colour_2 = "#009600"
def write(size, if_hex=False, length = 6, head_colour = [0, 0, 255], snake_colour_1 = [0,255,0], snake_colour_2 = [0,150,0]):
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
        "length" : length,
        "head_colour" : head_colour,
        "snake_colour_1" : snake_colour_1,
        "snake_colour_2" : snake_colour_2,
        "if_hex" : if_hex
    }
    setting = open('settings.json','w')
    json.dump(x,setting,indent=4)

#write(35)

#    // "head_colour": "#320E3B",
#     // "snake_colour_1": "#EDF4ED",
#     // "snake_colour_2": "#4CB963"