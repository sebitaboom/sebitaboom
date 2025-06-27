import pygame
import parametros as p 
from math import degrees, atan2
from personaje import Personaje


class Weapon:
    def __init__(self, imagen_arma: pygame.image) -> None:
        self.imagen_original= imagen_arma
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()

    def update(self, personaje: Personaje) -> None:
        #centrando el arma en el centro del personaje
        self.forma.center = personaje.forma.center

        #Hace que el arma siga la dirección del jugador
        if not personaje.flip:
            self.forma.x += personaje.forma.width * p.ESCALA_X
            self.forma.y += personaje.forma.height * p.ESCALA_Y
            self.rotar_arma(False)

        else:         
            self.forma.x -= personaje.forma.width * p.ESCALA_X
            self.forma.y += personaje.forma.height * p.ESCALA_Y
            self.rotar_arma(True)

        #Mover el rifle siguiendo el mouse
        mouse_posicion = pygame.mouse.get_pos()
        distancia_x = mouse_posicion[0] - self.forma.centerx
        distancia_y = -(mouse_posicion[1] - self.forma.centery)
        self.angulo = degrees(atan2(distancia_y, distancia_x))

        #DEFINIR MAX Y MIN (TAREA)
        print((self.angulo))

    def rotar_arma(self, rotar: bool) -> None:
        if rotar:
            imagen_flip = pygame.transform.flip(self.imagen_original, True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original, False, False) 
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
             
    def dibujar(self, ventana) -> None:
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)


        ventana.blit(self.imagen, self.forma)
        #pygame.draw.rect(ventana, p.COLOR_ARMA, self.forma, width = 1)

