from flask import Blueprint, jsonify
from app.services.game_service import GameService

bp = Blueprint('games', __name__)

@bp.route('/games', methods=['GET'])
def list_games():
    games = GameService.get_all_games()
    return jsonify(games)