import pygame


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.all_sprites = pygame.sprite.Group()

    def run(self, dt):
        self.display_surface.fill('red')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()
