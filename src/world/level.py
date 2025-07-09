import pygame

class Level:
    def __init__(self):
        self.tile_size = 64
        self.tiles = [
            [1, 1, 1, 1, 1],  # 1 = Parede, 0 = Chão
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]
        ]
        self.wall_color = (100, 100, 100)
        self.floor_color = (200, 200, 200)

    def draw(self, screen):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                rect = pygame.Rect(
                    x * self.tile_size,
                    y * self.tile_size,
                    self.tile_size,
                    self.tile_size
                )
                color = self.wall_color if tile == 1 else self.floor_color
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Borda
