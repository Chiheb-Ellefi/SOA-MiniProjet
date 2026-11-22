from datetime import date
from enum import Enum

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="DOS-IDL-Campus API",
    description="API pédagogique : certifications, séminaires, clubs, restauration, voyages",
    version="1.0.0",
)


def erreur(code_http: int, code: str, message: str) -> HTTPException:
    """Erreur au format commun : {detail: {code, message}}."""
    return HTTPException(status_code=code_http, detail={"code": code, "message": message})


# ---------- Modèles ----------
class Niveau(str, Enum):
    debutant = "debutant"
    intermediaire = "intermediaire"
    avance = "avance"


class CertificationCreate(BaseModel):
    code: str = Field(min_length=2, max_length=15, pattern=r"^[A-Z0-9-]+$")
    titre: str = Field(min_length=3, max_length=120)
    organisme: str | None = None
    domaine: str = Field(min_length=2)
    niveau: Niveau
    duree_heures: int = Field(gt=0, le=500)
    prix_dt: float = Field(ge=0)


class ClubCreate(BaseModel):
    nom: str = Field(min_length=2, max_length=60)
    domaine: str = Field(min_length=2)
    responsable: str = Field(min_length=2)


class Participation(BaseModel):
    etudiant_id: int = Field(gt=0)


class Creneau(str, Enum):
    midi = "midi"
    soir = "soir"


class ReservationRepas(BaseModel):
    etudiant_id: int = Field(gt=0)
    date: date
    creneau: Creneau


# ---------- Données fictives en mémoire ----------
certifications = [
    {"code": "PCEP", "titre": "Python Entry-Level Programmer", "organisme": None,
     "domaine": "programmation", "niveau": "debutant", "duree_heures": 30, "prix_dt": 120.0},
    {"code": "AZ900", "titre": "Cloud Fundamentals", "organisme": None,
     "domaine": "cloud", "niveau": "debutant", "duree_heures": 24, "prix_dt": 150.0},
]
seminaires = [
    {"id": 1, "titre": "Introduction à la cybersécurité", "intervenant": "Intervenant A",
     "date": "2026-12-05T09:00:00", "salle": "A104", "capacite": 2, "inscrits": []},
    {"id": 2, "titre": "Agilité et Scrum", "intervenant": "Intervenant B",
     "date": "2026-12-06T09:00:00", "salle": "B201", "capacite": 30, "inscrits": []},
]
clubs = [
    {"id": 1, "nom": "Club Robotique", "domaine": "technique", "responsable": "Responsable 1", "membres": []},
    {"id": 2, "nom": "Club Théâtre", "domaine": "culture", "responsable": "Responsable 2", "membres": []},
]
menus = {
    "2026-12-05": [
        {"nom": "Couscous", "prix_dt": 3.5, "allergenes": ["gluten"]},
        {"nom": "Salade composée", "prix_dt": 2.0, "allergenes": []},
    ]
}
voyages = [
    {"id": 1, "destination": "Tozeur", "latitude": 33.92, "longitude": 8.13,
     "date_depart": "2026-12-20", "prix_dt": 180.0, "places": 40, "inscrits": []},
]
reservations: list[dict] = []


