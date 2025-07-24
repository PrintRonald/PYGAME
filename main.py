import pygame 
import constantes
from personaje import Personaje
from weapon import Weapon
from textos import DamageText
from items import Item
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

#Fuentes
font = pygame.font.Font('assets/joystix/joystix_monospace.otf',25)

#Importar imagenes 

#Energía 

corazon_vacio = pygame.image.load('assets//images//items//heart_empty.png').convert_alpha()
corazon_vacio = escalar_img(corazon_vacio, constantes.SCALA_CORAZON)
corazon_mitad = pygame.image.load('assets//images//items//heart_half.png').convert_alpha()
corazon_mitad = escalar_img(corazon_mitad, constantes.SCALA_CORAZON)
corazon_lleno = pygame.image.load('assets//images//items//heart_full.png').convert_alpha()
corazon_lleno = escalar_img(corazon_lleno, constantes.SCALA_CORAZON)

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

#Cargar imagenes de los items
posion_roja = pygame.image.load("assets//images//items//potion.PNG")
posion_roja = escalar_img(posion_roja, 0.25)

#Cargar imagenes coin
coin_images = []
ruta_img ="assets//images//items//coin"
num_coin_images = contar_elemento(ruta_img)
#print(f"Numero de imagenes de monedas: {num_coin_images}")
for i in range(num_coin_images):
    img = pygame.image.load(f"assets//images//items//coin//coin_{i+1}.PNG")
    img = escalar_img(img,0.25)
    coin_images.append(img)

#Dibujar texto en pantalla
def dibujar_texto(texto,fuente,color,x,y):
    img = fuente.render(texto,True,color)
    ventana.blit(img, (x,y)) 

def vida_jugador():
    c_mitad_dibujado = False
    for i in range(5):
        if jugador.energia >= ((i+1)*20):
            ventana.blit(corazon_lleno, (5+i*50,5))
        elif jugador.energia % 20 > 0 and c_mitad_dibujado == False:
            ventana.blit(corazon_mitad, (5+i*50,5))
            c_mitad_dibujado = True
        else:
            ventana.blit(corazon_vacio, (5+i*50,5))
        

#Crear personaje de la clase personaje
jugador = Personaje(50,50,animaciones, 20)
#Crear un enemigo de la clase Personaje
zoombie = Personaje(400, 300, animaciones_enemigos[0], 100)
zoombie1 = Personaje(200, 200, animaciones_enemigos[1], 100)
zoombie2 = Personaje(100, 600, animaciones_enemigos[0], 100)
zoombie3 = Personaje(340, 550, animaciones_enemigos[1], 100)
#Crear una lista de enemigos
lista_enemigos = []
lista_enemigos.append(zoombie)
lista_enemigos.append(zoombie1)
lista_enemigos.append(zoombie2)
lista_enemigos.append(zoombie3)
#print(lista_enemigos)

#Crear un arma de la clase weapon
pistola = Weapon(imagen_pistola, imagen_balas)
#Crear un grupo de sprites (para gestionar las balas)
grupo_damage_text = pygame.sprite.Group() 
grupo_balas = pygame.sprite.Group() 
grupo_items = pygame.sprite.Group()

coin = Item(350,25,0,coin_images)
potion = Item(380,55,1,[posion_roja])

grupo_items.add(coin)
grupo_items.add(potion)

# temporal y despues borrar
#damage_text = DamageText(100, 240, '25', font, constantes.ROJO)
#grupo_damage_text.add(damage_text)


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
        print(ene.energia)
    #Actualiza el estado del arma
    bala = pistola.update(jugador)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        damage, pos_damage = bala.update(lista_enemigos)
        if damage != 0:
            damage_text = DamageText(pos_damage.centerx, pos_damage.centery, str(damage), font, constantes.ROJO)
            grupo_damage_text.add(damage_text)
    #print(grupo_balas)

    #Actualizar daño 
    grupo_damage_text.update()

    #Actualizar items
    grupo_items.update(jugador)

    #Dibujar al jugador 
    #print(f'{delta_x},{delta_y}')
    jugador.dibujar(ventana)
    #Dibujar al enemigo 
    for ene in lista_enemigos:
        ene.dibujar(ventana)
    #Dibujar el arma
    pistola.dibujar(ventana)
    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana) 
    #Dibujar corazones 
    vida_jugador()
    #Dibujar textos
    grupo_damage_text.draw(ventana)
    dibujar_texto(f"Score:{jugador.score}",font,(255,255,0),600,5)
    #Dibujar items
    grupo_items.draw(ventana)
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



