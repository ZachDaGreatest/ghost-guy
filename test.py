from turtle import *
import math

#todo fix movement
#to get rid of fish eye effect use components of distance

#modifiables
block_width = 16
block_height = 9
fov = 90
segments = 90
turn_dagree = 45

#lists
outer_walls = []
distances = []

#functions
def start():
    wn.setup(640,480)
    wn.bgcolor('black')
    wn.setworldcoordinates(0,0,segments,2)
    wn.tracer(False)
    level()
    turt.find_wall_locations()
    create.make_render()
    wn.onkeypress(turt.turn_right, 'd')
    wn.onkeypress(turt.turn_left, 'a')
    wn.onkeypress(turt.move_forward, 'w')
    wn.onkeypress(turt.move_backwards, 's')
    wn.listen()

#classes
class player:
    def __init__(self) -> None:
        player.position = (4,4)
        player.orientation = 90
    def cast_ray(self, ray_orientation):
        contact = False
        walls = outer_walls
        ray_pos = player.position
        ray_orientation = ray_orientation
        time = 0
        while contact == False:
            time += 1
            ray_pos = (ray_pos[0] + math.cos(math.radians(ray_orientation)), ray_pos[1] + math.sin(math.radians(ray_orientation)))
            hitbox = .5
            if time < 12:
                for box in walls:
                    if (box[1]-hitbox <= ray_pos[1] <= box[1]+hitbox and box[0]-hitbox <= ray_pos[0] <= box[0]+hitbox):
                        contact == True
                        wall_position = ray_pos
                        wall_position = (round(wall_position[1],0),round(wall_position[0],0))
                        # time = 0
                        return wall_position
            if time > 100:
                print('not working')
                wall_position = 100,100
                return wall_position
    def find_wall_locations(self):
        global distances
        distances = []
        incrament = fov/segments
        starting_orientation = player.orientation-(fov/2)
        for time_through in range(segments):
            box_location = self.cast_ray(ray_orientation=(starting_orientation+(incrament*time_through)))
            box_distance = math.sqrt((box_location[1]-player.position[0])**2 + (box_location[0]-player.position[0])**2)
            box_distance = round(box_distance,2)
            distances.append(box_distance)
    def turn_right(self):
        print('right')
        player.orientation -= turn_dagree
        if player.orientation < 0:
            player.orientation = player.orientation + 360
        if player.orientation > 360:
            player.orientation = player.orientation - 360
        print(player.orientation)
        create.reset()
        self.find_wall_locations()
        create.make_render()
        wn.update()
    def turn_left(self):
        print('left')
        player.orientation += turn_dagree
        if player.orientation < 0:
            player.orientation = player.orientation + 360
        if player.orientation > 360:
            player.orientation = player.orientation - 360
        print(player.orientation)
        create.reset()
        self.find_wall_locations()
        create.make_render()
        wn.update()
    def move_forward(self):
        global distances
        print('forwards')
        new_pos = (round(player.position[0]+math.cos(math.radians(player.orientation)),2),round(player.position[1]+math.sin(math.radians(player.orientation)),2))
        hitbox = .5
        hit_wall = False
        for box in outer_walls:
            if (box[1]-hitbox <= new_pos[1] <= box[1]+hitbox and box[0]-hitbox <= new_pos[0] <= box[0]+hitbox):
                print('hit a wall')
                hit_wall = True
        if hit_wall == False:
            player.position = new_pos
        create.reset()
        self.find_wall_locations()
        if hit_wall == True:
            for distance in distances:
                if distance == 2:
                    index_num = distances.index(2)
                    distances.insert(index_num, 1)
                    distances.pop(index_num+1)
                    print (distances[index_num])
        create.make_render()
        wn.update()
        print(player.position)
    def move_backwards(self):
        print('backwards')
        new_pos = (round(player.position[0]-math.cos(math.radians(player.orientation)),2),round(player.position[1]-math.sin(math.radians(player.orientation)),2))
        hitbox = .5
        hit_wall = False
        for box in outer_walls:
            if (box[1]-hitbox <= new_pos[1] <= box[1]+hitbox and box[0]-hitbox <= new_pos[0] <= box[0]+hitbox):
                print('hit a wall')
                hit_wall = True
        if hit_wall == False:
            player.position = new_pos
        else:
            print(distances)
        create.reset()
        self.find_wall_locations()
        create.make_render()
        wn.update()
        print(player.position)


    def test(self):
        pass

class level:
    def __init__(self) -> None:
        print('making level')
        global outer_walls
        id_num = 0
        id_num_2 = 0
        for number in range(2):
            for num in range((block_width)+1):
                outer_walls.append((id_num,block_height*id_num_2))
                id_num += (1)
            id_num_2 += 1
            id_num = 0
        id_num = 1
        id_num_2 = 0
        for number in range(2):
            for num in range((block_height)-1):
                outer_walls.append((id_num_2*block_width,id_num))
                id_num += 1
            id_num_2 += 1
            id_num = 1
        outer_walls.append((4,6))
    
class renderer:
    def __init__(self) -> None:
        self.render_maker = Turtle('square')
        self.render_maker.speed(0)
        self.size = 30/segments
        self.render_maker.shapesize(self.size)
    def make_render(self):
        self.render_maker.penup()
        num = segments
        for dis in distances:
            self.render_maker.goto(num-.4,1)
            if dis < 12:
                if dis == 1:
                    self.render_maker.color('red')
                    self.render_maker.shapesize(100/(2*dis),self.size)
                    self.render_maker.stamp()
                else:
                    hex_num = int(1/(dis)*100)
                    hex_num = ("#" + str(hex_num) + str(hex_num) + str(hex_num))
                    self.render_maker.color(hex_num)
                    self.render_maker.shapesize(100/(2*dis),self.size)
                    self.render_maker.stamp()
            else:
                self.render_maker.shapesize(1)
                self.render_maker.color('red')
                self.render_maker.stamp()
            num -= 1
        self.render_maker.goto(100,100)
    def reset(self):
        self.render_maker.clearstamps()


#setup
create = renderer()
turt = player()
wn = Screen()

#the stuff
start()
wn.mainloop()