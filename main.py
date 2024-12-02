import pygame

width = 800
height = 800

bg = pygame.image.load("starbg.png")
alienship = pygame.image.load("alienShip.png")
asteroid50 = pygame.image.load("asteroid50.png")
asteroid150 = pygame.image.load("asteroid150.png")
asteroid100 = pygame.image.load("asteroid100.png")
playerocket = pygame.image.load("spaceRocket.png")
star = pygame.image.load("star.png")

pygame.display.set_caption("Asteroids")
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

gameover = False

def redrawgamewindow():
     win.blit(bg,(0,0))


run = True
while run:
    clock.tick(60)
    if not gameover:
          pass
    for event in pygame.event.get():
        if event.type == quit:
            run = False