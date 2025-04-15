import pygame
pygame.init()

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#lisame teksti
#font = pygame.font.Font(None, 30)
#font = pygame.font.SysFont("Tahoma", 50) #kindla fondi määramine
font = pygame.font.Font(pygame.font.match_font('arial'), 50) #ligikaudne fondi nime määramine
font.set_underline(True) #teksti allajoonimine
                         #set_bold(True) – rasvaselt
                         #set_italic(True) – kaldkiri
text = font.render("Hello PyGame", True, [0,0,0])

#tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height

#screen.blit(text, [320,240])

# loome tekstikasti ja asetame selle ekraani keskele
text_rect = text.get_rect(center=(320, 240))
screen.blit(text, text_rect)

pygame.display.flip()

gameover = False
while not gameover:
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True