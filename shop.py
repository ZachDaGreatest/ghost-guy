import pygame
from class_selection import make_text_box, make_button

class shop():
    def __init__(self, player, WIDTH, HEIGHT):
        self.scale_factor = HEIGHT / 600
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT


        self.player = player
        self.chosen_class = player.chosen_class

        damage_upgrade_image = pygame.image.load('sprites\\damage icon.png')
        self.damage_upgrade_image = pygame.transform.scale_by(damage_upgrade_image, self.scale_factor*8)
        life_upgrade_image = pygame.image.load('sprites\\life icon.png')
        self.life_upgrade_image = pygame.transform.scale_by(life_upgrade_image, self.scale_factor*8)
        health_image = pygame.image.load('sprites\\health icon.png')
        self.health_image = pygame.transform.scale_by(health_image, self.scale_factor*8)

    def display_shop(self, screen):
        height_offset = self.life_upgrade_image.get_rect()[3]
        horizontal_offset = self.life_upgrade_image.get_rect()[2]/2

        screen.fill((0,0,0))
        screen.blit(self.life_upgrade_image, (self.WIDTH/2-3*horizontal_offset, self.HEIGHT/2-height_offset*2/3))
        make_text_box(screen, self.scale_factor, (self.WIDTH/3*2+horizontal_offset, self.HEIGHT/2+height_offset*2/3), ['Upgrade Your Health', 'increases max hp', 'or regens lost hp'])
        screen.blit(self.health_image, (self.WIDTH/2+horizontal_offset, self.HEIGHT/2-height_offset*2/3))
        make_text_box(screen, self.scale_factor, (self.WIDTH/3-horizontal_offset, self.HEIGHT/2+height_offset*2/3), ['Upgrade Your Defence', 'increases dodge chance', 'or regens lost hp'])
        screen.blit(self.damage_upgrade_image, (self.WIDTH/2-horizontal_offset, self.HEIGHT/2-height_offset*2/3))
        if self.player.chosen_class == 'ranger':
            make_text_box(screen, self.scale_factor, (self.WIDTH/2, self.HEIGHT/2+height_offset*2/3), ['Upgrade Your Attack', 'increases pierce', 'or increases damage'])
        else:
            make_text_box(screen, self.scale_factor, (self.WIDTH/2, self.HEIGHT/2+height_offset*2/3), ['Upgrade Your Attack', 'increases swing speed'])
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                # pygame.QUIT is activating imediately every time
                # if event.type == pygame.QUIT(): return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > self.WIDTH/3*2:
                        # health upgrade
                        if self.player.hp <= self.player.max_hp-2:
                            self.player.hp += 2
                        else:
                            self.player.max_hp += 1
                            self.player.hp = self.player.max_hp
                        return True
                    elif x > self.WIDTH/3:
                        # attack upgrade
                        if self.player.chosen_class == 'ranger':
                            if self.player.pierce <= self.player.damage:
                                self.player.pierce += 1
                            else:
                                self.player.damage += 1
                        else:
                            self.player.slash_speed += .05
                        return True
                    else:
                        # defence upgrade
                        if self.player.dodge_chance < 70:
                            self.player.dodge_chance += 10
                        else:
                            if self.player.hp <= self.player.max_hp-2:
                                self.player.hp += 2
                            else:
                                self.player.max_hp += 1
                                self.player.hp = self.player.max_hp
                        return True