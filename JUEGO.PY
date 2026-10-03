import pygame
import sys
pygame.init()
x,y=3040,2160
window=pygame.dysplay.set_mode(x,y)
pygame.display.set_caption("El Cuadrado Saltarín")
fps = pygame.time.Clock()
z=pygame.font.Sysfont
cielo=(135,206,235)
blue=(40,90,200)
red=(200,50,50)
white=(255,255,255)
player=pygame.Rect(80,300,40,40)
sy=300
vy=0
g=0.8
fs=-15
ees=True
ob=pygame.Rect(80,300,40,40)
vob=6
score=6
mode=True
while mode=True:
    fps.tick(500)
    for evento in pygame.event.get():
        if evento.tipe == pygame.QUIT:
            mode=False
            keys=pygame.key.get_pressed
            modo=False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.x-=5
            if keys[pygame.K_RIGHT]:
                player.x+=5
            if keys·[pygame.K_SPACE] and ees:
                vy=fs
                ees=False
                vy+=gravedad
                player.y+=vy
            if player.y>=sy:
                player.y=sy
                vy=0
                ees=True
            ob.x-=vob
            if ob.right<0:
                ob.x=800
                score+=1
            if player.colliderect(ob):
                mode=false
            pantalla.fill(fondo)
            pygame.draw.rect(window,blue,player)
            pygame.draw.rect(window,red,ob)
            txt=Fuente.render(f"Puentes{puntos}",True,white)
            pantalla.blit(txt,(10,10))
            pygame:display.flip()
pygame.quit()
pycame.exit()
