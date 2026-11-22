import os

import requests

URL_METEO = "https://api.open-meteo.com/v1/forecast"


class MeteoIndisponible(Exception):
    """Fournisseur injoignable ou en erreur."""


class MeteoTimeout(MeteoIndisponible):
    """Délai d'attente dépassé."""


class MeteoReponseInvalide(MeteoIndisponible):
    """Réponse impossible à interpréter."""


def mode_simulation(simulation: bool | None = None) -> bool:
    if simulation is not None:
        return simulation
    return os.getenv("MODE_SIMULATION", "false").lower() == "true"


def normaliser(brut: dict) -> dict:
    """Sélectionne les champs utiles ; tolère les champs manquants."""
    courant = brut.get("current_weather") if isinstance(brut, dict) else None
    if not isinstance(courant, dict):
        raise MeteoReponseInvalide("Champ current_weather absent")
    return {
        "temperature_c": courant.get("temperature"),
        "vent_kmh": courant.get("windspeed"),
        "heure": courant.get("time"),
        "source": "open-meteo",
        "mode": "reel",
    }


def obtenir_meteo(latitude: float, longitude: float,
                  simulation: bool | None = None, timeout: float = 5) -> dict:
    if mode_simulation(simulation):
        return {"temperature_c": 22.0, "vent_kmh": 10.0, "heure": None,
                "source": "simulation", "mode": "simule"}
    try:
        reponse = requests.get(
            URL_METEO,
            params={"latitude": latitude, "longitude": longitude, "current_weather": "true"},
            timeout=timeout,
        )
        reponse.raise_for_status()
    except requests.Timeout as exc:
        raise MeteoTimeout("Délai dépassé") from exc
    except requests.RequestException as exc:
        raise MeteoIndisponible("Fournisseur indisponible") from exc
    try:
        brut = reponse.json()
    except ValueError as exc:
        raise MeteoReponseInvalide("Réponse non JSON") from exc
    return normaliser(brut)
