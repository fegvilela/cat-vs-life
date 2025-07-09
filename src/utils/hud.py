import pygame
from settings import WHITE, RED, BLACK

class HUD:
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.Font(None, 36)
        self.health_bar_width = 200
        self.health_bar_height = 20

    def draw(self, screen):
        # Health Bar
        health_ratio = self.player.hp / 100
        pygame.draw.rect(screen, RED, (10, 10, self.health_bar_width * health_ratio, self.health_bar_height))
        pygame.draw.rect(screen, WHITE, (10, 10, self.health_bar_width, self.health_bar_height), 2)

        # Texto (HP e Inimigos Restantes)
        health_text = self.font.render(f"HP: {int(self.player.hp)}", True, WHITE)
        screen.blit(health_text, (10, 40))
