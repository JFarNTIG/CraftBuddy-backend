from typing import Dict, Optional

class GameModel:
    _games = {
        1: {
            "id": 1,
            "name": "Minecraft",
            "url": "minecraft"
        }
    }
    
    @classmethod
    def get_all(cls) -> list:
        return list(cls._games.values())
    
    @classmethod
    def get_by_id(cls, game_id: int) -> Optional[Dict]:
        return cls._games.get(game_id)
    
    @classmethod
    def add_game(cls, game_data: Dict) -> Dict:
        new_id = max(cls._games.keys()) + 1 if cls._games else 1
        game_data['id'] = new_id
        cls._games[new_id] = game_data
        return game_data