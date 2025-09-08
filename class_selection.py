import pygame
from options import make_button

# add lines so that you use multiple of the light gray box behind text with one big dark gray box
def make_text_box(screen, scale_factor, cords, text_list):

    adjustment = 5*scale_factor
    x, y = cords
    y_offset = 0
    x_offset = 0
    lines = []

    pygame.font.init()
    font = pygame.font.Font('fonts\\PixeloidSans.ttf', int(15*scale_factor))
    for text in text_list:
        lines.append(font.render(text, False, (0, 0, 0)))

    lengths = []
    for text in lines:
        lengths.append(text.get_rect()[2])
    lengths.sort(reverse=True)

    pygame.draw.rect(screen, (54,54,54), (x-1.5*adjustment - lengths[0]/2, y-.5*adjustment + y_offset, lengths[0] + 2*adjustment, lines[0].get_rect()[3]*len(lines) + adjustment))
    pygame.draw.rect(screen, (137,137,137), (x-1*adjustment - lengths[0]/2, y+0*adjustment + y_offset, lengths[0] + 1*adjustment, lines[0].get_rect()[3]*len(lines)))

    for text in lines:
        x_offset = (lengths[0] - text.get_rect()[2]) / 2 - lengths[0]/2

        screen.blit(text, (x + x_offset, y + y_offset))

        y_offset += text.get_rect()[3]

def class_selection(screen, WIDTH, HEIGHT):

    dagger_description = ['There is a dull magic dagger', 'It can fire bolts across the battlefield', 'Comes with regular armor']
    sword_description = ['There is a very sharp sword', 'Anything that touches it will take damage', 'Comes with extra strong armor']

    scale_factor = HEIGHT / 600

    # fills the screen with black
    screen.fill((0,0,0))

    dagger_image = pygame.image.load('sprites\\menu_dagger.png')
    dagger_image = pygame.transform.scale_by(dagger_image, scale_factor*8)
    sword_image = pygame.image.load('sprites\\menu_sword.png')
    sword_image = pygame.transform.scale_by(sword_image, scale_factor*8)

    height_offset = dagger_image.get_rect()[3]
    horizontal_offset = dagger_image.get_rect()[2]/2

    screen.blit(dagger_image, (WIDTH/2 - horizontal_offset*3, HEIGHT/2 - height_offset))
    screen.blit(sword_image, (WIDTH/2 + horizontal_offset, HEIGHT/2 - height_offset))
    make_button(screen, scale_factor, 'ranger', 2.5, .05, [])
    make_button(screen, scale_factor, 'knight', 2.5, 1.175, [])
    make_text_box(screen, scale_factor, (WIDTH/2 - horizontal_offset*2, HEIGHT/2 + height_offset/16*9), dagger_description)
    make_text_box(screen, scale_factor, (WIDTH/2 + horizontal_offset*2, HEIGHT/2 + height_offset/16*9), sword_description)

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
                # returns ranger so there isn't a keyerror when the class is pluged into the player class
                if event.key == pygame.K_ESCAPE: return False, 'ranger'