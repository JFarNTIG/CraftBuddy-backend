from typing import Dict, Any

def test_amount_craftable_success(client):
    """GET amountCraftable returns correct crafting result"""

    r = client.get("/api/games/1/items/203/amountCraftable?Sticks=10&Iron%20Ingot=6&recursive=true")

    assert r.status_code == 200
    assert r.mimetype == "application/json"
    assert isinstance(r.json, dict)

    assert "item" in r.json
    assert "amount craftable" in r.json

    assert r.json["item"] == "Iron Pickaxe"
    assert r.json["amount craftable"] == 2

def test_amount_craftable_missing_inventory(client):
    """Should return 400 when no inventory is provided"""

    r = client.get("/api/games/1/items/203/amountCraftable")

    assert r.status_code == 400
    assert r.mimetype == "application/json"
    assert isinstance(r.json, dict)

    assert "error" in r.json
    assert "No inventory provided" in r.json["error"]

def test_amount_craftable_invalid_item(client):
    """Should return 404 when item does not exist"""

    r = client.get(
        "/api/games/1/items/999999/amountCraftable"
        "?Sticks=10&Iron%20Ingot=6"
    )

    assert r.status_code == 404
    assert r.mimetype == "application/json"
    assert isinstance(r.json, dict)

    assert "error" in r.json
    assert r.json["error"] == "Item not found"