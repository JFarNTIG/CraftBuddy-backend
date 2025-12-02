from typing import Dict, Any

def test_crafting_grids_get(client):
    """This unit test checks the endpoint: `GET api/games/<int:game_id>/craftingGrid`"""
    r = client.get("/api/games/1/craftingGrid")

    # Get the list of crafting_grids should always succeed, i.e. HTTP 200 OK
    assert r.status_code == 200

    # Response type should be JSON
    assert r.mimetype == "application/json"

    # JSON should be parsable as a list
    assert isinstance(r.json, list)

    # 
    assert { "id": 1,
            "products": {"Furnace": 1},
            "crafting_coordinates": {
                "A1": "Cobblestone",
                "A2": "Cobblestone",
                "A3": "Cobblestone",
                "B1": "Cobblestone",
                "B2": "",
                "B3": "Cobblestone",
                "C1": "Cobblestone",
                "C2": "Cobblestone",
                "C3": "Cobblestone"
            }
            } in r.json

def test_crafting_grids_by_item_id_get_(client):
    """This unit test checks the endpoint: `GET api/games/<int:game_id>/items/<int:item_id>/craftingGrid`"""
    r = client.get("/api/games/1/items/2/craftingGrid")

    # Get the list of crafting_grids should always succeed, i.e. HTTP 200 OK
    assert r.status_code == 200

    # Response type should be JSON
    assert r.mimetype == "application/json"

    # JSON should be parsable as a list
    assert isinstance(r.json, list)

    # Assert that the correct crafting grid is displayed
    assert r.get_json() ==  [ 
            {
                "id": 2,
                "products": {
                    "Crafting Table": 1
                },
                "crafting_coordinates": {
                    "A1": "",
                    "A2": "",
                    "A3": "",
                    "B1": "Planks",
                    "B2": "Planks",
                    "B3": "",
                    "C1": "Planks",
                    "C2": "Planks",
                    "C3": ""
                }
            }]