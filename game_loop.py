import pygame
from player import player
from math import cos,sin,degrees,atan,pi
from handelers import handeler, rot_center
from map import elim_goals, find_num_matrix

pygame.init()

def game_loop(screen, HEIGHT, WIDTH, chosen_class, input_method):
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
    
    guy = player((2,2),chosen_class,current_level)

    floors = []
    find_num_matrix(0, floors, 5)
    wall_hitbox = .93
    map_size = WIDTH/20
    font = pygame.font.Font('fonts\\PixeloidSans.ttf', int(27*(HEIGHT/600)))
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
            if spawn_frame_count*dt > 12000/(frame_count*dt) and (elim_goals[current_level]-enemy_handeler.elim_count) > enemy_handeler.enemie_num:
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
                if input_method == 'keyboard':
                    if event.key == pygame.K_RIGHT: turn_right = True
                    if event.key == pygame.K_LEFT: turn_left = True
                    if event.key == pygame.K_UP: 
                        if guy.chosen_class == 'ranger':
                            guy.shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: forward = False
                if event.key == pygame.K_a: left = False
                if event.key == pygame.K_s: backward = False
                if event.key == pygame.K_d: right = False
                if input_method == 'keyboard':
                    if event.key == pygame.K_RIGHT: turn_right = False
                    if event.key == pygame.K_LEFT: turn_left = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if guy.chosen_class == 'ranger' and input_method == 'mouse':
                    guy.shoot()
        
        if forward == True: guy.move_forward()
        if backward == True: guy.move_backward()
        if right == True: guy.move_right()
        if left == True: guy.move_left()
        if input_method == 'keyboard':
            if turn_right == True: guy.turn_right()
            if turn_left == True: guy.turn_left()
        
        if input_method == 'mouse':
            mouse_x = pygame.mouse.get_pos()[0]/map_size
            mouse_y = pygame.mouse.get_pos()[1]/map_size
            guy_x = guy.pos[0] + .5
            guy_y = guy.pos[1] + .5
            if mouse_x - guy_x < 0:
                guy.direction = atan((mouse_y-guy_y)/(mouse_x-guy_x)) - pi
            else:
                guy.direction = atan((mouse_y-guy_y)/(mouse_x-guy_x))

        prev_hp = guy.hp
        status = guy.check(forward,backward,right,left,wall_hitbox,enemy_handeler,hit_frames)
        if guy.hp < 1:
            status = False
        if status == False: running = False

        if guy.chosen_class == 'ranger': 
            guy.bullet_move(enemy_handeler)
        if guy.chosen_class == 'knight': 
            guy.sword_swing(enemy_handeler)
        
        guy.pos_update()
        enemy_handeler.enemy_check(guy.pos,dt)
        enemy_handeler.move_bullets(guy, guy.room_walls, hit_frames, dt)

        #choose between run info and elim info with level info
        # run_info = font.render((f'level {current_level+1} with {enemy_handeler.elim_count} eliminations'), False, (169, 169, 169))
        # screen.blit(run_info, (WIDTH-run_info.get_rect()[2]-map_size, map_size*.1))
        elim_info = font.render((f'{elim_goals[current_level]-enemy_handeler.elim_count} ghosts remain'), False, (255, 0, 0))
        level_info = font.render((f'level {current_level+1}'), False, (169, 169, 169))
        screen.blit(elim_info, (WIDTH-elim_info.get_rect()[2]-map_size, map_size*.1))
        screen.blit(level_info, ((WIDTH-level_info.get_rect()[2])/2, map_size*.1))

        for pos in floors:
            screen.blit(floor_image, (pos[0]*map_size, pos[1]*map_size))
        for pos in guy.room_walls:
            # pygame.draw.rect(screen, (255,255,255), (pos[0]*map_size, pos[1]*map_size, map_size, map_size))
            screen.blit(wall_image, (pos[0]*map_size, pos[1]*map_size))

        for enemy in enemy_handeler.positions:
            # pygame.draw.rect(screen, (255,0,0), (pos[0]*map_size, pos[1]*map_size, map_size, map_size))
            screen.blit(enemy_handeler.type_info[enemy[2]][1], (enemy[0]*map_size, enemy[1]*map_size))
        
        for bullet in guy.bullets:
            if guy.chosen_class != 'knight':
                pygame.draw.rect(screen, (192,192,192), (bullet[0]*map_size+(3/8)*map_size, bullet[1]*map_size+(3/8)*map_size, map_size/4, map_size/4))

        for bullet in enemy_handeler.ghost_bullets:
            pygame.draw.rect(screen, (255,0,255), (bullet[0]*map_size+(3/8)*map_size, bullet[1]*map_size+(3/8)*map_size, map_size/4, map_size/4))

        # pygame.draw.rect(screen, (0,255,0), (guy.pos[0]*map_size + cos(guy.direction)*map_size/2 + map_size*(3/8), guy.pos[1]*map_size + sin(guy.direction)*map_size/2 + map_size*(3/8), map_size/4, map_size/4))
        screen.blit(guy_image, (guy.pos[0]*map_size, guy.pos[1]*map_size))

        dagger_image = pygame.image.load('sprites\\dagger.png')
        dagger_image = pygame.transform.scale_by(dagger_image,(map_size/16))
        dagger_image = rot_center(dagger_image, -degrees(guy.direction+pi/2))
        screen.blit(dagger_image, (guy.pos[0]*map_size + map_size*(1/4) + cos(guy.direction)*map_size/1.2, guy.pos[1]*map_size + map_size*(1/4) + sin(guy.direction)*map_size/1.2))
        
        if guy.hp <= 5:
            for num in range(guy.hp):
                screen.blit(heart_image, (num*map_size + map_size, 0))
        else:
            hp_text = font.render(str(guy.hp), False, (255, 0, 0))
            screen.blit(hp_text, (map_size,map_size*.1))
            screen.blit(heart_image, (hp_text.get_rect()[2] + map_size, 0))

        if prev_hp > guy.hp:
            hit_frames += 12*dt

        pygame.display.update((0,0,WIDTH,HEIGHT))
        game_clock.tick(tick_rate)

        current_level, frame_count = enemy_handeler.level_check(elim_goals, frame_count, current_level, guy)

    return str(enemy_handeler.elim_count), str(current_level + 1)