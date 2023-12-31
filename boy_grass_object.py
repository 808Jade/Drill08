from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5

class Smallball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= random.randint(1,10)
        if self.y <= 60:
            self.y = 60

class Bigball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= random.randint(1,10)
        if self.y <= 70:
            self.y = 70

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world
    global small_ball
    global big_ball

    running = True
    world = []

    grass = Grass()  # 클래스를 이용해서 객제를 찍어냄.
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    rand = random.randint(1,19)
    small_ball = [Smallball() for i in range(rand)]
    world += small_ball

    rand = 20 - rand
    big_ball = [Bigball() for i in range(rand)]
    world+= big_ball

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def update_world():
    for o in world:
        o.update()
    pass


open_canvas()
# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
