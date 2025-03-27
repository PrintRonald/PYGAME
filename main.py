import pygame 
import constantes
from personaje import Personaje


pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption('Mi primer juego')

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_image = pygame.transform.scale(image,(w*scale, h*scale))
    return nueva_image


animaciones = []
for i in range(4):
    img = pygame.image.load(f"assets//images//characters//player1//player{i}.png") 
    img = escalar_img(img,constantes.SCALA_PERSONAJE)
    animaciones.append(img)

# Creacion del personaje principal 
#player_image = pygame.image.load("assets//images//characters//player1//player0.png")
#Tamaño del player alto y ancho
#player_image = pygame.transform.scale(player_image,(player_image.get_width()*constantes.SCALA_PERSONAJE,player_image.get_height()*constantes.SCALA_PERSONAJE))
#player_image = escalar_img(player_image, constantes.SCALA_PERSONAJE)

jugador = Personaje(50,50,animaciones)

run = True

#Definir variables de movimientos del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#Controlar el frame rate
reloj = pygame.time.Clock()

# crear loop para que la ventana no se cierre
while run == True:
    #que vaya a 60 FPS
    reloj.tick(constantes.FPS)
    ventana.fill(constantes.COLOR_BG)

    #Calcular el movimiento del juagador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD
    
    #mover al jugador
    jugador.movimiento(delta_x, delta_y)

    jugador.update()

    #print(f'{delta_x},{delta_y}')

    jugador.dibujar(ventana)

    for event in pygame.event.get():
        # Para poder cerrar la ventana o salir del bucle
        if event.type == pygame.QUIT:
            run = False
        #Para cuando se presiona la tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True 
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
        #Para cuando se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False


    pygame.display.update()
pygame.QUIT()



