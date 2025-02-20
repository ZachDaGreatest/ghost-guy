import pygame

def menu(screen, elim_count, level, HEIGHT, WIDTH):
    screen.fill((0,0,0))

    scale_factor = HEIGHT / 600

    icon = pygame.image.load('original images\\Ospooky ghost.png')
    logo = pygame.image.load('sprites\\ghost guy logo.png')
    logo = pygame.transform.scale_by(logo,(10*scale_factor))
    start_button = pygame.image.load('sprites\\start button.png')
    start_button = pygame.transform.scale_by(start_button,(5*scale_factor))
    trophy_image = pygame.image.load('sprites\\trophy.png')
    trophy_image = pygame.transform.scale_by(trophy_image,(5*scale_factor))
    milmoe = pygame.image.load('original images\\milmoe.jpg')
    milmoe = pygame.transform.scale_by(milmoe,(scale_factor/2))

    screen.blit(logo, ((WIDTH-logo.get_rect()[2])/2,155*scale_factor))
    screen.blit(start_button, ((WIDTH-start_button.get_rect()[2])/2,370*scale_factor))
    screen.blit(milmoe, (WIDTH/2+65*scale_factor,265*scale_factor))
    font = pygame.font.SysFont('Pixeloid Sans', int(45*scale_factor))
    milmoe_text = font.render('MILMOE', False, (0, 0, 0))
    pygame.draw.rect(screen, (125,125,125), (WIDTH/2-scale_factor*145, 245*scale_factor, 190*scale_factor, 80*scale_factor))
    screen.blit(milmoe_text, (WIDTH/2-scale_factor*142, 260*scale_factor))

    #TODO add text of how you did in the previous run
    if level == 0:
        message = 'Click start or press space to begin!'
    else:
        message = 'you eliminated ' + elim_count + ' spooky ghosts reaching level ' + level
    pygame.font.init()
    font = pygame.font.SysFont('Pixeloid Sans', int(27*scale_factor))
    run_info = font.render(message, False, (169, 169, 169))
    screen.blit(run_info, ((WIDTH-run_info.get_rect()[2])/2,440*scale_factor))
    if int(level) >= 5:
        screen.blit(trophy_image, ((WIDTH-trophy_image.get_rect()[2])/2,480*scale_factor))

    pygame.display.set_icon(icon)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False,  False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if 312.5*scale_factor < x < 487.5*scale_factor and 370*scale_factor < y < 425*scale_factor:
                    return True, True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: return False,  False
                if event.key == pygame.K_SPACE: return True,  True