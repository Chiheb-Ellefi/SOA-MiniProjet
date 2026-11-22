import os

import requests


class ServiceEtudiantIndisponible(Exception):
    """Le service Étudiants (Équipe 1) ne répond pas correctement."""


def verifier_etudiant(etudiant_id: int, simulation: bool | None = None,
                      timeout: float = 3) -> bool:
    if simulation is None:
        simulation = os.getenv("MODE_SIMULATION", "false").lower() == "true"
    if simulation:
        return 1 <= etudiant_id <= 100  # étudiants fictifs simulés
    base = os.getenv("STUDENT_API_URL", "http://localhost:8001")
    try:
        reponse = requests.get(f"{base}/etudiants/{etudiant_id}", timeout=timeout)
    except requests.RequestException as exc:
        raise ServiceEtudiantIndisponible("Service Étudiants injoignable") from exc
    if reponse.status_code == 200:
        return True
    if reponse.status_code == 404:
        return False
    raise ServiceEtudiantIndisponible(f"Statut inattendu : {reponse.status_code}")
