import pygame
from entities.cat import Cat
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from world.level import Level
from utils.hud import HUD
from utils.save_manager import SaveManager
from utils.particles import ParticleSystem

class PlayState:
    def __init__(self, game):
        self.game = game
        self.all_sprites = pygame.sprite.Group()
	self.enemies = pygame.sprite.Group()
	self.spawn_timer = 0

	#hud
	self.hud = HUD(self.cat)

	#world
	self.level = Level()
        
        # Cria o gato no centro da tela
        self.cat = Cat(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.all_sprites.add(self.cat)

	#save manager
	self.save_manager = SaveManager()
	
	#particles
	self.particles = ParticleSystem()    

    def handle_events(self, event):
	# No handle_events do PlayState, modifique os ataques:
	if event.key == pygame.K_m:
    		self.cat.attack("meow")
    		check_attack([self.cat], self.enemies)  # Exemplo simplificado
		self.particles.add_particles(self.cat.rect.center, color=(255, 200, 0)) #particles
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

	self.particles.update() #particles
    
    def render(self, screen):
        screen.fill((135, 206, 235))  # Cor de fundo (céu)
        self.all_sprites.draw(screen)
	# No render do PlayState (antes do flip):
	self.particles.draw(screen)
	self.level.draw(screen) #world
	self.hud.draw(screen) #hud

    # Método para salvar (chame quando necessário, ex.: derrota/vitória):
    def save_progress(self):
    	data = {
        "level": 1,  # Exemplo
        "cat_hp": self.cat.hp,
        "enemies_defeated": 5  # Exemplo
   	 }
    	self.save_manager.save_game(data)
