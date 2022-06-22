import json
from calc_for_json import calc_in_grid
import sqlite3 as sql
from fun import str_as_list_into_list_int
#head_colour = "#0000FF", snake_colour_1 = "#00FF00", snake_colour_2 = "#009600"
# head_colour_rgb = [0, 0, 255], snake_colour_1_rgb = [0,255,0], snake_colour_2_rgb = [0,150,0]

# setting = open('settings.json',)
# setting_json = json.load(setting)

def write_logged(logged):
    with open('logged.json','w') as f:
        x = logged
        json.dump(x, f, indent=4)
        f.close()
    
# json.load(open('settings.json',))['head_colour_rgb']

def write(size,
    head_colour, snake_colour_1, snake_colour_2,
    if_hex, speed,length = 6,    
    head_colour_rgb = json.load(open('settings.json',))['head_colour_rgb'], snake_colour_1_rgb = json.load(open('settings.json',))['snake_colour_1_rgb'], snake_colour_2_rgb = json.load(open('settings.json',))['snake_colour_2_rgb'],
    head_colour_hex = json.load(open('settings.json',))['head_colour_hex'], snake_colour_1_hex = json.load(open('settings.json',))['snake_colour_1_hex'], snake_colour_2_hex = json.load(open('settings.json',))['snake_colour_2_hex']

    ):
    logged = json.load(open('logged.json',))
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
    setting = open('settings.json','w') if logged == False else open('account_settings.json','w')
    json.dump(x,setting,indent=4)

#write(35, "#0000FF", "#00FF00", "#009600", True, 8, 6, [0,0,255], [0,255,0], [0,150,0], "#0000FF", "#00FF00", "#009600")

def load_account_settings(username):
    setting = open('account_settings.json','w')
    con = sql.connect("Snake.sqlite3")
    cur = con.cursor()
    load_settings = f"SELECT * FROM Settings WHERE username = '{username}'"
    cur.execute(load_settings)
    fetch = cur.fetchone()
    print(fetch)
    print(fetch[10].replace('[','').replace(']','').replace(' ','').split(','))
    print('[]'.count('['))
    print(fetch[10].replace('[','').replace(']','').replace(' ','').split(','))
    
    #win_x, win_y, starting_x, starting_y, size, length, head_colour, snake_colour_1, snake_colour_2, head_colour_rgb, snake_colour_1_rgb, snake_colour_2_rgb, head_colour_hex, snake_colour_1_hex, snake_colour_2_hex, speed, if_hex = 
    x = {
        "win_x" : fetch[1],
        "win_y" : fetch[2],
        "starting_x" : fetch[3],
        "starting_y" : fetch[4],
        "size" : fetch[5],
        "length" : fetch[6],
        "head_colour" : str_as_list_into_list_int(fetch[7]) if fetch[7].count('[') + fetch[7].count(']') == 2 else fetch[7],
        "snake_colour_1" : str_as_list_into_list_int(fetch[8]) if fetch[8].count('[') + fetch[8].count(']') == 2 else fetch[8],
        "snake_colour_2" : str_as_list_into_list_int(fetch[9]) if fetch[9].count('[') + fetch[9].count(']') == 2 else fetch[9],
        "head_colour_rgb" : str_as_list_into_list_int(fetch[10]),
        "snake_colour_1_rgb" : str_as_list_into_list_int(fetch[11]),
        "snake_colour_2_rgb" : str_as_list_into_list_int(fetch[12]),
        "head_colour_hex" : fetch[13],
        "snake_colour_1_hex" : fetch[14],
        "snake_colour_2_hex" : fetch[15],
        "speed" : fetch[16],
        "if_hex" : True if fetch[17] == 'True' else False
        }
    json.dump(x, setting, indent=4)
    con.close()

#write(35,'#0000FF', '#00FF00', '#009600', True)

#    // "head_colour": "#320E3B",
#     // "snake_colour_1": "#EDF4ED",
#     // "snake_colour_2": "#4CB963"

# print(json.load(open('logged.json',)))