#this is a test for AP test constraints
from random import randint
from math import cos,sin,degrees,atan,sqrt,pi
import pygame

level_1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

level_2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, randint(0,1), randint(0,1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, randint(0,1), randint(0,1), 0, 1],
    [1, 0, randint(0,1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, randint(0,1), 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, randint(0,1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, randint(0,1), 0, 1],
    [1, 0, randint(0,1), randint(0,1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, randint(0,1), randint(0,1), 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

level_3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, randint(0,1), randint(0,1), 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, randint(0,1), 0, 0, 0, 0, 0, randint(0,1), randint(0,1), 0, 0, 0, 0, 0, randint(0,1), 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, randint(0,1), randint(0,1), 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

level_4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

level_5 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#18x13 walls
#16x11 spawnable

elim_goals = [10, 30, 70, 150, 310, 670, 1390, 2830]
maps = [level_1,level_2,level_3,level_4,level_5,level_5,level_5,level_5]

def find_num_matrix(desired_num, end_list, current_level):
    y = 0
    for row in (maps[current_level]):
        x = 0
        y += 1
        for collum in row:
            x += 1
            if collum == desired_num:
                end_list.append((x,y))

def collision_check(object_list,hitbox,x_speed,y_speed,location):
    x_hit = False
    y_hit = False
    for pos in object_list:
        if (pos[0] - hitbox < location[0] + x_speed < pos[0] + hitbox) and (pos[1] - hitbox < location[1] < pos[1] + hitbox):
            x_hit = True
        if (pos[0] - hitbox < location[0] < pos[0] + hitbox) and (pos[1] - hitbox < location[1] + y_speed < pos[1] + hitbox):
            y_hit = True
    return x_hit,y_hit

class handeler():
    def __init__(self,map_size):
        spooky_ghost_image = pygame.image.load('sprites\\spooky ghost.png')
        spooky_ghost_image = pygame.transform.scale_by(spooky_ghost_image,(map_size/16))
        sprinter_ghost_image = pygame.image.load('sprites\\sprinting ghost.png')
        sprinter_ghost_image = pygame.transform.scale_by(sprinter_ghost_image,(map_size/16))
        self.positions = []
        self.enemie_num = 0
        self.type_info = {
            'basic' : (.05, spooky_ghost_image, 1),
            'sprinter' : (.1, sprinter_ghost_image, 1),
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
            self.positions.append((enemy[0] + xspeed, enemy[1] + yspeed, ghost_type))
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
            else: self.elim_count += 10
        return current_level, frame_count
    
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

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

def game_loop(screen, HEIGHT, WIDTH):
    tick_rate = 60
    spawn_frame_count = 0
    hit_frames = 0
    frame_count = 0
    current_level = 0
    turn_left = False
    turn_right = False
    forward = False
    backward = False
    right = False
    left = False
    running = True
    
    floors = []
    find_num_matrix(0, floors, 5)
    player_acceleration = .005
    wall_hitbox = .93
    map_size = WIDTH/20
    font = pygame.font.SysFont('Pixeloid Sans', int(map_size/1.2))
    guy = player((2,2),player_acceleration,0)
    enemy_handeler = handeler(map_size)
    try: guy.set_dt(dt)
    except: guy.set_dt(1)

    floor_image = pygame.image.load('sprites\\floor.png')
    floor_image = pygame.transform.scale_by(floor_image,(map_size/16))
    wall_image = pygame.image.load('sprites\\wall.png')
    wall_image = pygame.transform.scale_by(wall_image,(map_size/16))
    guy_image = pygame.image.load('sprites\\guy.png')
    guy_image = pygame.transform.scale_by(guy_image,(map_size/16))
    heart_image = pygame.image.load('sprites\\heart.png')
    heart_image = pygame.transform.scale_by(heart_image,(map_size/7))

    game_clock = pygame.time.Clock()

    while running:
        frame_count += 1
        spawn_frame_count += 1
        
        # print(game_clock.get_fps()) #debugging ghost movement

        if tick_rate != 60:
            try: dt = 60/float(game_clock.get_fps())
            except: dt = 1
        else: dt = 1
        guy.set_dt(dt)

        if  enemy_handeler.enemie_num < (current_level + 3):
            if spawn_frame_count*dt > 12000/(frame_count*dt):
                enemy_handeler.spawn_enemy_random(guy.pos,(16,11),current_level)
                spawn_frame_count = 0
        #Draw background
        if hit_frames > 0:
            screen.fill((255,0,0))
            hit_frames -= 1
        else:
            screen.fill((0,0,0))
        

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
                if event.key == pygame.K_w: forward = True
                if event.key == pygame.K_a: left = True
                if event.key == pygame.K_s: backward = True
                if event.key == pygame.K_d: right = True
                if event.key == pygame.K_RIGHT: turn_right = True
                if event.key == pygame.K_LEFT: turn_left = True
                if event.key == pygame.K_UP: guy.shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: forward = False
                if event.key == pygame.K_a: left = False
                if event.key == pygame.K_s: backward = False
                if event.key == pygame.K_d: right = False
                if event.key == pygame.K_RIGHT: turn_right = False
                if event.key == pygame.K_LEFT: turn_left = False
        
        if forward == True: guy.move_forward()
        if backward == True: guy.move_backward()
        if right == True: guy.move_right()
        if left == True: guy.move_left()
        if turn_right == True:
            guy.turn_right()
        if turn_left == True: 
            guy.turn_left()
        
        prev_hp = guy.hp
        status = guy.check(forward,backward,right,left,wall_hitbox,enemy_handeler,hit_frames)
        if status == False: running = False
        guy.bullet_move(enemy_handeler)
        
        guy.pos_update()

        enemy_handeler.enemy_check(guy.pos,dt)

        run_info = font.render(('level ' + str(current_level+1) + ' with ' + str(enemy_handeler.elim_count) + ' eliminations'), False, (169, 169, 169))
        screen.blit(run_info, (WIDTH-run_info.get_rect()[2]-map_size,0))

        for pos in floors:
            screen.blit(floor_image, (pos[0]*map_size, pos[1]*map_size))
        for pos in guy.room_walls:
            # pygame.draw.rect(screen, (255,255,255), (pos[0]*map_size, pos[1]*map_size, map_size, map_size))
            screen.blit(wall_image, (pos[0]*map_size, pos[1]*map_size))

        for enemy in enemy_handeler.positions:
            # pygame.draw.rect(screen, (255,0,0), (pos[0]*map_size, pos[1]*map_size, map_size, map_size))
            screen.blit(enemy_handeler.type_info[enemy[2]][1], (enemy[0]*map_size, enemy[1]*map_size))
        
        for bullet in guy.bullets:
            pygame.draw.rect(screen, (192,192,192), (bullet[0]*map_size+(3/8)*map_size, bullet[1]*map_size+(3/8)*map_size, map_size/4, map_size/4))

        # pygame.draw.rect(screen, (0,255,0), (guy.pos[0]*map_size + cos(guy.direction)*map_size/2 + map_size*(3/8), guy.pos[1]*map_size + sin(guy.direction)*map_size/2 + map_size*(3/8), map_size/4, map_size/4))
        screen.blit(guy_image, (guy.pos[0]*map_size, guy.pos[1]*map_size))

        dagger_image = pygame.image.load('sprites\\dagger.png')
        dagger_image = pygame.transform.scale_by(dagger_image,(map_size/16))
        dagger_image = rot_center(dagger_image, -degrees(guy.direction+pi/2))
        screen.blit(dagger_image, (guy.pos[0]*map_size + map_size*(1/4) + cos(guy.direction)*map_size/1.2, guy.pos[1]*map_size + map_size*(1/4) + sin(guy.direction)*map_size/1.2))
        
        for num in range(guy.hp):
            screen.blit(heart_image, (num*map_size + map_size, 0))

        if prev_hp > guy.hp:
            hit_frames += 12*dt

        pygame.display.update((0,0,WIDTH,HEIGHT))
        game_clock.tick(tick_rate)

        current_level, frame_count = enemy_handeler.level_check(elim_goals, frame_count, current_level, guy)

    return str(enemy_handeler.elim_count), str(current_level + 1)

def menu(screen, elim_count, level, HEIGHT, WIDTH):
    screen.fill((0,0,0))

    scale_factor = HEIGHT / 600

    logo = pygame.image.load('sprites\\ghost guy logo.png')
    logo = pygame.transform.scale_by(logo,(10*scale_factor))
    start_button = pygame.image.load('sprites\\start button.png')
    start_button = pygame.transform.scale_by(start_button,(5*scale_factor))
    trophy_image = pygame.image.load('sprites\\trophy.png')
    trophy_image = pygame.transform.scale_by(trophy_image,(5*scale_factor))

    screen.blit(logo, ((WIDTH-logo.get_rect()[2])/2,155*scale_factor))
    screen.blit(start_button, ((WIDTH-start_button.get_rect()[2])/2,370*scale_factor))

    #TODO add text of how you did in the previous run
    if level == 0:
        message = 'Click start or press space to begin!'
    else:
        message = 'you eliminated ' + elim_count + ' spooky ghosts reaching level ' + level
    pygame.font.init()
    font = pygame.font.SysFont('Pixeloid Sans', int(27*scale_factor))
    run_info = font.render(message, False, (169, 169, 169))
    screen.blit(run_info, ((WIDTH-run_info.get_rect()[2])/2,440*scale_factor))
    if int(level) >= 5:
        screen.blit(trophy_image, ((WIDTH-trophy_image.get_rect()[2])/2,480*scale_factor))


    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False,  False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if 312.5*scale_factor < x < 487.5*scale_factor and 370*scale_factor < y < 425*scale_factor:
                    return True, True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: return False,  False
                if event.key == pygame.K_SPACE: return True,  True

HEIGHT = 720    #factors of 240 work best
WIDTH = int(HEIGHT*(4/3))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ghost guy")
elim_count = 0
level = 0

# pygame.display.toggle_fullscreen()

gaming = True
while gaming:
    play, gaming = menu(screen, elim_count, level, HEIGHT, WIDTH)
    if play: elim_count, level = game_loop(screen, HEIGHT, WIDTH)