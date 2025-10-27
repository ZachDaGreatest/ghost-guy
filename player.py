from math import sin,cos,sqrt,pi
from map import collision_check, find_num_matrix
from random import randint

class player():
    def __init__(self,pos,chosen_class,current_level,mode):
        self.room_walls = []
        find_num_matrix(1,self.room_walls,current_level,mode)
        self.pos = pos
        self.direction = -pi/2
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 0
        self.bullets = []
        self.bullet_speed = .2
        # make 1.0 for bayblade
        self.slash_speed = .075
        self.chosen_class = chosen_class
        # class name : [weapon name, starting hp, max hp, speed]
        # TODO change to dictionary of dictionaries
        self.classes = {
            'ranger' : {'weapon' : 'dagger', 
                        'hp' : 3, 
                        'max hp' : 5, 
                        'acceleration' : .005,
                        'dodge chance' : 0},
            'knight' : {'weapon' : 'sword',
                        'hp' : 5,
                        'max hp' : 8,
                        'acceleration' : .0075,
                        'dodge chance' : 5}
        }
        self.weapon = self.classes[chosen_class]['weapon']
        self.hp = self.classes[chosen_class]['hp']
        self.max_hp = self.classes[chosen_class]['max hp']
        self.acceleration = self.classes[chosen_class]['acceleration']
        # dodge_chance is a percent out of 100 that can be upgraded in the shop
        self.dodge_chance = self.classes[chosen_class]['dodge chance']
        # pierce is the number of enemies a bullet can travel through and can be upgraded in the shop
        if chosen_class == 'ranger':
            self.pierce = 1
    def set_dt(self,dt):
        self.dt = dt

    def set_walls(self,current_level,mode):
        self.room_walls = []
        find_num_matrix(1,self.room_walls,current_level,mode)

    def move_forward(self):
        self.speed += self.acceleration
        self.y_speed -= self.speed * self.dt
    def move_backward(self):
        self.speed += self.acceleration
        self.y_speed += self.speed * self.dt
    def move_right(self):
        self.speed += self.acceleration
        self.x_speed += self.speed * self.dt
    def move_left(self):
        self.speed += self.acceleration
        self.x_speed -= self.speed * self.dt
    def turn_right(self):
        self.direction += .1 * self.dt
        if self.chosen_class == 'knight':
            self.direction += self.slash_speed * self.dt
    def turn_left(self):
        self.direction -= .1 * self.dt
        if self.chosen_class == 'knight':
            self.direction -= self.slash_speed * self.dt
    def pos_update(self):
        self.pos = (self.pos[0] + self.x_speed, self.pos[1] + self.y_speed)
        self.x_speed = 0
        self.y_speed = 0
    def stop(self):
        self.speed = 0
    
    def check(self,forward,backward,right,left,wall_hitbox,enemy_handeler,hit):
        input_num = 0
        if forward == True and backward == True:
            forward = False
            backward = False
            self.y_speed = 0
        if right == True and left == True:
            right = False
            left = False
            self.x_speed = 0
        if forward == True: input_num += 1
        if backward == True: input_num += 1
        if left == True: input_num += 1
        if right == True: input_num += 1
        if input_num > 0:
            self.x_speed = self.x_speed/sqrt(input_num)
            self.y_speed = self.y_speed/sqrt(input_num)
        else:
            self.speed = 0
        if self.speed > .1:
            self.speed = .1
        x_wall,y_wall = collision_check(self.room_walls,wall_hitbox,self.x_speed,self.y_speed,self.pos)
        if x_wall == True:
            self.x_speed = 0
        if y_wall == True:
            self.y_speed = 0
        if hit <= 0:
            ghost_positions = []
            for ghost in enemy_handeler.ghosts:
                ghost_positions.append(ghost.pos)
            x_enemy,y_enemy = collision_check(ghost_positions,wall_hitbox,self.x_speed,self.y_speed,self.pos)
            if x_enemy == True and y_enemy == True:
                enemy_handeler.destroy_enemy((self.pos[0], self.pos[1]))
                self.hit()
                if self.hp <= 0:
                    return False
        return True
    
    def shoot(self):
        self.bullets.append((self.pos[0] + cos(self.direction), self.pos[1] + sin(self.direction), self.direction, self.pierce))

    def bullet_move(self, enemy_handeler):
        #TODO make movement uniform like the ghosts
        temp_list = self.bullets
        self.bullets = []
        for bullet in temp_list:
            x_speed = cos(bullet[2]) * self.dt * self.bullet_speed
            y_speed = sin(bullet[2]) * self.dt * self.bullet_speed
            pierce = bullet[3]
            x_wall, y_wall = collision_check(self.room_walls,.5,x_speed,y_speed,(bullet[0],bullet[1]))
            ghost_positions = []
            for ghost in enemy_handeler.ghosts:
                ghost_positions.append(ghost.pos)
            x_enemy, y_enemy = collision_check(ghost_positions,.65,x_speed,y_speed,(bullet[0],bullet[1]))
            if x_wall and y_wall == True:
                pass
            elif x_enemy and y_enemy == True:
                enemy_handeler.destroy_enemy((bullet[0],bullet[1]))
                pierce -= 1
                if pierce > 0:
                    self.bullets.append((bullet[0] + x_speed, bullet[1] + y_speed, bullet[2], pierce))
            else:
                self.bullets.append((bullet[0] + x_speed, bullet[1] + y_speed, bullet[2], pierce))
    
    def sword_swing(self, enemy_handeler):
        self.bullets = []
        x = self.pos[0] + cos(self.direction) * 1.1
        y = self.pos[1] + sin(self.direction) * 1.1
        x_wall, y_wall = collision_check(self.room_walls,.4,0,0,(x,y))
        if x_wall == False or y_wall == False:
            self.bullets.append((x, y, self.direction))
            ghost_positions = []
            for ghost in enemy_handeler.ghosts:
                ghost_positions.append(ghost.pos)
            x_enemy, y_enemy = collision_check(ghost_positions,.75,0,0,(x,y))
            if x_enemy and y_enemy == True:
                enemy_handeler.destroy_enemy((x,y))

    def hit(self):
        if randint(0,100) > self.dodge_chance:
            self.hp -= 1