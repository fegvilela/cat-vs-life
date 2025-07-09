# cat vs life

This is a very simple game about a cat and its tutor, a young woman who's facing a difficult time entering the adult life. 

cat_guardian_game/  
│── assets/               # Sprites, sons, fonts  
│   ├── sprites/          # cat.png, enemies/, etc.  
│   └── audio/            # meow.wav, hiss.wav  
│  
│── src/  
│   ├── main.py           # Ponto de entrada  
│   ├── settings.py       # Configurações (cores, FPS, etc.)  
│   │  
│   ├── entities/         # Classes de entidades  
│   │   ├── cat.py        # Classe do gato (jogador)  
│   │   └── enemies.py    # Inimigos (Bill, DepressionCloud, etc.)  
│   │  
│   ├── game_states/      # Gerenciamento de estados (menu, jogo, cutscene)  
│   │   ├── game_state.py # Classe base  
│   │   ├── menu_state.py  
│   │   └── play_state.py  
│   │  
│   ├── utils/            # Ferramentas auxiliares  
│   │   ├── asset_loader.py # Carrega sprites/sons  
│   │   └── collision.py  # Detecção de colisões  
│   │  
│   └── world/            # Mapa, objetos do cenário  
│       ├── level.py      # Gerenciador de fases  
│       └── tile.py       # Tiles do cenário (opcional)  


Separação de Responsabilidades: Cada classe/funcionalidade tem um propósito claro.

Escalável: Fácil adicionar novos estados (menu, pause), inimigos, mecânicas.

Boas Práticas:

Delta time (dt) para movimentos independentes de FPS.

Assets carregados em um único lugar (asset_loader.py).

Quer que eu desenvolva alguma parte específica (ex.: inimigos, cutscene, HUD)? 😊
