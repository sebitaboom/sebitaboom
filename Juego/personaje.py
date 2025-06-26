import pygame
import parametros as p


class Personaje:
    def __init__(self, x: int, y: int) -> None: 
        #Forma del personaje
        self.forma = pygame.Rect(0, 0, p.ALTO_PERSONAJE, p.ANCHO_PERSONAJE)
        #Donde se va a encontrar
        self.forma.center = (x, y)
        

    def dibujar(self, ventana) -> None:
        pygame.draw.rect(ventana, p.MORADO_RARO, self.forma)
 
    def movimiento(self, delta_x: int, delta_y: int) -> None:
        self.forma.x += delta_x
        self.forma.y += delta_y