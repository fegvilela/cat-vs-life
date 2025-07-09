import json
import os

class SaveManager:
    def __init__(self, save_path="saves/game_save.json"):
        self.save_path = save_path
        os.makedirs("saves", exist_ok=True)

    def save_game(self, data):
        with open(self.save_path, "w") as f:
            json.dump(data, f)

    def load_game(self):
        try:
            with open(self.save_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return None  # Nenhum save encontrado
