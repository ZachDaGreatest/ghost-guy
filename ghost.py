from math import sin, cos, atan, pi
from random import randint

class ghost():
    def __init__(self, type_info, type, pos):
        self.speed = type_info[type]['speed']
        self.image = type_info[type]['image']
        self.health = type_info[type]['health']
        self.type = type
        self.pos = pos
        if self.type == 'mage':
            self.attack_cooldown = 120

    def frame_check(self, target_pos, dt, handler):
        x = self.pos[0] - target_pos[0]
        y = self.pos[1] - target_pos[1]
        try: angle = atan(y/x)
        except: angle = 0
        xspeed = cos(angle)*dt*self.speed
        yspeed = sin(angle)*dt*self.speed
        if x>0:
            xspeed = -xspeed
            yspeed = -yspeed
            angle += (pi)
        self.pos = (self.pos[0] + xspeed, self.pos[1] + yspeed)
        if self.type == 'mage':
            self.attack_cooldown -= 1
            if self.attack_cooldown <= 0:
                handler.shoot(angle, self.pos[0], self.pos[1])
                self.attack_cooldown = 120*dt