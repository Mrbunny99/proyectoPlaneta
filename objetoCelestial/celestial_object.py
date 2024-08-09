import pygame
import logging
import math
from abc import ABC, abstractmethod

class CelestialObject(ABC):

    def __init__(self, image_path, mass, distance=0, orbit_speed=0):
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.distance = distance
        self._orbit_speed = 0
        self.mass = mass

        self.orbit_speed = orbit_speed
        logging.info(f'Objeto Celestial creado: {self.__class__.__name__} con masa {self.mass}')

    @property
    def orbit_speed(self):
        return self._orbit_speed
    
    @orbit_speed.setter
    def orbit_speed(self, value):
        if value >= 1 and value <= 10:
            self._orbit_speed = value
            logging.info(f'Orbita establecida: {self._orbit_speed}')
        else:
            logging.error('Error en el valor de la orbita')
            return ValueError('Orbit value error')

    def update(self):
        self.angle += self.orbit_speed
        logging.info(f'Actualizando angulo: {self.angle}')

    def draw(self, screen):
        x = (screen.get_width() // 2) + (self.distance * math.cos(math.radians(self.angle)))
        y = (screen.get_height() // 2) + (self.distance * math.sin(math.radians(self.angle)))
        self.rect.centerx = x
        self.rect.centery = y
        screen.blit(self.image, self.rect)
        logging.info(f'Dibujando {self.__class__.__name__} en posicion ({x}, {y})')

    @abstractmethod
    def generate_magnetic_field(self, screen):
        pass