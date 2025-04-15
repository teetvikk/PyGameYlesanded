import pygame #pygame baasi laadimine
pygame.init() #pygame käivitamine

screen=pygame.display.set_mode([640,480])#,pygame.RESIZABLE) #ekraani suurus ja saab muuta akna suurust lohiustamisega.
pygame.display.set_caption("My Screen") # akna nimi
screen.fill([204,255,255]) #taustavärvi muutmine

#joonistamine
#pygame.draw.line(screen,[255,0,0,], [100,100], [200,200], 2) #joon (line)
#pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2) #ristkülik (rect)
#pygame.draw.circle(screen, [0, 0, 255], [150,200], 100, 1) #ring (circle)
#pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2) #hulknurk (polygon)
#pygame.draw.ellipse(screen, [0, 225, 0], [50, 80, 200, 300], 2) #ovaal (ellipse)
pygame.draw.arc(screen,[0,0,0], [100,100,250,200], 0, 3.14*1.5, 1) #kaar (arc) Lisandub ainult kaare algus- ja lõpppunkti määramine. Täisringi saad, kui määrad kaare aluspunkti 0 ja lõpp-punkti 2*π. Seega poolkaare saad kui lisad ainult π-väärtuse jne. pygame.draw.arc(screen, värv, ristküliku_koordinaadid, start_nurk, lõpp_nurk, joone_paksus)

pygame.display.flip() #ekraani värskendamine




#värvid
"""
punane = (255,0,0)
roheline = (0,255,0)
sinine = (0,0,255)
valge = (255,255,255)
must = (0,0,0)
"""
#värve saab valida netist https://www.w3schools.com/colors/colors_picker.asp aadressilt.


#joon spikker
"""
syntax #pygame.draw.line(aken, värv, algus_pos, lõpp_pos, paksus)

#aken – muutuja nimi, millega akna tekitasid ehk kuhu kujund lisatakse
#värv – kasutame RGB värvimudelit, näiteks [255,0,0]
#algus_pos – joone alguspunkti koordinaadid [x,y]
#lõpp_pos – joonelõpppunkti koordinaadid [x,y]
#paksus – joone paksus, vaikimisi 1px

"""


#kood, et aken ei sulguks kohe ja saaks ristist sulgeda
gameover = False
while not gameover:
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True