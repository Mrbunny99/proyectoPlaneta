from estrella.star import Star
from planeta.planet import Planet
from asteroide.asteroid import Asteroid
import pygame
import logging
from datetime import datetime

#Configuracion del logger
fecha_actual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
logging.basicConfig(filename=f'logs_{fecha_actual}.log',
                    level = logging.INFO,
                    format = '%(asctime)s - %(levelname)s - %(message)s')

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sistema Solar")

sun = Star(image_path="sol.png", mass= 2000, nucleo_status= "Active")
mercury = Planet(image_path="mercurio.png", distance= 100, orbit_speed= 3, mass= 50, nucleo_status= "Inactive")
mars = Planet(image_path="marte.png", distance= 180, orbit_speed= 2, mass= 250, nucleo_status= "Active")
asteroid = Asteroid(image_path="asteroide.png", distance= 210, orbit_speed= 1, mass= 20)

background_image = pygame.image.load("fondo.png").convert()
background_rect = background_image.get_rect()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            logging.info("Cerrando el Sistema Solar")

    screen.blit(background_image, background_rect)
    sun.draw(screen)
    mercury.draw(screen)
    mars.draw(screen)
    asteroid.draw(screen)

    logging.info("Actualizando posiciones de los objetos celestiales")
    
    mercury.generate_magnetic_field(screen)
    mars.generate_magnetic_field(screen)
    sun.generate_magnetic_field(screen)

    sun.update()
    mercury.update()
    mars.update()
    asteroid.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()