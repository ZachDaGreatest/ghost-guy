import pygame
from options import make_button

def class_selection(screen, WIDTH, HEIGHT):

    scale_factor = HEIGHT / 600

    # fills the screen with black
    screen.fill((0,0,0))

    dagger_image = pygame.image.load('sprites\\menu_dagger.png')
    dagger_image = pygame.transform.scale_by(dagger_image, scale_factor*8)
    sword_image = pygame.image.load('sprites\\menu_sword.png')
    sword_image = pygame.transform.scale_by(sword_image, scale_factor*8)

    height_offset = dagger_image.get_rect()[3]/2
    horizontal_offset = dagger_image.get_rect()[2]/2

    screen.blit(dagger_image, (WIDTH/2 - horizontal_offset*3, HEIGHT/2 - height_offset))
    screen.blit(sword_image, (WIDTH/2 + horizontal_offset, HEIGHT/2 - height_offset))
    make_button(screen, scale_factor, 'ranger', 3.75, .05, [])
    make_button(screen, scale_factor, 'knight', 3.75, 1.175, [])

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            # if the user x's out then class selection makes running false
            if event.type == pygame.QUIT: return False, False

            # when the mouse is pressed the mouse pos is checked with the button pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (0) < x < (WIDTH/2):
                    # the ranger button is pressed so it returns to start game and the ranger class
                    return True, 'ranger'
                if (WIDTH/2) < x < (WIDTH):
                    # the options button is pressed so it returns to not start game while keeping up the main loop
                    return True, 'knight'
                
            if event.type == pygame.KEYDOWN: 
                # if escape is pressed so class selection returns to not start the game
                if event.key == pygame.K_ESCAPE: return False, False