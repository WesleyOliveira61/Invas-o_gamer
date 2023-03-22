class Settings():
    """Uma classe para armazenar todas as configuração do jogo"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = '#e1e1e2'
      
        # Configurações da espacionave
        self.ship_limit = 3

        # Configuração do da classe bullet
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Configuração dos alienígenas        
        self.fleet_drop_speed = 10

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initializa as configurações que mudam no decorrer do jogo."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # Fleet_direction igual a 1 representa a direita; -1 representa a 
        # esquerda
        self.fleet_direction = 1

      