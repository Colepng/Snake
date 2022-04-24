import json
import calc

size = 50
win_x = calc.calc_in_grid(1000,size)
win_y = calc.calc_in_grid(800,size)
starting_x = calc.calc_in_grid(win_x/2,size)
starting_y = calc.calc_in_grid(win_y/2,size)
length = 4
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