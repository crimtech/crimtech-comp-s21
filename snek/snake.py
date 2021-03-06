import random
import pygame
import sys

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

    def collision(self, x, y):
        if x < 0 or x > 23:
            return True
        elif y < 0 or y > 23:
            return True
        elif (x,y) in self.body[1:]:
            return True
        else:
            return False

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        body2 = []
        body2.append((self.get_head()[0] + DIR[self.direction][0], self.get_head()[1] + DIR[self.direction][1]))

        for i in range(len(self.body) - 1):
            body2.append(self.body[i])

        if len(self.body) - self.l != 1:
            body2.append(self.body[len(self.body) - 1])

        self.body = body2
        if self.collision(self.get_head()[0], self.get_head()[1]):
            self.kill()
        pass

    def kill(self):
        # TODO: See section 11, "Try again!"
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
        print("press any key to begin")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        pos2 = self.position
        while pos2 in snake:
            pos2 = (rand_int(23), rand_int(23))
        self.position = pos2


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
    pygame.font.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0
    should_wait = True
    while True:
        # TODO: see section 10, "incremental difficulty".
        clock.tick(10)
        snake.check_events()
        draw_grid(surface)
        snake.move()

        snake.draw(surface)
        apple.draw(surface)
        # TODO: see section 5, "Eating the Apple".

        if snake.get_head() == apple.position:
            print("the snake ate an apple!")
            apple.place(snake.body)
            score += 1
            snake.l += 1

        screen.blit(surface, (0,0))
        scorefont = pygame.font.SysFont('Times New Roman', 30)
        scoreboard = scorefont.render("Score: %d" % score, False, (0,0,0))
        screen.blit(scoreboard,(0,1))
        # TODO: see section 8, "Display the Score"

        pygame.display.update()
        if should_wait:
            snake.wait_for_key()
        should_wait = False
        if snake.dead:
            print('You died. Score: %d' % score)
            main()


if __name__ == "__main__":
    main()
