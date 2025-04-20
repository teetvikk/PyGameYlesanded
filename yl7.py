import pygame, random

pygame.init()

# Ekraani seaded
laius, korgus = 640, 480
ekraan = pygame.display.set_mode([laius, korgus])
pygame.display.set_caption("Ringikesed")
kell = pygame.time.Clock()

# Ringi info: [x, y, raadius, värv]
ringid = []
raadiuse_lisa = 2
algus_raadius = 10
maks_ringid = 10


def juhuslik_varv():
    return [random.randint(0, 255) for _ in range(3)]


def kasvata_ringid():
    for ring in ringid:
        ring[2] += raadiuse_lisa


gameover = False
while not gameover:
    kell.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            kasvata_ringid()
            uus_ring = [x, y, algus_raadius, juhuslik_varv()]
            ringid.append(uus_ring)
            if len(ringid) > maks_ringid:
                ringid.pop(0)

    ekraan.fill([153, 204, 255])

    for ring in ringid:
        pygame.draw.circle(ekraan, ring[3], (ring[0], ring[1]), ring[2])

    pygame.display.flip()

pygame.quit()