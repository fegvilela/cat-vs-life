import pygame
import random

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particles(self, x, y, color=(255, 255, 255), count=10):
        for _ in range(count):
            self.particles.append({
                "x": x,
                "y": y,
                "size": random.randint(2, 5),
                "color": color,
                "speed_x": random.uniform(-1, 1),
                "speed_y": random.uniform(-1, 1),
                "life": 30
            })

    def update(self):
        for particle in self.particles[:]:
            particle["x"] += particle["speed_x"]
            particle["y"] += particle["speed_y"]
            particle["life"] -= 1
            if particle["life"] <= 0:
                self.particles.remove(particle)

    def draw(self, screen):
        for particle in self.particles:
            pygame.draw.circle(
                screen,
                particle["color"],
                (int(particle["x"]), int(particle["y"])),
                particle["size"]
            )
