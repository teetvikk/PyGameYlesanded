import pygame, sys
pygame.init()

# värvid
"""red = [255,0,0]
blue = [0,0,255]
green = [0,255,0]
pink = [255,153,255]
lGreen = [153,255,153]"""
lBlue = [153,204,255]

# ekraani seaded
screenX= 640
screenY= 480
screen= pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Ping-pong")
screen.fill(lBlue)
clock=pygame.time.Clock()


# graafika laadimine
ball= pygame.image.load("img/ball.png")
pad= pygame.image.load("img/pad.png")

# graafika suurus
ball = pygame.transform.scale(ball, (20,20))
pad = pygame.transform.scale(pad, (120,20))

# parem suuruse viide
ball_w, ball_h = ball.get_width(), ball.get_height()
pad_w, pad_h = pad.get_width(), pad.get_height()

# Palli kiirus ja asukoht
bposX, bposY = 0,0
bspeedX = 3
bspeedY = 4

# aluse kiirus ja asukoht
pposX = screenX/1.5
pposY = screenY - pad_h - 140
pspeedX = 3.4
# pspeedY = 0

# skoor
score = 0
font = pygame.font.SysFont(None, 36)  # font suurusega 36 ja süsteemi font

gameover = False
while not gameover:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    # palli liigutamine
    bposX += bspeedX
    bposY += bspeedY

    # pall põrkub vastu ekraani ääri
    if bposX < 0 or bposX > screenX - ball_w:
        bspeedX *= -1
    if bposY < 0 or bposY > screenY - ball_h:
        bspeedY *= -1

     # alus liigub
    pposX += pspeedX
    if pposX < 0 or pposX > screenX - pad_w:
        pspeedX *= -1

    # palli ja aluse kokkupõrke kontroll
    ball_rect = pygame.Rect(bposX, bposY, ball_w, ball_h)
    pad_rect = pygame.Rect(pposX, pposY, pad_w, pad_h)
    if bspeedY > 0  and ball_rect.colliderect(pad_rect):
        bspeedY *= -1
        score += 1

    # kui jõuab alla
    if bposY > screenY - ball_h:
        # skoori vähendamine
        score -= 1



    # pildi lisamine ekraanile
    screen.fill(lBlue)  # tausta puhastamine enne uuesti joonistamist.
    screen.blit(ball, (bposX, bposY))
    screen.blit(pad, (pposX, pposY))

    # skoori kuvamine
    score_text = font.render("Skoor: " + str(score), True, (111, 0, 111))  #skoori tekst
    screen.blit(score_text, (510, 60))  # parem ülanurk

    #graafika kuvamine ekraanil
    pygame.display.flip()

pygame.quit()
sys.exit()