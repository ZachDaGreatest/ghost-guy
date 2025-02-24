from math import sin,cos,atan,pi
from random import randint
from map import collision_check
import pygame

class handeler():
    def __init__(self,map_size):
        spooky_ghost_image = pygame.image.load('sprites\\spooky ghost.png')
        spooky_ghost_image = pygame.transform.scale_by(spooky_ghost_image,(map_size/16))
        sprinter_ghost_image = pygame.image.load('sprites\\sprinting ghost.png')
        sprinter_ghost_image = pygame.transform.scale_by(sprinter_ghost_image,(map_size/16))
        mage_ghost_image = pygame.image.load('sprites\\mage ghost.png')
        mage_ghost_image = pygame.transform.scale_by(mage_ghost_image,(map_size/16))
        self.positions = []
        self.enemie_num = 0
        self.bullet_speed = .1
        self.ghost_bullets = []

        #TODO add a spawn frame count at the end so you can play a spawning animation
        self.type_info = {
            'basic' : (.05, spooky_ghost_image, 1),
            'sprinter' : (.1, sprinter_ghost_image, 1),
            'mage' : (.005, mage_ghost_image, 1),
            'place holder' : (0, spooky_ghost_image, 1)   #place holder is for testing
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
        pos_storage = self.positions
        self.positions = []
        for enemy in pos_storage:
            x = enemy[0] - player_pos[0]
            y = enemy[1] - player_pos[1]
            ghost_type = enemy[2]
            angle = atan(y/x)
            speed = self.type_info[enemy[2]][0]
            xspeed = cos(angle)*dt*speed
            yspeed = sin(angle)*dt*speed
            if x>0:
                xspeed = -xspeed
                yspeed = -yspeed
                angle += (pi)
            self.positions.append((enemy[0] + xspeed, enemy[1] + yspeed, ghost_type))
            if enemy[2] == 'mage':
                num = int(120 * dt)
                if randint(0,num) >= num:
                    self.shoot(angle, enemy[0], enemy[1])
    def spawn_enemy_random(self, player_pos, map_size, current_level):
        looking = True
        while looking:
            x = randint(2,map_size[0])
            y = randint(2,map_size[1])
            x_diff = x-player_pos[0]
            y_diff = y-player_pos[1]
            if (x_diff > 2 or x_diff < -2) or (y_diff > 2 or y_diff < -2):
                looking = False
        ghost_type = 'basic'
        if randint(0,10) > (10 - current_level):
            ghost_type = 'sprinter'
        elif randint(0,10) > (11 - current_level):
            ghost_type = 'mage'
        self.enemie_num += 1
        self.positions.append((x,y,ghost_type))
    def level_check(self, elim_list, frame_count, current_level, player):
        if self.elim_count >= elim_list[current_level]:
            current_level += 1
            self.positions = []
            self.ghost_bullets = []
            player.bullets = []
            self.enemie_num = 0
            frame_count = 0
            player.set_walls(current_level)
            player.pos = (2,2)
            if player.hp < player.max_hp: player.hp += 1
            else: self.elim_count += 10
        return current_level, frame_count
    def shoot(self, angle, x, y):
        self.ghost_bullets.append((x,y,angle))
    def move_bullets(self, player, wall_pos, hit, dt):
        temp = self.ghost_bullets
        self.ghost_bullets = []
        for bullet in temp:
            x_speed = cos(bullet[2]) * dt * self.bullet_speed
            y_speed = sin(bullet[2]) * dt * self.bullet_speed
            x_wall, y_wall = collision_check(wall_pos,.5,x_speed,y_speed,(bullet[0],bullet[1]))
            x_player, y_player = collision_check([player.pos],1,x_speed,y_speed,(bullet[0],bullet[1]))
            if x_wall and y_wall == True:
                pass
            elif x_player and y_player == True:
                if hit <= 0:
                    player.hp -= 1
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