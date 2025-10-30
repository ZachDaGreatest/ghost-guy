from math import sin,cos,atan,pi
from random import randint
from map import collision_check
from ghost import ghost
import pygame

class handler():
    def __init__(self,map_size):
        spooky_ghost_image = pygame.image.load('sprites\\spooky ghost.png')
        spooky_ghost_image = pygame.transform.scale_by(spooky_ghost_image,(map_size/16))
        sprinter_ghost_image = pygame.image.load('sprites\\sprinting ghost.png')
        sprinter_ghost_image = pygame.transform.scale_by(sprinter_ghost_image,(map_size/16))
        mage_ghost_image = pygame.image.load('sprites\\mage ghost.png')
        mage_ghost_image = pygame.transform.scale_by(mage_ghost_image,(map_size/16))
        bruiser_ghost_image = pygame.image.load('sprites\\bruiser ghost.png')
        bruiser_ghost_image = pygame.transform.scale_by(bruiser_ghost_image,(map_size/16))
        self.ghosts = []
        self.enemie_num = 0
        self.bullet_speed = .1
        self.ghost_bullets = []

        #TODO add a spawn frame count at the end so you can play a spawning animation
        self.type_info = {
            'basic' : {'speed' : .05, 
                        'image' : spooky_ghost_image,
                        'health' : 1},
            'sprinter' : {'speed' : .1, 
                        'image' : sprinter_ghost_image,
                        'health' : 1},
            'mage' : {'speed' : .005, 
                        'image' : mage_ghost_image,
                        'health' : 1},
            'bruiser' : {'speed' : .025, 
                        'image' : bruiser_ghost_image,
                        'health' : 2},
            'place holder' : {'speed' : 0, 
                        'image' : spooky_ghost_image,
                        'health' : 1}   #place holder is for testing
        }
        self.elim_count = 0
        self.speed = .05

    def damage_enemy(self, enemy_pos, damage, id_number):
        proximity_list = []
        for ghost in self.ghosts:
            proximity_list.append(abs(ghost.pos[0] - enemy_pos[0]) + abs(ghost.pos[1] - enemy_pos[1]))
        closest_location = min(proximity_list)
        is_alive = self.ghosts[proximity_list.index(closest_location)].damage(damage, id_number)
        if is_alive == True:
            pass
        else:
            self.enemie_num -= 1
            self.elim_count += 1
            self.ghosts.pop(proximity_list.index(closest_location))

    def enemy_check(self, player_pos, dt):
        for ghost in self.ghosts:
            ghost.frame_check(player_pos, dt, self)

    def spawn_enemy_random(self, player_pos, map_size, current_level):
        looking = True
        while looking:
            x = randint(2,map_size[0])
            y = randint(2,map_size[1])
            x_diff = x-player_pos[0]
            y_diff = y-player_pos[1]
            if (x_diff > 3 or x_diff < -3) or (y_diff > 3 or y_diff < -3):
                looking = False
        ghost_type = 'basic'
        if randint(0,10) > (10 - current_level):
            ghost_type = 'sprinter'
        elif randint(0,10) > (11 - current_level):
            ghost_type = 'mage'
        if ghost_type == 'basic' and randint(0, current_level+1) > 2:
            ghost_type = 'bruiser'
        self.enemie_num += 1
        self.ghosts.append(ghost(self.type_info, ghost_type, (x,y)))

    def level_check(self, elim_list, frame_count, current_level, player, mode):
        is_new_level = False
        if self.elim_count >= elim_list[current_level]:
            is_new_level = True
            current_level += 1
            self.ghosts = []
            self.ghost_bullets = []
            player.bullets = []
            self.enemie_num = 0
            frame_count = 0
            player.set_walls(current_level, mode)
            player.pos = (2,2)
        return current_level, frame_count, is_new_level
    
    def shoot(self, angle, x, y):
        self.ghost_bullets.append((x,y,angle))

    def move_bullets(self, player, wall_pos, hit, dt):
        temp = self.ghost_bullets
        self.ghost_bullets = []
        for bullet in temp:
            x_speed = cos(bullet[2]) * self.bullet_speed * dt
            y_speed = sin(bullet[2]) * self.bullet_speed * dt
            x_wall, y_wall = collision_check(wall_pos,.5,x_speed,y_speed,(bullet[0],bullet[1]))
            x_player, y_player = collision_check([player.pos],1,x_speed,y_speed,(bullet[0],bullet[1]))
            if x_wall and y_wall == True:
                pass
            elif x_player and y_player == True:
                if hit <= 0:
                    player.hit()
            else:
                self.ghost_bullets.append((bullet[0] + x_speed, bullet[1] + y_speed, bullet[2]))

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image