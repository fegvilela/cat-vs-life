import pygame
from settings import SPRITES_PATH

class Cat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(SPRITES_PATH + "cat.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.hp = 100
        
        # Ataques
        self.attacks = {
            "meow": {"damage": 10, "cooldown": 1.0},
            "scratch": {"damage": 20, "cooldown": 2.0},
            "hiss": {"damage": 5, "cooldown": 0.5}
        }
    
    def update(self, dt):
        # Movimento (exemplo com WASD)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
    
    def attack(self, attack_type):
        if attack_type in self.attacks:
            print(f"Cat used {attack_type}! Damage: {self.attacks[attack_type]['damage']}")
            # Lógica de cooldown/dano aqui
