import pygame
import random
from settings import SPRITES_PATH

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type):
        super().__init__()
        self.enemy_type = enemy_type
        self.load_sprites()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.uniform(1.0, 3.0)
        self.hp = 30
        self.damage = 10

    def load_sprites(self):
        enemy_sprites = {
            "bill": "bill.png",
            "depression": "depression_cloud.png",
            "work": "work_monster.png"
        }
        self.image = pygame.image.load(SPRITES_PATH + enemy_sprites[self.enemy_type]).convert_alpha()

    def update(self, dt, player_rect):
        # Movimento simples: persegue o jogador
        dx = player_rect.centerx - self.rect.centerx
        dy = player_rect.centery - self.rect.centery
        distance = max(1, (dx ** 2 + dy ** 2) ** 0.5)
        self.rect.x += (dx / distance) * self.speed
        self.rect.y += (dy / distance) * self.speed

class Bill(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, "bill")
        self.hp = 40  # Mais resistente

class DepressionCloud(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, "depression")
        self.speed = 1.5  # Mais lento, mas drena HP do jogador com o tempo
