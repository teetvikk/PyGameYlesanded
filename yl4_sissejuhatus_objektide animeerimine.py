import pygame, sys
pygame.init()

#värvid
red = [255,0,0]
blue = [0,0,255]
green = [0,255,0]
pink = [255,153,255]
lGreen = [153,255,153]
lBlue = [153,204,255]

#ekraani seaded
screenX= 640
screenY= 480
screen= pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock=pygame.time.Clock()


#graafika laadimine
ball= pygame.image.load("img/ball.png")

#kiirus ja asukoht
posX, posY = 0,0
speedX = 3
speedY = 4

gameover = False
while not gameover:
    #fps
    clock.tick(60)
    #mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    #pildi lisamine ekraanile
    screen.fill(lBlue)  #tausta puhastamine enne uuesti joonistamist.
    screen.blit(ball, (posX,posY))

    #palli liigutamine
    posX += speedX
    posY += speedY

    #kui puudutab ekraani ääri, siis muudab suunda
    if posX > screenX-ball.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY-ball.get_rect().width or posY < 0:
        speedY = -speedY

    #graafika kuvamine ekraanil
    pygame.display.flip()

pygame.quit()
sys.exit()