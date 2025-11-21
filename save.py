import json
import os
from typing import Optional, Tuple
from model import GameModel

saveFile = "savegame.json"

def saveGame(game: GameModel) -> bool:
    # Simpan state game ke file JSON
    try:
        data = {
            'grid': game.board.grid,
            'score': game.board.score,
            'bestScore': game.bestScore,
            'moves': game.moves
        }
        
        with open(saveFile, 'w') as f:
            json.dump(data, f, indent=2)
        
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        return False

def loadGame() -> Optional[GameModel]:
    # Load game state dari file JSON
    try:
        if not os.path.exists(saveFile):
            return None
            
        with open(saveFile, 'r') as f:
            data = json.load(f)
        
        # Bikin game baru terus isi datanya dari file
        game = GameModel()
        game.board.grid = data['grid']
        game.board.score = data['score']
        game.bestScore = data['bestScore']
        game.moves = data['moves']
        
        return game
    except Exception as e:
        print(f"Error loading game: {e}")
        return None

def hasSavedGame() -> bool:
    # Cek ada saved game gak
    return os.path.exists(saveFile)
