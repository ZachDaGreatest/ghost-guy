#uses pygame, random, and math
import pygame
from game_loop import game_loop
from menu import menu
from options import option_menu
 
pygame.init()

HEIGHT = 720    #factors of 240 work best
WIDTH = int(HEIGHT*(4/3))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ghost guy")
elim_count = 0
level = 0

# pygame.display.toggle_fullscreen()

input_method = 'keyboard' #can be 'keyboard' or 'mouse'

chosen_class = 'ranger' #ranger is the default class, modify for testing
# chosen_class = 'knight'

gaming = True
while gaming:
    play, gaming = menu(screen, elim_count, level, HEIGHT, WIDTH)
    if play: elim_count, level = game_loop(screen, HEIGHT, WIDTH, chosen_class, input_method)
    elif gaming: gaming, chosen_class = option_menu(screen, HEIGHT, WIDTH, chosen_class)