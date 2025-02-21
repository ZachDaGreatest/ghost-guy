import pygame

def option_menu(screen, HEIGHT, WIDTH, chosen_class):
    screen.fill((0,0,0))

    scale_factor = HEIGHT / 600

    start_button = pygame.image.load('sprites\\start button.png')
    start_button = pygame.transform.scale_by(start_button,(5*scale_factor))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False,  False, 'n/a'
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if 312.5*scale_factor < x < 487.5*scale_factor and 370*scale_factor < y < 425*scale_factor:
                    return True, True, chosen_class
                if 295*scale_factor < x < 505*scale_factor and 490*scale_factor < y < 545*scale_factor:
                    return False, True, chosen_class
                
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: return True, chosen_class
                if event.key == pygame.K_SPACE: return True, chosen_class