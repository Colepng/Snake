import pickle
import pygame
import json

def get_logged():
    logged = json.load(open('logged.json',))
    return logged
def get_highscore():
    logged = json.load(open('logged.json',))
    filename = "highscore.pk" if not logged else "highscore_account.pk"
    with open(filename, "rb") as f: 
        unpick = pickle.Unpickler(f)
        return unpick.load()
def get_username():
    return json.load(open('logged.json',))["username"]


def calc_in_grid(num_to_round, grid_size):
    return round(num_to_round/grid_size)*grid_size

def set_up_highscore():
    logged = json.load(open('logged.json',))
    filename = "highscore.pk" if logged == False else "highscore_account.pk"
    with open(filename,  "wb") as f:
        highscore = 0
        pickle.dump(highscore, f)
    with open(filename,  "rb") as f:
        unpick = pickle.Unpickler(f)
        print(unpick.load())

def drawGrid(surface,colour, size):
    blockSize = size#Set the size of the grid block
    #print(blockSize)
    for x in range(0, 1000, blockSize):
        for y in range(0, 800, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, colour, rect, 1)

def calc_mid_of_rect_for_text(outside_rect, text):
    return ((outside_rect.width - text.get_width())/2 + outside_rect.x, (outside_rect.height - text.get_height())/2 + outside_rect.y)
            

def calc_offset_of_outside_text(rect, text):
    return (rect.x - text.get_width(),(rect.height - text.get_height())/2 + rect.y)
    #(head_colour_input_rect.x - head_colour_surface.get_width(),head_colour_input_rect.height - head_colour_surface.get_height()/2 + head_colour_input_rect.y))

def list_into_str(list):
    first_run = True
    list_as_str = ''
    for i in range(len(list)): #0,0,255 = [0,1,2]
        if first_run ==  True:
            list_as_str = list_as_str + str(list[i]) #list[0] = 0            str(0) = "0"
            first_run = False
        else:
            list_as_str = list_as_str + ',' + str(list[i]) # "0" + ',' + "0"        thired run "0,0" + ', + "255"
        #print(list_as_str)
    return list_as_str

def draw_surfaces(screen, input_surface, text_surface, rect):
    screen.blit(input_surface, calc_mid_of_rect_for_text(rect, input_surface))
    screen.blit(text_surface, calc_offset_of_outside_text(rect, text_surface))

def update_account_highscore(score):
    with open("highscore_account.pk", "wb") as f:
        pickle.dump(score, f)

def str_as_list_into_list_int(list):
    list_str = list.replace('[','').replace(']','').replace(' ','').split(',')
    return [int(i) for i in list_str]