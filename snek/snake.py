import random
import pygame
import sys
import pygame.freetype
from pygame.locals import *




# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False
    applepos = ''

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dirs):
        # TODO: See section 3, "Turning the snake".
        if DIR[dirs] != tuple([-1*x for x in DIR[self.direction]]):
            self.direction = dirs
        else:
            print('nope')

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        if x < 0 or x > 23 or y < 0 or y > 23:
            return True
        elif (x, y) in self.body:
            return True
        else:
            return False
        pass
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        # print('current pos')
        # print(self.body)
        x = self.body[0][0] + DIR[self.direction][0]
        # print(x)
        y = self.body[0][1] + DIR[self.direction][1]
        # print(y)
        # print([(x, y)]+ self.body[:-1])
        if self.collision(x, y):
            self.kill()
        else:
            tail = self.body[:-1]
            if len(self.body) < self.l + 1:
                tail = self.body
            self.body = [(x, y)]+ tail


    def kill(self):
        # Implements feature 11
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    
    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        pass


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        # TODO: see section 6, "moving the apple".
        pass

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface, score):
    font = pygame.font.Font('league.ttf', 25)
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)
    img = font.render("Score: " + str(score), True, (40,50,100))
    surface.blit(img, (10,445))

def start():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                return

def main():
    pygame.init()

    score = 0

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    # Implements feature 10
    startscreen = pygame.image.load('start.png')
    startscreen = startscreen.convert()
    screen.blit(startscreen, (0, 0))
    pygame.display.update()
    #screen.blit(startscreen, (0, 0))
    start() 

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface, score)


    snake = Snake()
    apple = Apple()


    while True:
        # TODO: see section 10, "incremental difficulty".
        clock.tick(5)
        snake.check_events()
        draw_grid(surface, score)
        snake.move()

        snake.draw(surface)
        apple.draw(surface)
        # TODO: see section 5, "Eating the Apple".
        if snake.body[0] == apple.position:
            #print('you ate the apple :)')
            #textsurface = myfont.render('Score:' + str(score), False, (0, 0, 0))
            score += 1
            snake.l += 1
            while apple.position in snake.body:
                apple.position = (random.randint(0, 23), random.randint(0, 23))
            snake.applepos = apple.position
        screen.blit(surface, (0,0))
        # TODO: see section 8, "Display the Score"

        pygame.display.update()
        if snake.dead:
            endscreen = pygame.image.load('lose.png')
            endscreen = endscreen.convert()
            screen.blit(endscreen, (0, 0))
            pygame.display.update()
            print('you quit')
            snake.l = 1
            snake.body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
            apple.position = (10, 10)
            score = 0
            snake.dead = False
            start()

if __name__ == "__main__":
    main()