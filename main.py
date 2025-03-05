#uses pygame, random, and math
import pygame
from game_loop import game_loop
from menu import menu
from options import option_menu
 
pygame.init()

# the try except is to set everything to defaults incase the 'save info.txt' file has an error
try:
    # save info.txt has all saved settings
    save_info = open('save info.txt', 'r')
    for line in save_info:
        for character in line:
            if character == 'I':
                input_method = ''
                for num in range(len(line)-3):
                    input_method += line[num+2]
            if character == 'C':
                chosen_class = ''
                for num in range(len(line)-3):
                    chosen_class += line[num+2]
            if character == 'M':
                mode = ''
                for num in range(len(line)-3):
                    mode += line[num+2]
    # the info list is to make sure that all needed data is found
    info = [input_method, chosen_class, mode]
except:
    print('save data is corrupted')
    input_method = 'keyboard' 
    chosen_class = 'ranger' # can be 'ranger' or 'knight' with 'ranger' being default
    mode = 'castle' # 'dungeon', 'crypt', and 'castle' are normal mode and 'endless' is the wave based mode

HEIGHT = 720    # factors of 240 work best
WIDTH = int(HEIGHT*(4/3))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ghost guy")

pygame.display.toggle_fullscreen()

gaming = True
while gaming:
    # the try except is for the first boot when there isn't info from game loop
    try: play, gaming = menu(screen, HEIGHT, WIDTH, elim_count, level)
    except: play, gaming = menu(screen, HEIGHT, WIDTH)
    # if menu returned true, true then the game runs
    if play: elim_count, level = game_loop(screen, HEIGHT, WIDTH, chosen_class, input_method, mode)
    # if menu returned false, true the game loop doesn't run and the option menu does
    elif gaming: gaming, input_method, mode, chosen_class = option_menu(screen, HEIGHT, WIDTH, chosen_class, input_method, mode)


save_info = open('save info.txt', 'w')
save_info.write(f'I {input_method}\n')
save_info.write(f'C {chosen_class}\n')
save_info.write(f'M {mode}\n')