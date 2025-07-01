from typing import Dict, Any

def _verify_valid_game_entry(game_entry: Dict[str, Any]):
    """Helper function to verify a game entry.
    Verifies that the game entry object contains id, name and url
    and that they are of the correct types.
    """
    assert ["id", "name", "url"] == list(game_entry.keys())
    assert type(game_entry["id"]) is int
    assert type(game_entry["name"]) is str
    assert type(game_entry["url"]) is str

def test_games_get(client):
    """This unit test checks the endpoint: `GET /api/games`"""
    r = client.get("/api/games")

    # Get the list of games should always succeed, i.e. HTTP 200 OK
    assert r.status_code == 200

    # Response type should be JSON
    assert r.mimetype == "application/json"

    # JSON should be parsable as a list
    assert isinstance(r.json, list)

    # Minecraft was the first game supported, so at the very least
    # it should be present in the output data.
    assert { "id": 1, "name": "Minecraft", "url": "minecraft" } in r.json

    # Verify that all game entries in the output have the expected format.
    for game_entry in r.json:
        _verify_valid_game_entry(game_entry)

def test_games_wrong_method(client):
    """This unit test checks the endpoint: `POST /api/games`
    This method is not allowed by our API server (only GET)
    therefore this request should fail on 
    """
    r = client.post("/api/games")

    # Expected response is HTTP 405 Method Not Allowed
    assert r.status_code == 405