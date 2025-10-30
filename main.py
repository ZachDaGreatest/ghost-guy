# uses pygame, random, and math
import pygame
from game_loop import game_loop
from menu import menu
from options import option_menu
from save_data import load_save_data, write_save_data

pygame.init()

# this records the monitors resolution for use in options when changing game resolution
monitor_width = pygame.display.Info().current_w
monitor_height = pygame.display.Info().current_h

# this grabs all info from given file
input_method, mode, high_score, resolution, is_fullscreen = load_save_data('save info.txt')

# take the resolution from save data and turns it into a height and width
HEIGHT = resolution    # factors of 240 work best
WIDTH = int(HEIGHT*(4/3))

# set up the screen object with pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ghost guy")

# if the game was saved in fullscreen the game will toggle into full screen
if is_fullscreen == 'fullscreen':
    pygame.display.toggle_fullscreen()

# the while loop is for changing between settings, the game, and quitting
gaming = True
while gaming:
    # the try except is for the first boot when there isn't info from game loop
    try: play, gaming = menu(screen, HEIGHT, WIDTH, elim_count, level)
    except: play, gaming = menu(screen, HEIGHT, WIDTH)
    # if menu returned true, true then the game runs
    if play: 
        # the try except is to avoid errors when quiting
        try: elim_count, level = game_loop(screen, HEIGHT, WIDTH, input_method, mode)
        except: break
        # this checks if there is a new high score
        if int(elim_count) > int(high_score): high_score = elim_count
    # if menu returned false, true the game loop doesn't run and the option menu does
    elif gaming: 
        gaming, input_method, mode, new_resolution, is_fullscreen = option_menu(screen, HEIGHT, WIDTH, input_method, mode, high_score, resolution, is_fullscreen, monitor_width, monitor_height)
        # if the resolution has changed the width and height are updated
        if new_resolution != resolution:
            resolution = new_resolution
            HEIGHT = resolution
            WIDTH = int(HEIGHT*(4/3))

# all save data is erased and replaced with new save data
write_save_data('save info.txt', input_method, mode, high_score, resolution, is_fullscreen)