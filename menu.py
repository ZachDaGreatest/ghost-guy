import pygame

# accepts the pygame screen, height and width values, and run info
# run info [0] is elim cound and [1] is the level from previous run, they are optional to avoid first boot errors
def menu(screen, HEIGHT, WIDTH, *run_info):
    # The second piece of run info is the level reached, and it is stored for use in
    try: lvl = int(run_info[1])
    except: lvl = 0

    # This erases anything that was previously on the screen
    screen.fill((0,0,0))

    # the scale factor makes everything look the same no matter the resolution
    scale_factor = HEIGHT / 600

    # load all of the images
    icon = pygame.image.load('original images\\Ospooky ghost.png')
    logo = pygame.image.load('sprites\\ghost guy logo.png')
    logo = pygame.transform.scale_by(logo,(10*scale_factor))
    start_button = pygame.image.load('sprites\\start button.png')
    start_button = pygame.transform.scale_by(start_button,(5*scale_factor))
    options_button = pygame.image.load('sprites\\options image.png')
    options_button = pygame.transform.scale_by(options_button,(5*scale_factor))
    trophy_image = pygame.image.load('sprites\\trophy.png')
    trophy_image = pygame.transform.scale_by(trophy_image,(5*scale_factor))

    # draw the logo and buttons on the screen
    screen.blit(logo, ((WIDTH-logo.get_rect()[2])/2,155*scale_factor))
    screen.blit(start_button, ((WIDTH-start_button.get_rect()[2])/2,370*scale_factor))
    screen.blit(options_button, ((WIDTH-options_button.get_rect()[2])/2,490*scale_factor))

    # if you have a run it tells you how you did, otherwise it tells you how to start
    try: message = f'you eliminated {run_info[0]} spooky ghosts reaching level {str(lvl)}'
    except: message = 'Click start or press space to begin!'

    # the message is taken and turned into a screen object that is put on the screen
    pygame.font.init()
    font = pygame.font.Font('fonts\\PixeloidSans.ttf', int(27*scale_factor))
    run_info = font.render(message, False, (169, 169, 169))
    screen.blit(run_info, ((WIDTH-run_info.get_rect()[2])/2,440*scale_factor))

    # TODO make trophy actualy spawn
    # if the player got to level 5 a trophy is displayed
    if lvl >= 5: 
        screen.blit(trophy_image, ((WIDTH-trophy_image.get_rect()[2])/2,50*scale_factor))

    # the icon is set to a ghost picture and the screen is updated
    pygame.display.set_icon(icon)
    pygame.display.flip()
    
    # the main loop of the menu waiting for user input
    while True:
        for event in pygame.event.get():
            # if the user x's out then the menu returns to not start the game and not continue the main loop
            if event.type == pygame.QUIT: return False,  False

            # when the mouse is pressed the mouse pos is checked with the button pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if 312.5*scale_factor < x < 487.5*scale_factor and 370*scale_factor < y < 425*scale_factor:
                    # the start button is pressed so it returns to start game and keep up the main loop
                    return True, True
                if 295*scale_factor < x < 505*scale_factor and 490*scale_factor < y < 545*scale_factor:
                    # the options button is pressed so it returns to not start game while keeping up the main loop
                    return False, True
                
            if event.type == pygame.KEYDOWN: 
                # if escape is pressed the menu returns to not start the game and not continue the main loop
                if event.key == pygame.K_ESCAPE: return False,  False
                if event.key == pygame.K_SPACE: return True,  True