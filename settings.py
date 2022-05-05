import json
from calc_for_json import calc_in_grid
#head_colour = "#0000FF", snake_colour_1 = "#00FF00", snake_colour_2 = "#009600"
# head_colour_rgb = [0, 0, 255], snake_colour_1_rgb = [0,255,0], snake_colour_2_rgb = [0,150,0]

setting = open('settings.json',)
setting_json = json.load(setting)

json.load(open('settings.json',))['head_colour_rgb']

def write(size,
    head_colour, snake_colour_1, snake_colour_2,
    if_hex, speed,length = 6,    
    head_colour_rgb = json.load(open('settings.json',))['head_colour_rgb'], snake_colour_1_rgb = json.load(open('settings.json',))['snake_colour_1_rgb'], snake_colour_2_rgb = json.load(open('settings.json',))['snake_colour_2_rgb'],
    head_colour_hex = json.load(open('settings.json',))['head_colour_hex'], snake_colour_1_hex = json.load(open('settings.json',))['snake_colour_1_hex'], snake_colour_2_hex = json.load(open('settings.json',))['snake_colour_2_hex']

    ):
    
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
        "head_colour_rgb" : head_colour_rgb,
        "snake_colour_1_rgb" : snake_colour_1_rgb,
        "snake_colour_2_rgb" : snake_colour_2_rgb,
        "head_colour_hex" : head_colour_hex,
        "snake_colour_1_hex" : snake_colour_1_hex,
        "snake_colour_2_hex" : snake_colour_2_hex,
        "speed" : speed,
        "if_hex" : if_hex
    }
    setting = open('settings.json','w')
    json.dump(x,setting,indent=4)

#write(35,'#0000FF', '#00FF00', '#009600', True)

#    // "head_colour": "#320E3B",
#     // "snake_colour_1": "#EDF4ED",
#     // "snake_colour_2": "#4CB963"