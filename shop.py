import pygame
from class_selection import make_text_box, make_button

class shop():
    def __init__(self, player, WIDTH, HEIGHT):
        # loads info about the width and height for use in placing sprites
        self.scale_factor = HEIGHT / 600
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        # loads the player and its class to change the players stats along with what upgrades are available
        self.player = player
        self.chosen_class = player.chosen_class

        # loads and scales all of the needed sprites
        damage_upgrade_image = pygame.image.load('sprites\\damage icon.png')
        self.damage_upgrade_image = pygame.transform.scale_by(damage_upgrade_image, self.scale_factor*8)
        life_upgrade_image = pygame.image.load('sprites\\life icon.png')
        self.life_upgrade_image = pygame.transform.scale_by(life_upgrade_image, self.scale_factor*8)
        health_image = pygame.image.load('sprites\\health icon.png')
        self.health_image = pygame.transform.scale_by(health_image, self.scale_factor*8)

        # uses the sprite size to create on offset for placing images
        self.height_offset = self.life_upgrade_image.get_rect()[3]
        self.horizontal_offset = self.life_upgrade_image.get_rect()[2]/2

    # the main function that is called to use the shop
    def display_shop(self, screen):
        # checks whether health should be regened or max hp and updating the text displayed
        if self.player.hp <= self.player.max_hp-2: 
            health_upgrade_text = ['Upgrade Your Health', 'regens lost hp']
            regen = True
        else: 
            health_upgrade_text = ['Upgrade Your Health', 'increases max hp']
            regen = False

        # checks the form of damage upgrade based on class and current stats
        if self.player.chosen_class == 'ranger':
            if self.player.pierce <= self.player.damage:
                damage_upgrade_text = ['Upgrade Your Attack', 'increases pierce']
                ranger_pierce = True
            else:
                damage_upgrade_text = ['Upgrade Your Attack', 'increases damage']
                ranger_pierce =  False
        else:
            damage_upgrade_text = ['Upgrade Your Attack', 'increases swing speed']

        # checks the dodge chance so a player can't be invincible, if to high this becomes a health upgrade
        if self.player.dodge_chance < 70:
            dodge = True
            defence_upgrade_text = ['Upgrade Your Defence', 'increases dodge chance']
        else:
            dodge = False
            defence_upgrade_text = ['Upgrade Your Defence', 'dodge chance is higher than 70%', 'gives health upgrade']

        # reset the screen by filling it with a color
        screen.fill((139,69,19))

        # draws all pictures and text boxes to the screen
        screen.blit(self.life_upgrade_image, (self.WIDTH/2-3*self.horizontal_offset, self.HEIGHT/2-self.height_offset*17/30))
        make_text_box(screen, self.scale_factor, (self.WIDTH/3*2+self.horizontal_offset*31/32, self.HEIGHT/2+self.height_offset*2/3), health_upgrade_text)
        screen.blit(self.health_image, (self.WIDTH/2+self.horizontal_offset, self.HEIGHT/2-self.height_offset*17/30))
        make_text_box(screen, self.scale_factor, (self.WIDTH/3-self.horizontal_offset*15/16, self.HEIGHT/2+self.height_offset*2/3), defence_upgrade_text)
        screen.blit(self.damage_upgrade_image, (self.WIDTH/2-self.horizontal_offset, self.HEIGHT/2-self.height_offset*17/30))
        make_text_box(screen, self.scale_factor, (self.WIDTH/2, self.HEIGHT/2+self.height_offset*2/3), damage_upgrade_text)
        make_text_box(screen, self.scale_factor*3, (self.WIDTH/2, self.height_offset/10), ['Upgrade Time'])
        
        # updates the screen so the user can see the changes
        pygame.display.flip()
        
        # this is the main loop for checking if the user has made a choice
        waiting = True
        while waiting:
            for event in pygame.event.get():
                # if the user clicks the x the shop returns false to tell the game to stop
                if event.type == pygame.QUIT: 
                    return False
                if event.type == pygame.KEYDOWN:
                    # if escape is pressed the shop returns false to tell the game to stop
                    if event.key == pygame.K_ESCAPE:
                        return False
                # if there is a mouse click the game checks the position to determine the clicked upgrade
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                    # all upgrades return true to tell the game to continue
                    if x > self.WIDTH/3*2:
                        # health upgrade, right side
                        if regen == True: 
                            self.player.hp += 2
                        else:
                            self.player.max_hp += 1
                            self.player.hp = self.player.max_hp
                        return True
                    elif x > self.WIDTH/3:
                        # attack upgrade, middle
                        try:
                            if ranger_pierce == True:
                                self.player.pierce += 1
                            else:
                                self.player.damage += 1
                        except:
                            self.player.slash_speed += .05
                        return True
                    else:
                        # defence upgrade, left side
                        if dodge == True:
                            self.player.dodge_chance += 10
                        else:
                            if self.player.hp <= self.player.max_hp-2:
                                self.player.hp += 2
                            else:
                                self.player.max_hp += 1
                                self.player.hp = self.player.max_hp
                        return True