class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (27, 59, 98)

        # Настройки корабля
        self.ship_speed = 2.5
        self.ship_limit = 2

        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 200
        self.bullet_height = 4
        self.bullet_color = (255, 255, 255)
        self.bullet_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 5
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1