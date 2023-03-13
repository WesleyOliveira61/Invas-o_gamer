class Settings():
    """Uma classe para armazenar todas as configuração do jogo"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = '#e1e1e2'
        # Configuranção da espaçonave
        self.ship_speed_factor = 1.5

        # Configuração do da classe bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Configuração dos alienígenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet_direction igual a 1  representa a direita; -1 representa
        #  a esquerda
        self.fleet_direction = 1
