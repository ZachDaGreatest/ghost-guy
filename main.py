import pygame
from game_loop import game_loop
from menu import menu
 
pygame.init()

HEIGHT = 720    #factors of 240 work best
WIDTH = int(HEIGHT*(4/3))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ghost guy")
elim_count = 0
level = 0

# pygame.display.toggle_fullscreen()

gaming = True
while gaming:
    play, gaming = menu(screen, elim_count, level, HEIGHT, WIDTH)
    if play: elim_count, level = game_loop(screen, HEIGHT, WIDTH) 