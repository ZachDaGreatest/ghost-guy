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
input_method, chosen_class, mode, high_score, resolution, is_fullscreen = load_save_data('save info.txt')

HEIGHT = resolution    # factors of 240 work best
WIDTH = int(HEIGHT*(4/3))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ghost guy")

if is_fullscreen == 'fullscreen':
    pygame.display.toggle_fullscreen()

# FIXME when you click space to go out of options and then click space again it crashes
# this only occures after changing the screen resolution
# code breaks if you quit to fast after changing resolution
gaming = True
while gaming:
    # the try except is for the first boot when there isn't info from game loop
    try: play, gaming = menu(screen, HEIGHT, WIDTH, elim_count, level)
    except: play, gaming = menu(screen, HEIGHT, WIDTH)
    # if menu returned true, true then the game runs
    if play: 
        elim_count, level = game_loop(screen, HEIGHT, WIDTH, chosen_class, input_method, mode)
        # this checks if there is a new high score
        if int(elim_count) > int(high_score): high_score = elim_count
    # if menu returned false, true the game loop doesn't run and the option menu does
    elif gaming: 
        gaming, input_method, mode, chosen_class, new_resolution, is_fullscreen = option_menu(screen, HEIGHT, WIDTH, chosen_class, input_method, mode, high_score, resolution, is_fullscreen, monitor_width, monitor_height)
        if new_resolution != resolution:
            resolution = new_resolution
            HEIGHT = resolution
            WIDTH = int(HEIGHT*(4/3))

# all save data is erased and replaced with new save data
write_save_data('save info.txt', input_method, chosen_class, mode, high_score, resolution, is_fullscreen)