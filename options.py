import pygame
from pygame._sdl2 import Window

# these lists contain all possible options for the different catagories in the options menu
input_options = ['keyboard', 'mouse']
modes = ['dungeon', 'crypt', 'castle', 'endless']
resolutions = ['res: 480p', 'res: 720p', 'res: 960p']
fullscreen = ['fullscreen', 'windowed']


# this function can be used to brighten the screen by a desired amount
def brighten_screen(screen, amount):
    brightness_filter = pygame.surface.Surface((screen.get_size()))
    brightness_filter.fill((amount, amount, amount))
    screen.blit(brightness_filter, (0,0), special_flags=pygame.BLEND_RGB_ADD)


# this function makes a button with text displayed
def make_button(screen, scale_factor, text, object_num, collum, bounds):
    # uses given info to determine where to place the button on the screen
    adjustment = 5*scale_factor
    x = 50*scale_factor + 3*adjustment + scale_factor*400*collum
    y = 74*scale_factor + 100*scale_factor*object_num

    # initializes the font used on the button
    pygame.font.init()
    font = pygame.font.Font('fonts\\PixeloidSans.ttf', int(54*scale_factor))
    button = font.render(text, False, (0, 0, 0))

    # draws the outline of the botton along with the text for the button
    pygame.draw.rect(screen, (54,54,54), (x-3*adjustment, y-2*adjustment, button.get_rect()[2] + 4.8*adjustment, button.get_rect()[3] + 4*adjustment))
    pygame.draw.rect(screen, (85,85,85), (x-2*adjustment, y-1*adjustment, button.get_rect()[2] + 2.8*adjustment, button.get_rect()[3] + 2*adjustment))
    pygame.draw.rect(screen, (137,137,137), (x-1*adjustment, y+0*adjustment, button.get_rect()[2] + .8*adjustment, button.get_rect()[3]))
    screen.blit(button, (x, y))

    # this takes the bounds list that was given and adds the bounds of the created button
    # bounds.append((x-3*adjustment, y-2*adjustment, x-3*adjustment + button.get_rect()[2]*scale_factor-2*adjustment, y-2*adjustment + button.get_rect()[3]*scale_factor+2*adjustment))
    bounds.append((x-3*adjustment, y-2*adjustment, (x-3*adjustment) + button.get_rect()[2] + 4.8*adjustment, (y-2*adjustment) + button.get_rect()[3] + 4*adjustment))
    

# this function draws the menu
def make_menu(screen, HEIGHT, info):
    # reset the screen to black
    screen.fill((0,0,0))

    # set the scale based on the screen height
    scale_factor = HEIGHT / 600

    # load, scale, and place the sprite for the options logo
    options_image = pygame.image.load('sprites\\options image.png')
    options_image = pygame.transform.scale_by(options_image,(9*scale_factor))
    screen.blit(options_image, (50*scale_factor,50*scale_factor))

    # create a list that will store the bounds for the different buttons
    bounds = []
    # the loop is to place each button in a different collum/row
    for num in range(len(info)):
        if num < 4:
            make_button(screen, scale_factor, info[num], num+1, 0, bounds)
        else:
            make_button(screen, scale_factor, info[num], num+1-4, 1, bounds)

    # update the screen so the user can view the changes
    pygame.display.flip()

    # returns the list of bounds for the created buttons
    return bounds


# this function figures out what catagory the selected choice is from, and what the next option is
def cycle(current):    
    if current in input_options:
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
    
    elif current in fullscreen:
        try:
            index = fullscreen.index(current) + 1
            return fullscreen[index]
        except:
            return fullscreen[0]
        
    else:
        return current


# this is the main fuction for the opttions menu
def option_menu(screen, HEIGHT, WIDTH, input_method, mode, high_score, resolution, is_fullscreen, monitor_width, monitor_height):

    # create a list with all of the supplied info
    info = [input_method, mode, f'res: {resolution}p', is_fullscreen, f'best {high_score}', 'quit']

    # draws the menu and retrieves the bounds of all created buttons
    bounds = make_menu(screen, HEIGHT, info)

    # this is the main loop of the menu
    while True:
        for event in pygame.event.get():
            # if the user quits through the x or escape the menu tells the program to stop running while passing back all of the current info
            if event.type == pygame.QUIT: return False,  info[0], info[1], info[2], int(info[3])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False,  info[0], info[1], info[2], int(info[3])
            # this runs when there is a mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get the current position of the mouse
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # check the current position with all of the button bounds to figure out if a button was pressed
                for button in bounds:
                    if button[0] < x < button[2] and button[1] < y < button[3]:
                        # if a button is pressed, the current info on the button is cycled to the next option
                        index = bounds.index(button)
                        info[index] = cycle(info[index])

                        # if the quite button is pressed the used is returned to the main menu
                        if info[index] == False:
                            try: return True, info[0], info[1], int(info[2][5:8]), info[3] # except is for 4 didgit resolutions
                            except: return True, info[0], info[1], int(info[2][5:9]), info[3]

                        # this is for a resolution change
                        if info[index] in resolutions:
                            current_screen_state = pygame.display.is_fullscreen()
                            try: HEIGHT = int(info[index][5:8]) # only takes characters 4-7 to only get resolution
                            except: HEIGHT = int(info[index][5:9]) # except is for 4 digit resolutions
                            WIDTH = int(HEIGHT*(4/3))
                            screen = pygame.display.set_mode((WIDTH, HEIGHT))
                            window = Window.from_display_module()
                            width_offset = (monitor_width - WIDTH)/2
                            height_offset = (monitor_height - HEIGHT)/2
                            window.position = (width_offset, height_offset)
                            if current_screen_state == True:
                                pygame.display.toggle_fullscreen()
                        
                        # if the fullscreen button was pressed than the screen is toggled
                        elif info[index] in fullscreen:
                            pygame.display.toggle_fullscreen()

                        # redraws the menu and gets the new bounds for the buttons
                        bounds = make_menu(screen, HEIGHT, info)
                
            # code breaks if you quit to fast after changing resolution
            # if event.type == pygame.KEYDOWN: 
            #     if event.key == pygame.K_ESCAPE: return True, info[0], info[1], info[2], int(info[3])
            #     if event.key == pygame.K_SPACE: return True, info[0], info[1], info[2], int(info[3])