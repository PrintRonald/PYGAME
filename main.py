import pygame 
import constantes
from personaje import Personaje
from weapon import Weapon
import os
#Funciones
#escalar imagen
def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_image = pygame.transform.scale(image,(w*scale, h*scale))
    return nueva_image

#Funcion para contar elementos
def contar_elemento(directorio):
    return len(os.listdir(directorio))

#print(contar_elemento("assets//images//characters//enemies"))

#Funcion listar nombre elementos 
def nombre_carpetas(directorio):
    return os.listdir(directorio)

#print(nombre_carpetas("assets\images\characters\enemies"))

pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption('Mi primer juego')



#Importar imagenes 
# personaje
animaciones = []
for i in range(4):
    img = pygame.image.load(f"assets//images//characters//player1//player{i}.png") 
    img = escalar_img(img,constantes.SCALA_PERSONAJE)
    animaciones.append(img)

# enemigos
directorio_enemigos = "assets//images//characters//enemies"
tipo_enemigo = nombre_carpetas(directorio_enemigos)
animaciones_enemigos = []
for eni in tipo_enemigo:
    lista_temp = []
    ruta_temp = f"assets//images//characters//enemies//{eni}"
    num_animaciones = contar_elemento(ruta_temp)
    #print(f'numero de imagenes: {num_animaciones}')
    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}//{eni}{i + 1}.PNG").convert_alpha()
        img_enemigo = escalar_img(img_enemigo,constantes.SCALA_ENEMIGOS)
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)
#print(animaciones_enemigos)

#Arma
imagen_pistola = pygame.image.load(f"assets//images//weapons//gun.png")
imagen_pistola = escalar_img(imagen_pistola,constantes.SCALA_ARMA)

#Balas
imagen_balas = pygame.image.load(f"assets//images//weapons//bullet.png")
imagen_balas = escalar_img(imagen_balas,constantes.SCALA_ARMA)
# Creacion del personaje principal 
#player_image = pygame.image.load("assets//images//characters//player1//player0.png")
#Tamaño del player alto y ancho
#player_image = pygame.transform.scale(player_image,(player_image.get_width()*constantes.SCALA_PERSONAJE,player_image.get_height()*constantes.SCALA_PERSONAJE))
#player_image = escalar_img(player_image, constantes.SCALA_PERSONAJE)

#Crear personaje de la clase personaje
jugador = Personaje(50,50,animaciones)
#Crear un enemigo de la clase Personaje
zoombie = Personaje(400, 300, animaciones_enemigos[0])
zoombie1 = Personaje(200, 200, animaciones_enemigos[1])
zoombie2 = Personaje(100, 600, animaciones_enemigos[0])
#Crear una lista de enemigos
lista_enemigos = []
lista_enemigos.append(zoombie)
lista_enemigos.append(zoombie1)
lista_enemigos.append(zoombie2)
#print(lista_enemigos)

#Crear un arma de la clase weapon
pistola = Weapon(imagen_pistola, imagen_balas)
#Crear un grupo de sprites (para gestionar las balas)
grupo_balas = pygame.sprite.Group() 

#Definir variables de movimientos del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#Controlar el frame rate
reloj = pygame.time.Clock()

# crear loop para que la ventana no se cierre
run = True
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
    #Actualiza el estado del jugador
    jugador.update()
    #Actualiza el estado del enemigo
    for ene in lista_enemigos:
        ene.update()
    #Actualiza el estado del arma
    bala = pistola.update(jugador)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        bala.update()
    #print(grupo_balas)

    #Dibujar al jugador 
    #print(f'{delta_x},{delta_y}')
    jugador.dibujar(ventana)
    #Dibuhar al enemigo 
    for ene in lista_enemigos:
        ene.dibujar(ventana)
    #Dibujar el arma
    pistola.dibujar(ventana)
    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)
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



