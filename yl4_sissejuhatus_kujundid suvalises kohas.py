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