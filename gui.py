import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien  = Alien(ai_settings, screen)
    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        
        gf.update_bullets(bullets)
        
        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        

# Chamando o Objeto do jogo
run_game() 