import pygame
from entities.cat import Cat
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class PlayState:
    def __init__(self, game):
        self.game = game
        self.all_sprites = pygame.sprite.Group()
        
        # Cria o gato no centro da tela
        self.cat = Cat(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.all_sprites.add(self.cat)
    
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m: self.cat.attack("meow")
            if event.key == pygame.K_a: self.cat.attack("scratch")
            if event.key == pygame.K_h: self.cat.attack("hiss")
    
    def update(self, dt):
        self.all_sprites.update(dt)
    
    def render(self, screen):
        screen.fill((135, 206, 235))  # Cor de fundo (céu)
        self.all_sprites.draw(screen)
