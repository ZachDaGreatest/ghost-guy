from math import sin,cos,atan,degrees
from random import randint
import pygame

class handeler():
    def __init__(self,map_size):
        spooky_ghost_image = pygame.image.load('sprites\spooky ghost.png')
        spooky_ghost_image = pygame.transform.scale_by(spooky_ghost_image,(map_size/16))
        sprinter_ghost_image = pygame.image.load('sprites\sprinting ghost.png')
        sprinter_ghost_image = pygame.transform.scale_by(sprinter_ghost_image,(map_size/16))
        self.positions = []
        self.enemie_num = 0
        self.type_info = {
            'basic' : (.05, spooky_ghost_image, 1),
            'sprinter' : (.1, sprinter_ghost_image, 1)
        }
        self.elim_count = 0
        self.speed = .05
    def destroy_enemy(self, enemy_pos):
        proximity_list = []
        for pos in self.positions:
            proximity_list.append(abs(pos[0] - enemy_pos[0]) + abs(pos[1] - enemy_pos[1]))
        closest_location = min(proximity_list)
        self.positions.pop(proximity_list.index(closest_location))
        self.enemie_num -= 1
        self.elim_count += 1
    def enemy_check(self,player_pos,dt):
        for enemy in self.positions:
            x = enemy[0] - player_pos[0]
            y = enemy[1] - player_pos[1]
            ghost_type = enemy[2]
            angle = atan(y/x)
            speed = self.type_info[enemy[2]][0]
            self.positions.remove(enemy)
            if x<0:
                self.positions.append((enemy[0]+cos(angle)*dt*speed,enemy[1]+sin(angle)*dt*speed, ghost_type))
            if x>0:
                self.positions.append((enemy[0]-cos(angle)*dt*speed,enemy[1]-sin(angle)*dt*speed, ghost_type))
    def spawn_enemy_random(self, player_pos, map_size, current_level):
        looking = True
        while looking:
            x = randint(2,map_size[0])
            y = randint(2,map_size[1])
            x_diff = x-player_pos[0]
            y_diff = y-player_pos[1]
            if (x_diff > 2 or x_diff < -2) and (y_diff > 2 or y_diff < -2):
                looking = False
        ghost_type = 'basic'
        if randint(0,10) > (10 - current_level):
            ghost_type = 'sprinter'
        self.enemie_num += 1
        self.positions.append((x,y,ghost_type))
    def level_check(self, elim_list, frame_count, current_level, player):
        if self.elim_count >= elim_list[current_level]:
            current_level += 1
            self.positions = []
            self.enemie_num = 0
            frame_count = 0
            player.set_walls(current_level)
            player.pos = (2,2)
            if player.hp < 5: player.hp += 1
        return current_level, frame_count
    

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image