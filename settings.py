class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (245, 245, 220)
        #ship
        self.ship_speed = 5
        self.ship_limit = 3
        #bullets
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (231, 84, 128)
        self.bullets_allowed = 300
        #alien
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        #level up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.bullet_speed = 5
        self.alien_speed = 2

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
