# TP3 — Développement d'une API REST avec Python et FastAPI

**Module :** DOS — **Durée :** 3 heures — **Organisation :** trinôme
**Technologies :** Python 3.10+, FastAPI, Pydantic v2, Uvicorn, OpenAPI — **Projet :** DOS-IDL-Campus, API REST des trois services

## Contexte
Le TP2 a utilisé SOAP et un contrat WSDL. Ce TP introduit l'approche REST : les ressources sont exposées par des URL, manipulées par les
méthodes HTTP et échangées en JSON. Vous développez l'API REST de DOS-IDL-Campus avec FastAPI. Les données restent en mémoire.

## Prérequis
- Python : fonctions, listes, dictionnaires, modules.
- Notions de HTTP, d'URL et de JSON.
- Contrat d'API commun (`docs/mp3-cahier-des-charges.md`) et conception du TP1.

Environnement : Python 3.10+, `pip`, environnement virtuel, FastAPI et Uvicorn, un navigateur ou Postman.

## Objectifs pédagogiques
1. Expliquer les principes d'une API REST et distinguer GET, POST, PUT, DELETE.
2. Développer une API FastAPI couvrant plusieurs services.
3. Valider les entrées avec Pydantic.
4. Utiliser les codes HTTP (200, 201, 404, 409, 422).
5. Appliquer le format d'erreur commun.
6. Explorer la documentation OpenAPI générée (`/docs`).

## Travail demandé

**Exercice 1 — Préparation de l'environnement (20 min).**
```
python -m venv .venv
.venv\Scripts\activate          (Windows)
source .venv/bin/activate       (Linux/macOS)
python -m pip install fastapi "uvicorn[standard]"
```
Créez le dossier `DOS-IDL-TP3` et `main.py`, démarrez avec `uvicorn main:app --reload` et vérifiez l'accès dans le navigateur.

**Exercice 2 — Première API (25 min).** `GET /` (message de bienvenue), `GET /health` (état), `GET /about` (projet et technologie), en JSON.

**Exercice 3 — Consultation des ressources (35 min).**
- `GET /certifications` avec filtres facultatifs `domaine` et `niveau` ;
- `GET /certifications/{code}` avec 404 si le code n'existe pas ;
- `GET /seminaires` et `GET /clubs` (filtre `domaine`) ;
- `GET /voyages` et `GET /menus?date=AAAA-MM-JJ`.

**Exercice 4 — Validation et création (30 min).**
- `POST /certifications` : code obligatoire (majuscules et chiffres), titre obligatoire, durée strictement positive, prix positif ou nul, niveau dans une liste ; code existant refusé (409) ;
- `POST /clubs` : nom unique ;
- `POST /clubs/{id}/adhesions` et `POST /seminaires/{id}/inscriptions` *(avancé)* : refuser doublons et dépassements de capacité (409).

Testez une requête valide et au moins deux requêtes invalides.

**Exercice 5 — Documentation et tests (30 min).** Ouvrez `/docs`, testez avec « Try it out », consultez `/openapi.json`, puis complétez :

| Requête | Résultat attendu | Résultat observé |
|---|---|---|
| Lister les certifications | 200 | À compléter |
| Consulter `PCEP` | 200 | À compléter |
| Consulter un code absent | 404 | À compléter |
| Créer une certification valide | 201 | À compléter |
| Créer avec `duree_heures` négative | 422 | À compléter |
| Créer un code déjà existant | 409 | À compléter |
| Inscrire deux fois le même étudiant | 409 | À compléter |

**Exercice 6 — Synthèse (20 min).** 8 à 10 lignes : différence SOAP/REST, rôle de JSON, intérêt de FastAPI et de Pydantic, apport d'OpenAPI,
consommation par une application mobile, améliorations avant un déploiement réel.

## Livrables
1. Sources Python et `requirements.txt`.
2. Routes fonctionnelles et modèles Pydantic.
3. Résultats d'au moins cinq tests.
4. Capture ou extrait de `/docs`.
5. Tableau de tests complété.
6. Synthèse de comparaison SOAP/REST.

## Barème indicatif

| Critère | Points |
|---|---|
| Préparation de l'environnement | 10 |
| Routes et consultation | 25 |
| Validation et création | 25 |
| Tests et codes HTTP | 20 |
| Documentation OpenAPI | 10 |
| Synthèse et qualité | 10 |
| **Total** | **100** |

## Organisation des trois heures

| Activité | Durée |
|---|---|
| Présentation et installation | 20 min |
| Exercice 2 | 25 min |
| Exercice 3 | 35 min |
| Exercice 4 | 30 min |
| Exercice 5 | 30 min |
| Exercice 6 | 20 min |
| Vérification et dépôt | 20 min |
| **Total** | **180 min** |
