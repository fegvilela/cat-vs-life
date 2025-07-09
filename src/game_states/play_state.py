import pygame
from entities.cat import Cat
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class PlayState:
    def __init__(self, game):
        self.game = game
        self.all_sprites = pygame.sprite.Group()
	self.enemies = pygame.sprite.Group()
	self.spawn_timer = 0
        
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
	self.spawn_timer += dt
	if self.spawn_timer >= 5.0:  # Spawn a cada 5 segundos
    		enemy_type = random.choice(["bill", "depression", "work"])
    		x = random.randint(0, SCREEN_WIDTH)
    		y = random.randint(0, SCREEN_HEIGHT)
    		if enemy_type == "bill":
       		 self.enemies.add(Bill(x, y))
    		elif enemy_type == "depression":
       			 self.enemies.add(DepressionCloud(x, y))
    		self.spawn_timer = 0

	self.enemies.update(dt, self.cat.rect)  # Atualiza inimigos
    
    def render(self, screen):
        screen.fill((135, 206, 235))  # Cor de fundo (céu)
        self.all_sprites.draw(screen)
