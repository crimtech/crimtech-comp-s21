import random
import pygame
import sys
import time

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1, 0),
    'r' : (1, 0)
}


class Snake(object):

    def __init__(self):
        self.l = 1
        self.body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
        self.direction = 'r'
        self.dead = False

    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (len(self.body) - i) + y * i) / len(self.body), hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # TODO: See section 3, "Turning the snake".
        self.direction = dir

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        if x < 0 or x >= WIDTH or y < 0 or y >= WIDTH:
        	return True
        if self.body[0] in self.body[1:]:
        	return True

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self, apple):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        dx, dy = DIR[self.direction]
        self.body.insert(0, (self.body[0][0] + dx, self.body[0][1] + dy))
        if apple != self.body[0]:
        	self.body = self.body[:-1]
        if self.collision(self.body[0][0], self.body[0][1]):
        	self.kill()

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
        while self.position in snake:
        	x = random.randrange(0, WIDTH)
        	y = random.randrange(0, HEIGHT)
        	self.position = (x, y)
        pass

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

    start = False

    while True:
        if snake.dead:
            # print('You died. Score: %d' % score)
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(f'You died. Score: {score}. Press any key to play again', True, (255, 255, 255), (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)
            pygame.draw.rect(surface, (0,0,0), pygame.Rect((100, 100), (10, 10)))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    snake = Snake()
                    apple = Apple()
                    score = 0

        elif start:
            clock.tick(9 + int(len(snake.body) ** 0.5))
        	# TODO: see section 10, "incremental difficulty".
            snake.check_events()
            draw_grid(surface)
            snake.move(apple.position)

            if snake.body[0] == apple.position:
            	print('the snake ate an apple!')
            	apple.place(snake.body)
            	score += 1

            snake.draw(surface)
            apple.draw(surface)
            screen.blit(surface, (0,0))
            # TODO: see section 8, "Display the Score"

        else:
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Press any key to start', True, (255, 255, 255), (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)
            pygame.draw.rect(surface, (0,0,0), pygame.Rect((100, 100), (10, 10)))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    start = True

        pygame.display.update()

            # pygame.quit()
            # sys.exit(0)

if __name__ == "__main__":
    main()
