from typing import Optional, List, Dict
import crafterlib
from app.models.game import GameModel

class GameService:
    @staticmethod
    def get_all_games() -> List[Dict]:
        return GameModel.get_all()
    
    @staticmethod
    def get_game(game_id: int) -> Optional[Dict]:
        return GameModel.get_by_id(game_id)
    
    @staticmethod
    def load_game_data(game_id: int) -> Optional[crafterlib.GameCraftingData]:
        game = GameModel.get_by_id(game_id)
        if not game:
            return None
        
        try:
            return crafterlib.load_data_for_game(game["url"])
        except Exception:
            return None