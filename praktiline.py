#Teet Russ IS24
import pygame, sys, random, time

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
lBlue = [153, 204, 255]
black = [0, 0, 0]
alive = green

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ruut - 90min ül")
clock = pygame.time.Clock()
screen.fill(lBlue)

# ruudu kordinaatide muutujate defineerimine
ruutX = 310
ruutY = 230

# ruudu loomine
ruut = pygame.Rect(ruutX, ruutY, 20, 20)
pygame.draw.rect(screen, alive, ruut)

# kiirus ja asukoht
posX, posY = 0, 0

# koordinaatide loomine ja lisamine massiivi
coords = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords.append([posX, posY])
    print(coords)

coords2 = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords2.append([posX, posY])
    print(coords2)

coords3 = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords3.append([posX, posY])
    print(coords3)

coords4 = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords4.append([posX, posY])
    print(coords4)

coords5 = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords5.append([posX, posY])
    print(coords5)

coords = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords.append([posX, posY])
    print(coords)

coords6 = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords6.append([posX, posY])
    print(coords6)

coords7 = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords7.append([posX, posY])
    print(coords7)

coords8 = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords8.append([posX, posY])
    print(coords8)

coords9 = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords9.append([posX, posY])
    print(coords9)

coords10 = []
for i in range(1):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords10.append([posX, posY])
    print(coords10)

enemy = pygame.Rect([coords[i][0], coords[i][1], random.randint(10, 100), random.randint(10, 100)])
enemy2 = pygame.Rect([coords2[i][0], coords2[i][1], random.randint(10, 100), random.randint(10, 100)])
enemy3 = pygame.Rect([coords3[i][0], coords3[i][1], random.randint(10, 100), random.randint(10, 100)])
enemy4 = pygame.Rect([coords4[i][0], coords4[i][1], random.randint(10, 100), random.randint(10, 100)])
enemy5 = pygame.Rect([coords5[i][0], coords5[i][1], random.randint(10, 100), random.randint(10, 100)])
enemy6 = pygame.Rect([coords6[i][0], coords6[i][1], random.randint(10, 100), random.randint(10, 100)])
enemy7 = pygame.Rect([coords7[i][0], coords7[i][1], random.randint(10, 100), random.randint(10, 100)])
enemy8 = pygame.Rect([coords8[i][0], coords8[i][1], random.randint(10, 100), random.randint(10, 100)])
enemy9 = pygame.Rect([coords9[i][0], coords9[i][1], random.randint(10, 100), random.randint(10, 100)])
enemy10 = pygame.Rect([coords10[i][0], coords10[i][1], random.randint(10, 100), random.randint(10, 100)])

# mängu loop
running = True
while running:
    clock.tick(60)  # fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # võimaldab ristist kinni panemise
            running = False

    ### punase ruudu liikuma panemine ###

    # tuvastab klahvi vajutusi
    pressed = pygame.key.get_pressed()
    # klahvi vajutusel liigub ruut
    if pressed[pygame.K_UP]:
        ruutY -= 4
        ruut = pygame.Rect(ruutX, ruutY, 20, 20)
    if pressed[pygame.K_DOWN]:
        ruutY += 4
        ruut = pygame.Rect(ruutX, ruutY, 20, 20)
    if pressed[pygame.K_LEFT]:
        ruutX -= 4
        ruut = pygame.Rect(ruutX, ruutY, 20, 20)
    if pressed[pygame.K_RIGHT]:
        ruutX += 4
        ruut = pygame.Rect(ruutX, ruutY, 20, 20)

    # kontrollib, kas punane ruut on tee piirides ja piirab sisse
    if ruutX < 0:
        ruutX = 0
    if ruutX > 620:
        ruutX = 620

    if ruutY < 0:
        ruutY = 0
    if ruutY > 460:
        ruutY = 460

    if ruut.colliderect(enemy):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    if ruut.colliderect(enemy2):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    if ruut.colliderect(enemy3):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    if ruut.colliderect(enemy4):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    if ruut.colliderect(enemy5):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    if ruut.colliderect(enemy6):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    if ruut.colliderect(enemy7):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    if ruut.colliderect(enemy8):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    if ruut.colliderect(enemy9):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    if ruut.colliderect(enemy10):
        alive = red
        time.sleep(1)  # ootab sekundi
        running = False  # paneb mängu kinni

    screen.fill(lBlue)  # täidab tausta (et jälge ei tekiks)
    pygame.draw.rect(screen, alive, ruut)  # joonistab ruudu peale igat uuendust

    pygame.draw.rect(screen, black, enemy)
    pygame.draw.rect(screen, black, enemy2)
    pygame.draw.rect(screen, black, enemy3)
    pygame.draw.rect(screen, black, enemy4)
    pygame.draw.rect(screen, black, enemy5)
    pygame.draw.rect(screen, black, enemy6)
    pygame.draw.rect(screen, black, enemy7)
    pygame.draw.rect(screen, black, enemy8)
    pygame.draw.rect(screen, black, enemy9)
    pygame.draw.rect(screen, black, enemy10)

    pygame.display.flip()  # värskendab

pygame.quit()