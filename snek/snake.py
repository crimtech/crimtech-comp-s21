import random
import pygame
import sys
import math

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
    ate = False
    pressed = False

    def __init__(self):
        pass

    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        self.direction = dir
        pass

    def in_bounds(self, loc):
        return loc[0] >= 0 and loc[0] < WIDTH and loc[1] >= 0 and loc[1] < HEIGHT

    def collision(self):
        return not(self.in_bounds(self.body[0]) and self.body[0] not in self.body[1:])

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        dx = DIR[self.direction]
        self.body = [(self.body[0][0]+dx[0], self.body[0][1]+dx[1])] + self.body[0:-1]
        if(self.ate):
            self.body = self.body + [(WIDTH, HEIGHT)]
            self.ate = False
            self.l += 1
        if(self.collision()):
            self.kill()

    def kill(self):
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        self.pressed = True
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
        return self.pressed


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        rand_loc = (rand_int(WIDTH-1), rand_int(HEIGHT-1))
        while(rand_loc in snake):
            rand_loc = (rand_int(WIDTH-1), rand_int(HEIGHT-1))
        self.position = rand_loc

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0

    while True:
        clock.tick(10 - math.floor(math.sqrt(score)))
        snake.check_events()
        draw_grid(surface)
        if(not snake.wait_for_key()):
            continue
        snake.move()

        snake.draw(surface)
        apple.draw(surface)
        screen.blit(surface, (0,0))

        if(snake.body[0] == apple.position):
            apple.place(snake.body)
            score += 1
            snake.ate = True

        pygame.display.set_caption('Score: ' + str(score))

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()
