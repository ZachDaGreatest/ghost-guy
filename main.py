#uses pygame, random, and math
import pygame
from game_loop import game_loop
from menu import menu
from options import option_menu
 
pygame.init()

HEIGHT = 720    # factors of 240 work best
WIDTH = int(HEIGHT*(4/3))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ghost guy")

# pygame.display.toggle_fullscreen()

input_method = 'keyboard' # can be 'keyboard' or 'mouse'

chosen_class = 'ranger' # can be 'ranger' or 'knight' with 'ranger' being default

mode = 'dungeon' # 'dungeon' is the normal mode and 'endless' is the wave based mode

gaming = True
while gaming:
    # the try except is for the first boot when there isn't info from game loop
    try: play, gaming = menu(screen, HEIGHT, WIDTH, elim_count, level)
    except: play, gaming = menu(screen, HEIGHT, WIDTH)
    # if menu returned true, true then the game runs
    if play: elim_count, level = game_loop(screen, HEIGHT, WIDTH, chosen_class, input_method, mode)
    # if menu returned false, true the game loop doesn't run and the option menu does
    elif gaming: gaming, chosen_class = option_menu(screen, HEIGHT, WIDTH, chosen_class)