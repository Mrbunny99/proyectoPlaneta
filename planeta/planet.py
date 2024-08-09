import pygame
from objetoCelestial.celestial_object import CelestialObject

class Planet(CelestialObject):

    def __init__(self, image_path, distance, orbit_speed, mass, nucleo_status):
        super().__init__(image_path = image_path, distance = distance, orbit_speed = orbit_speed, mass = mass)
        self.nucleo_status = nucleo_status

    def generate_magnetic_field(self, screen):
        if self.nucleo_status == 'Active' and self.mass > 200:
            width = self.rect.width + 20
            height = self.rect.height + 20
            blue_field = pygame.image.load('campo_azul.png')
            blue_field_rasized = pygame.transform.scale(blue_field,
                                                        (width,
                                                         height))
            blue_field_rasized_rect = blue_field_rasized.get_rect()
            blue_field_rasized_rect.centerx = self.rect.centerx
            blue_field_rasized_rect.centery = self.rect.centery
            screen.blit(blue_field_rasized, blue_field_rasized_rect)