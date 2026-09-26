import pygame
import sys
pygame.init(python3)
x,y=3040,2160
window=pygame.dysplay.set_mode(x,y)
pygame.display.set_caption("El Cuadrado Saltarín")
fps = pygame.time.Clock()
mode=bool:True
while mode=True:
    fps.tick(500)
    for evento in pygame.event.get():
        if evento.tipe == pygame.QUIT:
            mode=False
            pygame.display.flip
            pygame.quit
            pygame.exit
            fondo=(135,206,235)
            blue=(40,90,200)
            player=pygame.Rect(80,300,40,40)
            mode=True
            while modo:
                fps.tick(500)
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        modo=False
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_LEFT]:
                            player.x-=5
                         if keys[pygame.K_RIGHT]:
                            player.x+=5
                        pantalla.fill(fondo)
                        pygame.draw.rect(window,blue,player)
                        pygame.display.flip()
                        pygame.display.,flip()
                        