import pygame
from settings import ASSETS_PATH

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "meow": pygame.mixer.Sound(ASSETS_PATH + "audio/meow.wav"),
            "scratch": pygame.mixer.Sound(ASSETS_PATH + "audio/scratch.wav"),
            "hiss": pygame.mixer.Sound(ASSETS_PATH + "audio/hiss.wav"),
            "hit": pygame.mixer.Sound(ASSETS_PATH + "audio/hit.wav")
        }
        self.music = pygame.mixer.music.load(ASSETS_PATH + "audio/background.mp3")

    def play_sound(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()

    def play_music(self, loop=True):
        pygame.mixer.music.play(-1 if loop else 0)
