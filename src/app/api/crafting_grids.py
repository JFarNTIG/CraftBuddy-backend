from flask import Blueprint, jsonify, request
from app.services.game_service import GameService
from app.services.crafting_service import CraftingService

bp = Blueprint('crafting_grids', __name__)

# Endpoints for the crafting grid feature

# Endpoint that displays all the crafting grids
@bp.route('/games/<int:game_id>/craftingGrid', methods=['GET'])
def list_game_crafting_grids(game_id: int):
    game_data = GameService.load_game_data(game_id)
    if not game_data:
        return jsonify({"error": "Game not found or failed to load data"}), 404
    
    crafting_grids = CraftingService.get_crafting_grids_for_game(game_data)
    
    return jsonify(crafting_grids)

# Endpoint that displays the crafting grid based on what the product is
@bp.route('/games/<int:game_id>/items/<int:item_id>/craftingGrid', methods=['GET'])
def recipes_for_item(game_id: int, item_id: int):
    game_data = GameService.load_game_data(game_id)
    crafting_grids = CraftingService.get_crafting_grids_for_game(game_data)
    if not game_data:
        return jsonify({"error": "Game not found or failed to load data"}), 404
    
    recipes = CraftingService.get_recipes_for_item(game_data, item_id)
    if recipes is None:
        return jsonify({"error": "Item not found"}), 404
    
    products = []
    for recipe in recipes:
        products.append(recipe["products"]) 
    
    final_list = []
    for product in products:
        for crafting_grid in crafting_grids:
            if crafting_grid["products"] == product:
                final_list.append(crafting_grid)
    
    return jsonify(final_list)