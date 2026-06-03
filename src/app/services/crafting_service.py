from typing import List, Dict, Optional
import crafterlib
import crafterlib.craftutils

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
    
    @staticmethod
    def get_crafting_grids_for_game(game_data: crafterlib.GameCraftingData) -> List[Dict]:
        return [crafting_grid.to_dict() for crafting_grid in game_data.crafting_grids]
    
    @staticmethod
    def calculate_amount_craftable(game_data: crafterlib.GameCraftingData, item_id: int, inventory: Dict[str, float], recursive: bool = False) -> Optional[Dict]:
        # Get item from ID so we can use the item.name
        item = game_data.get_item_by_id(item_id)
        if not item:
            return None

        amount = crafterlib.craftutils.get_amount_craftable_with(game_data=game_data, ingredients=inventory, product=item.name, recursive=recursive)
        return { "item": item.name, "amount craftable": amount}