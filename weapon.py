import pygame
import constantes
import math

class Weapon():
    def __init__(self,image):
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original,self.angulo)
        self.forma = self.imagen.get_rect()

    def update(self, personaje):
        # Estamos centrando la imagen del arma al centro del personaje
        self.forma.center = personaje.forma.center
        # Para rotar el arma en el eje x
        if personaje.flip == False:
            self.forma.x = self.forma.x + personaje.forma.width/4
            self.rotar_arma(False)
        if personaje.flip == True:
            self.forma.x = self.forma.x - personaje.forma.width/4
            self.rotar_arma(True)
        #Mover la pistola con el mause
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y,distancia_x))
        
        print(self.angulo)
        #self.forma.y = self.forma.y + 4

    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.imagen_original,True,False) 
            self.imagen = pygame.transform.rotate(imagen_flip,self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original,False,False)
            self.imagen = pygame.transform.rotate(imagen_flip,self.angulo)
    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen,self.angulo)
        interfaz.blit(self.imagen,self.forma)
        #pygame.draw.rect(interfaz,constantes.COLOR_ARMA, self.forma, 1)

    