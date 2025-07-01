from flask import Blueprint, jsonify

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@bp.app_errorhandler(405)
def not_found(error):
    return jsonify({"error": "Method not allowed"}), 405

@bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@bp.app_errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400