import pygame
from game_states.game_state import GameState

class CutsceneState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.dialogue = [
            ("Tutor", "Ugh, adult life is so hard..."),
            ("Cat", "Meow! *purrs*"),
            ("Tutor", "Thanks, little one...")
        ]
        self.current_line = 0
        self.font = pygame.font.Font(None, 36)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.current_line += 1
            if self.current_line >= len(self.dialogue):
                self.game.current_state = PlayState(self.game)  # Transição para o jogo

    def render(self, screen):
        screen.fill((0, 0, 0))
        speaker, text = self.dialogue[self.current_line]
        rendered_text = self.font.render(f"{speaker}: {text}", True, (255, 255, 255))
        screen.blit(rendered_text, (50, 50))
