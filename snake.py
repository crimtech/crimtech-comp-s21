
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
    body = [ (WIDTH // 2 + 1, HEIGHT // 2) , (WIDTH // 2, HEIGHT // 2) ]
    direction = 'r'
    prev = ''
    dead = False
    length=2

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # TODO: See section 3, "Turning the snake".
        self.prev = self.direction
        self.direction = dir

        # if (self.direction=='r'):
        #     temp=self.get_head()
            # self.body[]



    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        collided = False
        if x<0 or x>24:
            collided=True
        if y<0 or y>24:
            collided=True
        # if get_head(self) == (x,y)
        #     collided=True
        
        return collided
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self, apple):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times. 
        head=self.body[0]
        tail=self.body[-1]
        change=DIR[self.direction]
        coord = self.body[0] 
        new_coord = (coord[0] + change[0], coord[1] + change[1])

        if (self.prev=="r" and self.direction=="l"):
            self.kill()
        if (self.prev=="l" and self.direction=="r"):
            self.kill()
        if (self.prev=="u" and self.direction=="d"):
            self.kill()
        if (self.prev=="d" and self.direction=="u"):
            self.kill()



        self.body.insert(0, new_coord)
        self.body.remove(tail)

        if (self.body[0]==apple):
            self.body.append(tail)

        for i in range(1, len(self.body)):
            if (self.body[0] == self.body[i]):
                self.kill()

        if self.collision(head[0], head[1]):
            self.kill()
    

    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            # pygame.draw.rect(surface, self.get_color(i), r)
            pygame.draw.rect(surface, (0, 0, 0), r)


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
        randx = random.randint(0,23)
        randy = random.randint(0,23)

        for i in range(len(snake)):
            if i==(randx, randy):
                randx = random.randint(0,24)
                randy = random.randint(0,24)

        self.position=(randx, randy)
      

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

    # display_surface = pygame.display.set_mode((12, 12))
    # pygame.display.set_caption('Show Text')
    # font = pygame.font.Font('freesansbold.ttf', 32)
    # green = (0, 255, 0)
    # blue = (0, 0, 128)
    # text = font.render('GeeksForGeeks', True, green, blue)
    # textRect = text.get_rect()
    

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0

    # myfont = pygame.font.SysFont('Comic Sans MS', 30)
    # textsurface = myfont.render(str(score), True, (0, 0, 0))

    while True:
        # TODO: see section 10, "incremental difficulty".
        # display_surface.blit(text, textRect)
        
        clock.tick(8)
        snake.check_events()
        draw_grid(surface)        
        snake.move(apple.position)
        # print(snake.get_head())

        snake.draw(surface)
        apple.draw(surface)
        
        # TODO: see section 5, "Eating the Apple".
        if snake.get_head() == apple.position:
            print("the snake at an apple!")
            apple.place(snake.body) #i think this is the issue
            score=score+1
        
        screen.blit(surface, (0,0))
        # TODO: see section 8, "Display the Score"
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(score), True, (0, 0, 0))
        screen.blit(textsurface,(10,10))
        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()