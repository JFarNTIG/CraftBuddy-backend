from flask import Blueprint, jsonify, request
from app.services.game_service import GameService
from app.services.crafting_service import CraftingService

bp = Blueprint('items', __name__)

@bp.route('/games/<int:game_id>/items', methods=['GET'])
def list_game_items(game_id: int):
    game_data = GameService.load_game_data(game_id)
    if not game_data:
        return jsonify({"error": "Game not found or failed to load data"}), 404
    
    items = CraftingService.get_items_for_game(game_data)
    return jsonify(items)

@bp.route('/games/<int:game_id>/items/<int:item_id>/recipes', methods=['GET'])
def recipes_for_item(game_id: int, item_id: int):
    game_data = GameService.load_game_data(game_id)
    if not game_data:
        return jsonify({"error": "Game not found or failed to load data"}), 404
    
    recipes = CraftingService.get_recipes_for_item(game_data, item_id)
    if recipes is None:
        return jsonify({"error": "Item not found"}), 404
    
    return jsonify(recipes)

@bp.route('/games/<int:game_id>/items/<int:item_id>/ingredients', methods=['GET'])
def ingredients_for_item(game_id: int, item_id: int):
    # Parse query parameters
    quantity = request.args.get('quantity', 1, type=float)
    
    game_data = GameService.load_game_data(game_id)
    if not game_data:
        return jsonify({"error": "Game not found or failed to load data"}), 404
    
    result = CraftingService.calculate_ingredients(game_data, item_id, quantity)
    if result is None:
        return jsonify({"error": "Item not found"}), 404
    
    return jsonify(result)