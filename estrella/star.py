import pygame
from objetoCelestial.celestial_object import CelestialObject

class Star(CelestialObject):

    def __init__(self, image_path, mass, nucleo_status):
        super().__init__(image_path, mass)
        self.nucleo_status = nucleo_status

    def generate_magnetic_field(self, screen):
        if self.nucleo_status == 'Active' and self.mass > 1000:
            width = self.rect.width + 40
            height = self.rect.height + 40
            red_field = pygame.image.load('campo_rojo.png')
            red_field_rasized = pygame.transform.scale(red_field,
                                                        (width,
                                                         height))
            red_field_rasized_rect = red_field_rasized.get_rect()
            red_field_rasized_rect.centerx = self.rect.centerx
            red_field_rasized_rect.centery = self.rect.centery
            screen.blit(red_field_rasized, red_field_rasized_rect)