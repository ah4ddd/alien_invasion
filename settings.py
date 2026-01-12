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
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        pass