# ---------- Racine ----------
@app.get("/")
def accueil():
    return {"message": "Bienvenue dans DOS-IDL-Campus"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/about")
def about():
    return {"projet": "DOS-IDL-Campus", "technologie": "Python et FastAPI"}


# ---------- Service Certifications et Séminaires ----------
@app.get("/certifications")
def lister_certifications(domaine: str | None = None, niveau: Niveau | None = None):
    resultat = certifications
    if domaine:
        resultat = [c for c in resultat if c["domaine"].lower() == domaine.lower()]
    if niveau:
        resultat = [c for c in resultat if c["niveau"] == niveau.value]
    return resultat


@app.get("/certifications/{code}")
def consulter_certification(code: str):
    for c in certifications:
        if c["code"].lower() == code.lower():
            return c
    raise erreur(status.HTTP_404_NOT_FOUND, "NOT_FOUND", "Certification introuvable")


@app.post("/certifications", status_code=status.HTTP_201_CREATED)
def creer_certification(nouvelle: CertificationCreate):
    if any(c["code"] == nouvelle.code for c in certifications):
        raise erreur(status.HTTP_409_CONFLICT, "ALREADY_EXISTS", "Ce code existe déjà")
    element = nouvelle.model_dump(mode="json")
    certifications.append(element)
    return element


@app.get("/seminaires")
def lister_seminaires():
    return seminaires


@app.post("/seminaires/{seminaire_id}/inscriptions", status_code=status.HTTP_201_CREATED)
def inscrire_seminaire(seminaire_id: int, demande: Participation):
    sem = next((s for s in seminaires if s["id"] == seminaire_id), None)
    if sem is None:
        raise erreur(status.HTTP_404_NOT_FOUND, "NOT_FOUND", "Séminaire introuvable")
    if demande.etudiant_id in sem["inscrits"]:
        raise erreur(status.HTTP_409_CONFLICT, "ALREADY_EXISTS", "Étudiant déjà inscrit")
    if len(sem["inscrits"]) >= sem["capacite"]:
        raise erreur(status.HTTP_409_CONFLICT, "CAPACITY_REACHED", "Séminaire complet")
    sem["inscrits"].append(demande.etudiant_id)
    return {"seminaire_id": seminaire_id, "etudiant_id": demande.etudiant_id, "statut": "confirmee"}


# ---------- Service Clubs ----------
@app.get("/clubs")
def lister_clubs(domaine: str | None = None):
    if domaine is None:
        return clubs
    return [c for c in clubs if c["domaine"].lower() == domaine.lower()]


@app.post("/clubs", status_code=status.HTTP_201_CREATED)
def creer_club(nouveau: ClubCreate):
    if any(c["nom"].lower() == nouveau.nom.lower() for c in clubs):
        raise erreur(status.HTTP_409_CONFLICT, "ALREADY_EXISTS", "Ce club existe déjà")
    element = {"id": max((c["id"] for c in clubs), default=0) + 1,
               **nouveau.model_dump(), "membres": []}
    clubs.append(element)
    return element


@app.post("/clubs/{club_id}/adhesions", status_code=status.HTTP_201_CREATED)
def adherer_club(club_id: int, demande: Participation):
    club = next((c for c in clubs if c["id"] == club_id), None)
    if club is None:
        raise erreur(status.HTTP_404_NOT_FOUND, "NOT_FOUND", "Club introuvable")
    if demande.etudiant_id in club["membres"]:
        raise erreur(status.HTTP_409_CONFLICT, "ALREADY_EXISTS", "Déjà membre")
    club["membres"].append(demande.etudiant_id)
    return {"club_id": club_id, "etudiant_id": demande.etudiant_id, "statut": "membre"}


@app.get("/clubs/{club_id}/membres")
def lister_membres(club_id: int):
    club = next((c for c in clubs if c["id"] == club_id), None)
    if club is None:
        raise erreur(status.HTTP_404_NOT_FOUND, "NOT_FOUND", "Club introuvable")
    return club["membres"]


# ---------- Service Restauration et Voyages ----------
@app.get("/menus")
def consulter_menu(jour: date = Query(alias="date")):
    plats = menus.get(jour.isoformat())
    if plats is None:
        raise erreur(status.HTTP_404_NOT_FOUND, "NOT_FOUND", "Aucun menu pour cette date")
    return {"date": jour.isoformat(), "plats": plats}


@app.post("/reservations-repas", status_code=status.HTTP_201_CREATED)
def reserver_repas(demande: ReservationRepas):
    jour_iso = demande.date.isoformat()
    if jour_iso not in menus:
        raise erreur(status.HTTP_404_NOT_FOUND, "NOT_FOUND", "Aucun menu pour cette date")
    if any(r["etudiant_id"] == demande.etudiant_id and r["date"] == jour_iso
           and r["creneau"] == demande.creneau.value for r in reservations):
        raise erreur(status.HTTP_409_CONFLICT, "ALREADY_EXISTS", "Réservation déjà enregistrée")
    element = {"id": len(reservations) + 1, "etudiant_id": demande.etudiant_id,
               "date": jour_iso, "creneau": demande.creneau.value}
    reservations.append(element)
    return element


@app.get("/voyages")
def lister_voyages():
    return voyages


@app.post("/voyages/{voyage_id}/inscriptions", status_code=status.HTTP_201_CREATED)
def inscrire_voyage(voyage_id: int, demande: Participation):
    voyage = next((v for v in voyages if v["id"] == voyage_id), None)
    if voyage is None:
        raise erreur(status.HTTP_404_NOT_FOUND, "NOT_FOUND", "Voyage introuvable")
    if demande.etudiant_id in voyage["inscrits"]:
        raise erreur(status.HTTP_409_CONFLICT, "ALREADY_EXISTS", "Étudiant déjà inscrit")
    if len(voyage["inscrits"]) >= voyage["places"]:
        raise erreur(status.HTTP_409_CONFLICT, "CAPACITY_REACHED", "Voyage complet")
    voyage["inscrits"].append(demande.etudiant_id)
    return {"voyage_id": voyage_id, "etudiant_id": demande.etudiant_id, "statut": "confirmee"}
