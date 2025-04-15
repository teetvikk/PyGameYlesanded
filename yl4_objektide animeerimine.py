import pygame, sys, random
pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
clock = pygame.time.Clock()

#graafika laadimine
bg=pygame.image.load("img/bg_rally.jpg")
f1_b=pygame.image.load("img/f1_blue.png")
f1_r=pygame.image.load("img/f1_red.png")

# kiirus ja asukoht
#posX, posY = 0, 0
#speedX, speedY = 3, 3


# autode mõõtmed
f1_b_w, f1_b_h = f1_b.get_width(), f1_b.get_height()
f1_r_w, f1_r_h = f1_r.get_width(), f1_r.get_height()

# punase auto positsioon (all keskel)
f1_r_x = (screenX - f1_r.get_width()) // 2
f1_r_y = screenY - f1_r.get_height()

# arvuta alasid
left_start = max(0, f1_r_x - 100)
left_end = f1_r_x - f1_b_w
right_start = f1_r_x + f1_r_w
right_end = min(screenX - f1_b_w, right_start + 100)

# koordinaadid sinistele autodele
"""coords = []
for i in range(10):
    if random.choice([True, False]):
        x = random.randint(left_start, left_end)
    else:
        x = random.randint(right_start, right_end)

    y = random.randint(-300, -40)
    speed = random.randint(2, 6)
    coords.append([x, y, speed])
"""

# koordinaadid sinistele autodele (ilma kattumiseta)
coords = []
attempts = 0
while len(coords) < 10 and attempts < 1000:
    attempts += 1
    if random.choice([True, False]):
        x = random.randint(left_start, left_end)
    else:
        x = random.randint(right_start, right_end)

    y = random.randint(-300, -40)
    speed = random.randint(2, 6)

    # kontrolli, et x-koordinaat ei kattuks olemasolevaga (vähemalt 40px vahe)
    too_close = False
    for c in coords:
        if abs(x - c[0]) < f1_b_w + 10:  # 10px lisapuhver
            too_close = True
            break

    if not too_close:
        coords.append([x, y, speed])

#skoor
score = 0
font = pygame.font.SysFont(None, 36)  # vaikimisi font suurusega 36

gameover = False
while not gameover:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    #tausta joonitamine
    screen.blit(bg,(0,0))

    # siniste autode liikumine ülevalt alla
    for i in range(len(coords)):
        screen.blit(f1_b, (coords[i][0], coords[i][1]))  # sinine auto
        coords[i][1] += coords[i][2]  # liigu alla

        #kui jõuab alla
        if coords[i][1] > screenY:
            #skoori suurendamine
            score += 1
            coords[i][1] = random.randint(-300, -40)

            #sinised autod ei kattuks ei vasakul ega paremal
            attempts = 0
            while attempts < 1000:
                attempts += 1
                if random.choice([True, False]):
                    new_x = random.randint(left_start, left_end)
                else:
                    new_x = random.randint(right_start, right_end)

                too_close = False
                for j, other in enumerate(coords):
                    if i != j and abs(new_x - other[0]) < f1_b_w + 10 and abs(coords[i][1] - other[1]) < f1_b_h:
                        too_close = True
                        break

                if not too_close:
                    coords[i][0] = new_x
                    break

    # punane auto all keskel
    screen.blit(f1_r, (f1_r_x, f1_r_y))

    #skoori kuvamine
    score_text = font.render("Skoor: " + str(score), True, (0, 0, 0))  # must tekst
    screen.blit(score_text, (10, 10))  # vasak ülanurk

    pygame.display.flip()
pygame.quit()
sys.exit()