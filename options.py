import pygame

classes = ['ranger', 'knight']
input_options = ['keyboard', 'mouse']
modes = ['dungeon', 'crypt', 'castle', 'endless']


def make_button(screen, scale_factor, text, object_num, bounds):

    x = 115*scale_factor
    y = 100*scale_factor + 100*scale_factor*object_num
    adjustment = 5*scale_factor

    pygame.font.init()
    font = pygame.font.Font('fonts\\PixeloidSans.ttf', int(54*scale_factor))
    button = font.render(text, False, (0, 0, 0))

    pygame.draw.rect(screen, (54,54,54), (x-3*adjustment, y-2*adjustment, button.get_rect()[2]+4.8*adjustment, button.get_rect()[3]+4*adjustment))
    pygame.draw.rect(screen, (85,85,85), (x-2*adjustment, y-1*adjustment, button.get_rect()[2]+2.8*adjustment, button.get_rect()[3]+2*adjustment))
    pygame.draw.rect(screen, (137,137,137), (x-1*adjustment, y+0*adjustment, button.get_rect()[2]+.8*adjustment, button.get_rect()[3]))
    screen.blit(button, (x, y))

    bounds.append((x-3*adjustment, y-2*adjustment, x-3*adjustment + button.get_rect()[2]*scale_factor-2*adjustment, y-2*adjustment + button.get_rect()[3]*scale_factor+2*adjustment))
    

def make_menu(screen, HEIGHT, info):
    screen.fill((0,0,0))

    scale_factor = HEIGHT / 600

    options_image = pygame.image.load('sprites\\options image.png')
    options_image = pygame.transform.scale_by(options_image,(9*scale_factor))

    screen.blit(options_image, (100*scale_factor,50*scale_factor))

    bounds = []
    for num in range(len(info)):
        make_button(screen, scale_factor, info[num], num+1, bounds)

    pygame.display.flip()

    return bounds

def cycle(current):
    if current in classes:
        try:
            index = classes.index(current) + 1
            return classes[index]
        except:
            return classes[0]
        
    if current in input_options:
        try:
            index = input_options.index(current) + 1
            return input_options[index]
        except:
            return input_options[0]
        
    if current in modes:
        try:
            index = modes.index(current) + 1
            return modes[index]
        except:
            return modes[0]


def option_menu(screen, HEIGHT, WIDTH, chosen_class, input_method, mode):

    info = [input_method, mode, chosen_class]

    bounds = make_menu(screen, HEIGHT, info)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False,  False, 'n/a', 'n/a', 'n/a'
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                for button in bounds:
                    if button[0] < x < button[2] and button[1] < y < button[3]:
                        index = bounds.index(button)
                        info[index] = cycle(info[index])
                        bounds = make_menu(screen, HEIGHT, info)
                
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: return True, info[0], info[1], info[2]
                if event.key == pygame.K_SPACE: return True, info[0], info[1], info[2]