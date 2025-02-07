from math import sin,cos,sqrt,pi
from map import collision_check, find_num_matrix

class player():
    def __init__(self,pos,acceleration,current_level):
        self.room_walls = []
        find_num_matrix(1,self.room_walls,current_level)
        self.pos = pos
        self.direction = -pi/2
        self.x_speed = 0
        self.y_speed = 0
        self.acceleration = acceleration
        self.speed = 0
        self.bullets = []
        self.bullet_speed = .4
        self.hp = 3

    def set_dt(self,dt):
        self.dt = dt

    def set_walls(self,current_level):
        self.room_walls = []
        find_num_matrix(1,self.room_walls,current_level)

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
    def turn_left(self):
        self.direction -= .1 * self.dt
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
            x_enemy,y_enemy = collision_check(enemy_handeler.positions,wall_hitbox,self.x_speed,self.y_speed,self.pos)
            if x_enemy == True and y_enemy == True:
                enemy_handeler.destroy_enemy((self.pos[0], self.pos[1]))
                self.hp -= 1
                if self.hp <= 0:
                    return False
        return True
    
    def shoot(self):
        self.bullets.append((self.pos[0] + cos(self.direction), self.pos[1] + sin(self.direction), self.direction))

    def bullet_move(self,enemies):
        for bullet in self.bullets:
            x_speed = cos(bullet[2]) * self.dt * self.bullet_speed
            y_speed = sin(bullet[2]) * self.dt * self.bullet_speed
            x_wall, y_wall = collision_check(self.room_walls,.5,x_speed,y_speed,(bullet[0],bullet[1]))
            x_enemy, y_enemy = collision_check(enemies.positions,1,x_speed,y_speed,(bullet[0],bullet[1]))
            if x_wall and y_wall == True:
                self.bullets.remove(bullet)
            elif x_enemy and y_enemy == True:
                enemies.destroy_enemy((bullet[0],bullet[1]))
                self.bullets.remove(bullet)
            else:
                self.bullets.remove(bullet)
                self.bullets.append((bullet[0] + x_speed, bullet[1] + y_speed, bullet[2]))