from typing import List, Dict, Optional
import crafterlib

class CraftingService:
    @staticmethod
    def get_items_for_game(game_data: crafterlib.GameCraftingData) -> List[Dict]:
        return [item.to_dict() for item in game_data.items]
    
    @staticmethod
    def get_recipes_for_item(game_data: crafterlib.GameCraftingData, item_id: int) -> Optional[List[Dict]]:
        item = game_data.get_item_by_id(item_id)
        if not item:
            return None
        
        recipes = game_data.get_recipes_for_item(item.name)
        return [recipe.to_dict() for recipe in recipes]
    
    @staticmethod
    def calculate_ingredients(game_data: crafterlib.GameCraftingData, item_id: int, quantity: float = 1.0) -> Optional[Dict]:
        item = game_data.get_item_by_id(item_id)
        if not item:
            return None
        
        recipes = game_data.get_recipes_for_item(item.name)
        if not recipes:
            return {"ingredients": {}}
        
        # Use the first available recipe
        recipe = recipes[0]
        amount_of_product = recipe.products[item.name]
        
        ingredients = {}
        for ingredient, amount in recipe.ingredients.items():
            ingredients[ingredient] = amount * quantity / amount_of_product
        
        return {"ingredients": ingredients}