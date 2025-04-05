import pygame
from sys import exit
import random

class make_pillar():
    def __init__(self):
        self.height = random.randint(50,400)
        self.up = pygame.Surface((50, self.height ))
        self.up_rect = self.up.get_rect(topleft = (500, 0))
        self.down = pygame.Surface((50, 600-self.height-150))
        self.down_rect = self.down.get_rect(topleft = (500, self.height+150))
        self.up.fill('black')
        self.down.fill('black')

def move_pillar(pillar):
    pillar.up_rect.x  -= 2
    pillar.down_rect.x-= 2
    if pillar.up_rect.x  == -50:
        global score 
        score += 1
        return 1
    if pillar.up_rect.colliderect(bird_rect) or pillar.down_rect.colliderect(bird_rect):
        pillar.up.fill('red')
        pillar.down.fill('red')
        global running
        running = False
    screen.blit(pillar.up, pillar.up_rect)
    screen.blit(pillar.down, pillar.down_rect)
    return 0

def reset_game():
    global pillar1, pillar2, two, three, running, gravity, score, bird_rect
    pillar1 = make_pillar()
    two, three, gravity, score = 0, 0, 0, 0
    bird_rect = bird.get_rect(center = (40,100))
    running = True

pygame.init()
screen = pygame.display.set_mode((500,600))
bg = pygame.Surface((800,600))
bg.fill('turquoise1')

pillar1 = make_pillar()

two,three = 0,0
running = True
clock = pygame.time.Clock()
gravity = 0
score = 0
font = pygame.font.Font(None, 80)

bird = pygame.image.load('bird.png').convert()
bird = pygame.transform.scale(bird, (40,40))
bird_rect = bird.get_rect(center = (40,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity = -5   
                if not running:
                    reset_game()


    if running: 
        gravity += 0.4
        bird_rect.y += gravity
        if(bird_rect.y >=560):
            bird_rect.y = 560
    
        screen.blit(bg,(0,0))
        
        if move_pillar(pillar1) == 1:
            pillar1 = make_pillar()
        if pillar1.up_rect.x == 250:
            pillar2 = make_pillar()
            two = True
        if two:
            move_pillar(pillar2)
        
        screen.blit(font.render(f"{score}", True, 'white'), (250,15))
        screen.blit(bird, bird_rect)
    
    pygame.display.update()
    clock.tick(60)   
