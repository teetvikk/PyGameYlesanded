import pygame, sys
pygame.init()

# värvid
red = [255,0,0]
blue = [0,0,255]
green = [0,255,0]
pink = [255,153,255]
lGreen = [153,255,153]
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
bspeedX = 2.5
bspeedY = 3

# aluse kiirus ja asukoht
pposX = screenX/1.5
pposY = screenY - pad_h - 140
pspeedX = 3.4


# skoor
score = 0
font = pygame.font.SysFont(None, 36)  # font suurusega 36 ja süsteemi font

# taustamuuika
pygame.mixer.music.load('music/bg_music.mp3')
pygame.mixer.music.play(-1)

directionX = 0

gameover = False
running = True
while running:
    clock.tick(60)

    # sündmuste käsitlemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                directionX = "move_right"
            elif event.key == pygame.K_LEFT:
                directionX = "move_left"

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                directionX = 0

    if not gameover:
        # aluse liikumine
        if directionX == "move_left" and pposX > 0:
            pposX -= pspeedX
        elif directionX == "move_right" and pposX + pad_w < screenX:
            pposX += pspeedX

        # palli liigutamine
        bposX += bspeedX
        bposY += bspeedY

        # pall põrkub äärest
        if bposX < 0 or bposX > screenX - ball_w:
            bspeedX *= -1
        if bposY < 0:
            bspeedY *= -1

        # aluse ja palli kokkupõrge
        ball_rect = pygame.Rect(bposX, bposY, ball_w, ball_h)
        pad_rect = pygame.Rect(pposX, pposY, pad_w, pad_h)
        if bspeedY > 0 and ball_rect.colliderect(pad_rect):
            bspeedY *= -1
            score += 1

        # kui pall läheb alla äärde
        if bposY > screenY - ball_h:
            gameover = True

        # joonistamine mängu ajal
        screen.fill(lBlue)
        screen.blit(ball, (bposX, bposY))
        screen.blit(pad, (pposX, pposY))

        score_text = font.render("Skoor: " + str(score), True, (111, 0, 111))
        screen.blit(score_text, (510, 60))

    else:
        # "Game Over" ekraan
        screen.fill(lGreen)
        game_over_font = pygame.font.SysFont(None, 128)
        game_over_text = game_over_font.render("GAME OVER", True, (200, 0, 0))
        text_rect = game_over_text.get_rect(center=(screenX / 2, screenY / 2))
        screen.blit(game_over_text, text_rect)

    # uuenda ekraani iga kaader
    pygame.display.flip()

pygame.quit()
sys.exit()