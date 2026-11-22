import os

os.environ["MODE_SIMULATION"] = "true"  # avant l'import de l'application

import requests
from fastapi.testclient import TestClient

import client_meteo
from main import app

client = TestClient(app)


def test_lister_certifications():
    reponse = client.get("/certifications")
    assert reponse.status_code == 200
    assert isinstance(reponse.json(), list)


def test_certification_inexistante():
    reponse = client.get("/certifications/INCONNU")
    assert reponse.status_code == 404
    assert reponse.json()["detail"]["code"] == "NOT_FOUND"


def test_creation_invalide():
    reponse = client.post("/certifications", json={
        "code": "TST1", "titre": "Test", "domaine": "cloud",
        "niveau": "debutant", "duree_heures": -5, "prix_dt": 10})
    assert reponse.status_code == 422


def test_doublon_certification():
    corps = {"code": "DUP1", "titre": "Doublon", "domaine": "cloud",
             "niveau": "debutant", "duree_heures": 10, "prix_dt": 10}
    assert client.post("/certifications", json=corps).status_code == 201
    reponse = client.post("/certifications", json=corps)
    assert reponse.status_code == 409


def test_capacite_seminaire():
    # le séminaire 1 a une capacité de 2
    assert client.post("/seminaires/1/inscriptions", json={"etudiant_id": 10}).status_code == 201
    assert client.post("/seminaires/1/inscriptions", json={"etudiant_id": 11}).status_code == 201
    reponse = client.post("/seminaires/1/inscriptions", json={"etudiant_id": 12})
    assert reponse.status_code == 409
    assert reponse.json()["detail"]["code"] == "CAPACITY_REACHED"


def test_etudiant_inconnu():
    reponse = client.post("/seminaires/2/inscriptions", json={"etudiant_id": 999})
    assert reponse.status_code == 422
    assert reponse.json()["detail"]["code"] == "INVALID_STUDENT"


def test_meteo_simulee():
    reponse = client.get("/voyages/1/meteo")
    assert reponse.status_code == 200
    assert reponse.json()["meteo"]["mode"] == "simule"


def test_meteo_delai_depasse(monkeypatch):
    def leve_timeout(*args, **kwargs):
        raise requests.Timeout()

    monkeypatch.setattr(client_meteo.requests, "get", leve_timeout)
    reponse = client.get("/voyages/1/meteo?simulation=false")
    assert reponse.status_code == 504
    assert reponse.json()["detail"]["code"] == "EXTERNAL_TIMEOUT"


def test_meteo_reponse_invalide(monkeypatch):
    class FausseReponse:
        def raise_for_status(self):
            pass

        def json(self):
            raise ValueError("pas du JSON")

    monkeypatch.setattr(client_meteo.requests, "get", lambda *a, **k: FausseReponse())
    reponse = client.get("/voyages/1/meteo?simulation=false")
    assert reponse.status_code == 502


def test_documentation_openapi():
    reponse = client.get("/openapi.json")
    assert reponse.status_code == 200
    assert "paths" in reponse.json()
