import pygame
from pygame._sdl2 import Window

classes = ['ranger', 'knight']
input_options = ['keyboard', 'mouse']
modes = ['dungeon', 'crypt', 'castle', 'endless']
resolutions = ['480', '720', '960']


def make_button(screen, scale_factor, text, object_num, collum, bounds):

    adjustment = 5*scale_factor
    x = 50*scale_factor + 3*adjustment + scale_factor*400*collum
    y = 74*scale_factor + 100*scale_factor*object_num

    pygame.font.init()
    font = pygame.font.Font('fonts\\PixeloidSans.ttf', int(54*scale_factor))
    button = font.render(text, False, (0, 0, 0))

    pygame.draw.rect(screen, (54,54,54), (x-3*adjustment, y-2*adjustment, button.get_rect()[2] + 4.8*adjustment, button.get_rect()[3] + 4*adjustment))
    pygame.draw.rect(screen, (85,85,85), (x-2*adjustment, y-1*adjustment, button.get_rect()[2] + 2.8*adjustment, button.get_rect()[3] + 2*adjustment))
    pygame.draw.rect(screen, (137,137,137), (x-1*adjustment, y+0*adjustment, button.get_rect()[2] + .8*adjustment, button.get_rect()[3]))
    screen.blit(button, (x, y))

    # bounds.append((x-3*adjustment, y-2*adjustment, x-3*adjustment + button.get_rect()[2]*scale_factor-2*adjustment, y-2*adjustment + button.get_rect()[3]*scale_factor+2*adjustment))
    bounds.append((x-3*adjustment, y-2*adjustment, (x-3*adjustment) + button.get_rect()[2] + 4.8*adjustment, (y-2*adjustment) + button.get_rect()[3] + 4*adjustment))
    

def make_menu(screen, HEIGHT, info):
    screen.fill((0,0,0))

    scale_factor = HEIGHT / 600

    options_image = pygame.image.load('sprites\\options image.png')
    options_image = pygame.transform.scale_by(options_image,(9*scale_factor))

    screen.blit(options_image, (50*scale_factor,50*scale_factor))

    bounds = []
    for num in range(len(info)):
        if num < 3:
            make_button(screen, scale_factor, info[num], num+1, 0, bounds)
        else:
            make_button(screen, scale_factor, info[num], num+1-3, 1, bounds)

    pygame.display.flip()

    return bounds

def cycle(current):
    if current in classes:
        try:
            index = classes.index(current) + 1
            return classes[index]
        except:
            return classes[0]
        
    elif current in input_options:
        try:
            index = input_options.index(current) + 1
            return input_options[index]
        except:
            return input_options[0]
        
    elif current in modes:
        try:
            index = modes.index(current) + 1
            return modes[index]
        except:
            return modes[0]
        
    elif current in resolutions:
        try:
            index = resolutions.index(current) + 1
            return resolutions[index]
        except:
            return resolutions[0]
        
    elif current == 'quit':
        return False
        
    else:
        return current


def option_menu(screen, HEIGHT, WIDTH, chosen_class, input_method, mode, high_score, resolution, monitor_width, monitor_height):

    info = [input_method, mode, chosen_class, str(resolution), f'best {high_score}', 'quit']

    bounds = make_menu(screen, HEIGHT, info)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False,  info[0], info[1], info[2], int(info[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                for button in bounds:
                    if button[0] < x < button[2] and button[1] < y < button[3]:
                        index = bounds.index(button)
                        info[index] = cycle(info[index])
                        if info[index] == False:
                            return True, info[0], info[1], info[2], int(info[3])
                        if info[index] in resolutions:
                            HEIGHT = int(info[index])
                            WIDTH = int(HEIGHT*(4/3))
                            screen = pygame.display.set_mode((WIDTH, HEIGHT))
                            window = Window.from_display_module()
                            width_offset = (monitor_width - WIDTH)/2
                            height_offset = (monitor_height - HEIGHT)/2
                            window.position = (width_offset, height_offset)
                        bounds = make_menu(screen, HEIGHT, info)
                
            # code breaks if you quit to fast after changing resolution
            # if event.type == pygame.KEYDOWN: 
            #     if event.key == pygame.K_ESCAPE: return True, info[0], info[1], info[2], int(info[3])
            #     if event.key == pygame.K_SPACE: return True, info[0], info[1], info[2], int(info[3])