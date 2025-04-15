"""
import pygame
import sys
pygame.init()

#värvid
lGreen = [153, 255, 153]
lBlue = [153,204,255]

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)

gameover = False

while not gameover:

    #Lisame pildid
    youWin=pygame.image.load("image/youwin.ping")
    youWin=pygame.transform.scale(youWin, [300, 120])
    screen.blit(youWin, [180, 100])

    pygame.display.flip()

    #mängu sulgemine ristist

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

pygame.quit()
"""
"""
import pygame
import random

pygame.init()

#värvid
red = [255, 0, 0]
lGreen = [153, 255, 153]

#ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)
running = True

for i in range(1, 10):
    x = random.randint(0, 620)
    y = random.randint(0, 460)
    pygame.draw.rect(screen, red, [x, y, 20, 20])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
"""
"""
import pygame
import sys
import random
gameover = False

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]

# ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)


# funktsioonid
def drawHouse(x, y, width, height, screen, color):
    points = [(x, y - ((3 / 4.0) * height)), (x, y), (x + width, y), (x + width, y - (3 / 4.0) * height),
              (x, y - ((3 / 4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)


# kutsun funktsiooni välja
drawHouse(100, 400, 300, 200, screen, red)

pygame.display.flip()

while not gameover:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

pygame.quit()
"""