import pygame 
import constantes
from personaje import Personaje

jugador = Personaje(50,50)


pygame.init()



run = True
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption('Mi primer juego')
# crear loop para que la ventana no se cierre
while run == True:
    jugador.dibujar(ventana)

    for event in pygame.event.get():
        # Para poder cerrar la ventana o salir del bucle
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.QUIT()



