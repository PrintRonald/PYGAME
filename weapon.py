import pygame
import constantes
import math
import random

class Weapon():
    def __init__(self,image, imagen_bala):
        self.imagen_bala =  imagen_bala
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original,self.angulo)
        self.forma = self.imagen.get_rect()
        self.disparada = False
        self.ultimo_disparo = pygame.time.get_ticks()

    def update(self, personaje):
        disparo_cooldown = constantes.COOLDOWN_BALAS
        bala = None
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
        #print(self.angulo)
        #self.forma.y = self.forma.y + 4

        #detectar los click del mause
        if pygame.mouse.get_pressed()[0] and self.disparada == False and (pygame.time.get_ticks()-self.ultimo_disparo >= disparo_cooldown):
            bala = Bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            self.disparada = True
            self.ultimo_disparo = pygame.time.get_ticks()
        #Resetear el click del mause
        if pygame.mouse.get_pressed()[0] == False:
            self.disparada = False
        return bala
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



class Bullet(pygame.sprite.Sprite):
    def __init__(self,image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)    
        self.delta_x = math.cos(math.radians(self.angulo))*constantes.VELOCIDAD_BALA 
        self.delta_y = -math.sin(math.radians(self.angulo))*constantes.VELOCIDAD_BALA
    
    def update(self, lista_enemigos):
        dano = 0
        pos_dano = None
        self.rect.x += self.delta_x
        self.rect.y = self.rect.y + self.delta_y

        #Ver si las balas salieron de pantalla
        if self.rect.right < 0 or self.rect.left > constantes.ANCHO_VENTANA or self.rect.top > constantes.ALTO_VENTANA:
            self.kill()
        
        #Verificar si hay colisión con los enemigos
        for enemigo in lista_enemigos:
            if enemigo.forma.colliderect(self.rect):
                dano = 15 + random.randint(-7,7)
                pos_dano = enemigo.forma  
                enemigo.energia = enemigo.energia - dano
                self.kill()
                break
                
        return dano, pos_dano
    
    def dibujar(self, interfaz):
        #Los parentesis para los ejes x e y
        interfaz.blit(self.image,(self.rect.centerx,(self.rect.centery - int(self.image.get_height()/2))))             
                            