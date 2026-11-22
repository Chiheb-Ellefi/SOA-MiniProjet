from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_lister_certifications():
    r = client.get("/certifications")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_filtre_domaine():
    r = client.get("/certifications?domaine=cloud")
    assert [c["code"] for c in r.json()] == ["AZ900"]


def test_certification_inexistante():
    r = client.get("/certifications/INCONNU")
    assert r.status_code == 404
    assert r.json()["detail"]["code"] == "NOT_FOUND"


def test_creation_valide():
    r = client.post("/certifications", json={
        "code": "CKA", "titre": "Kubernetes Administrator", "domaine": "cloud",
        "niveau": "avance", "duree_heures": 40, "prix_dt": 400})
    assert r.status_code == 201


def test_creation_invalide():
    r = client.post("/certifications", json={
        "code": "TST1", "titre": "Test", "domaine": "cloud",
        "niveau": "debutant", "duree_heures": -5, "prix_dt": 10})
    assert r.status_code == 422


def test_doublon():
    corps = {"code": "DUP1", "titre": "Doublon", "domaine": "cloud",
             "niveau": "debutant", "duree_heures": 10, "prix_dt": 10}
    assert client.post("/certifications", json=corps).status_code == 201
    assert client.post("/certifications", json=corps).status_code == 409


def test_capacite_seminaire():
    assert client.post("/seminaires/1/inscriptions", json={"etudiant_id": 10}).status_code == 201
    assert client.post("/seminaires/1/inscriptions", json={"etudiant_id": 10}).status_code == 409
    assert client.post("/seminaires/1/inscriptions", json={"etudiant_id": 11}).status_code == 201
    r = client.post("/seminaires/1/inscriptions", json={"etudiant_id": 12})
    assert r.status_code == 409
    assert r.json()["detail"]["code"] == "CAPACITY_REACHED"


def test_clubs():
    assert client.post("/clubs/1/adhesions", json={"etudiant_id": 5}).status_code == 201
    assert client.get("/clubs/1/membres").json() == [5]
    assert client.get("/clubs/99/membres").status_code == 404


def test_menu_et_reservation():
    assert client.get("/menus?date=2026-12-05").status_code == 200
    assert client.get("/menus?date=2026-01-01").status_code == 404
    corps = {"etudiant_id": 3, "date": "2026-12-05", "creneau": "midi"}
    assert client.post("/reservations-repas", json=corps).status_code == 201
    assert client.post("/reservations-repas", json=corps).status_code == 409


def test_voyages():
    assert client.get("/voyages").status_code == 200
    assert client.post("/voyages/1/inscriptions", json={"etudiant_id": 7}).status_code == 201


def test_documentation_openapi():
    r = client.get("/openapi.json")
    assert r.status_code == 200
    assert "paths" in r.json()
