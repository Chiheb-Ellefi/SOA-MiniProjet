# Corrigé indicatif du TP3

## Code de référence
Projet complet et testé : [`DOS-IDL-TP3/`](DOS-IDL-TP3/)

```
DOS-IDL-TP3/
├── main.py            API complète (3 services, modèles Pydantic v2, erreurs au format commun)
├── test_api.py        11 tests pytest
├── requirements.txt
└── README.md
```

Lancement : `uvicorn main:app --reload` ; documentation : http://127.0.0.1:8000/docs ; tests : `python -m pytest -v`.
Un fichier unique est accepté pour ce TP ; au TP4 le code est réparti en modules.

## Points clés du code
- `erreur(code_http, code, message)` construit l'erreur au format commun `{detail: {code, message}}`.
- `CertificationCreate` : validation automatique (code en majuscules/chiffres, durée > 0, prix ≥ 0, niveau énuméré) → 422 géré par FastAPI.
- Validation **métier** (doublon de code, doublon d'inscription, capacité atteinte) → 409 levé explicitement.
- `GET /menus?date=...` utilise `Query(alias="date")` pour respecter le nom de paramètre du contrat sans masquer le type `date`.

## Résultats attendus
- `GET /certifications?domaine=cloud` : uniquement `AZ900`.
- `GET /certifications/INCONNU` : 404 `NOT_FOUND`.
- `POST /certifications` valide : 201 ; `duree_heures` négative ou code vide : 422 ; code déjà présent : 409 `ALREADY_EXISTS`.
- Séminaire 1 (capacité 2) : même étudiant deux fois → 409 `ALREADY_EXISTS` ; troisième étudiant → 409 `CAPACITY_REACHED`.
- `GET /menus?date=2026-12-05` : 200 ; date sans menu : 404.

Corps JSON d'exemple :
```json
{"code": "CKA", "titre": "Kubernetes Administrator", "domaine": "cloud",
 "niveau": "avance", "duree_heures": 40, "prix_dt": 400}
```
```json
{"etudiant_id": 12}
```

## Points à vérifier pendant la correction
- L'application démarre sans erreur et `/docs` est accessible.
- Routes et méthodes HTTP cohérentes avec le contrat commun.
- Erreurs 404 et 409 au format `{detail: {code, message}}`.
- Les étudiants distinguent **validation automatique** (422) et **validation métier** (409).
- Données fictives.

Point de vigilance : pas d'authentification dans cette version ; un `etudiant_id` fourni par le client n'est pas une preuve d'identité,
et les listes de membres ne sont pas protégées.

## Transition vers le TP4
Le TP4 fait dialoguer l'API avec l'extérieur : API météo publique pour les voyages et service Étudiants de l'Équipe 1, avec tests automatisés et démonstration.
