from typing import Dict, Any

def _verify_valid_stats(stats: Dict[str, Any]):
     """Helper function to verify stats output.
     Verifies that the stats objects contains min and max
     and that they are of the correct types.
     """
     assert set(stats.keys()) == {"min", "max"}
     assert type(stats["min"]) is float, int
     assert type(stats["max"]) is float, int

def test_stats_get(client):
     """This unit test checks the endpoint: `GET /api/games/<int:game_id>/stats`"""
     r = client.get("/api/games/1/stats")
 
     # Get the list of games should always succeed, i.e. HTTP 200 OK
     assert r.status_code == 200
 
     # Response type should be JSON
     assert r.mimetype == "application/json"
 
     # JSON should be parsable as a dict
     assert isinstance(r.json, dict)
 
     # Verify stats format
     _verify_valid_stats(r.json)

def test_stats_wrong_method(client):
    """This unit test checks the endpoint: `POST /api/games/<int:game_id>/stats`
    This method is not allowed by our API server (only GET)
    therefore this request should fail on 
    """
    r = client.post("/api/games/1/stats")

    # Expected response is HTTP 405 Method Not Allowed
    assert r.status_code == 405