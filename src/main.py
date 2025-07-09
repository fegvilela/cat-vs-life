import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game_states.play_state import PlayState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cat Guardian")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Gerenciador de estados (inicia com o estado de jogo)
        self.current_state = PlayState(self)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # Delta time em segundos
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.current_state.handle_events(event)
            
            # Update e render
            self.current_state.update(dt)
            self.current_state.render(self.screen)
            
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
