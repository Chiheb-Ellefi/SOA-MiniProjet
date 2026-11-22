# TP4 — Intégration : API externe, services des autres équipes, tests et démonstration

**Module :** DOS — **Durée :** 3 heures — **Organisation :** trinôme
**Technologies :** Python, `requests`, FastAPI, JSON, OpenAPI, `pytest` — **Projet :** DOS-IDL-Campus, version intégrée

## Contexte
Une application orientée services consomme aussi d'autres services. L'API du TP3 dialogue avec deux fournisseurs :
- une **API météo publique** (Open-Meteo, sans clé) pour la météo de la destination d'un voyage ;
- le **service Étudiants de l'Équipe 1** pour vérifier qu'un `etudiant_id` existe avant une inscription.

Chaque appel externe prévoit un **mode simulé** pour rester testable sans Internet et sans attendre l'autre équipe.
Le TP se termine par les tests automatisés, le README et la préparation de la démonstration.

## Prérequis
- API FastAPI du TP3 fonctionnelle.
- Requêtes HTTP, JSON, gestion des exceptions en Python.
- Environnement virtuel actif.

Installation : `python -m pip install requests fastapi "uvicorn[standard]" pytest httpx`

## Objectifs pédagogiques
1. Expliquer le rôle d'une API externe dans une architecture orientée services.
2. Envoyer une requête HTTP avec délai d'attente et traiter la réponse JSON.
3. Gérer erreurs HTTP, erreurs réseau, délais dépassés et réponses invalides.
4. Normaliser des données externes dans un format interne cohérent.
5. Intégrer un service d'une autre équipe en respectant son contrat.
6. Prévoir un mode simulé et le distinguer du mode réel dans les réponses.
7. Écrire des tests automatisés reproductibles, sans Internet.
8. Préparer une démonstration et documenter le projet.

## Travail demandé

**Exercice 1 — Découverte de l'API externe (15 min).**
1. Différence entre API locale et API externe ? Identifiez fournisseur, consommateur et données échangées.
2. Consultez la documentation Open-Meteo (`https://open-meteo.com/en/docs`) et vérifiez ses conditions d'utilisation.
3. Ouvrez : `https://api.open-meteo.com/v1/forecast?latitude=33.92&longitude=8.13&current_weather=true`.
4. Repérez les champs température, vitesse du vent, heure.
5. Pourquoi les champs d'une API externe doivent-ils être vérifiés avant utilisation ?

**Exercice 2 — Client HTTP avec gestion des erreurs (30 min).** Créez `client_meteo.py` : requête GET avec délai d'attente, vérification du statut,
conversion en objet Python. Traitez au minimum : réponse valide, statut HTTP en erreur, délai dépassé, réponse non JSON.

**Exercice 3 — Normalisation (20 min).** Fonction `normaliser` produisant `{temperature_c, vent_kmh, heure, source, mode}`, qui gère les champs manquants
et ne suppose pas une structure toujours identique.

**Exercice 4 — Intégration FastAPI (35 min).** Ajoutez `GET /voyages/{id}/meteo` :
1. Retrouver le voyage (404 sinon).
2. Appeler le client météo.
3. Renvoyer un JSON cohérent avec le champ `mode` (`reel` ou `simule`).
4. Traduire les erreurs : 504 `EXTERNAL_TIMEOUT` (délai dépassé), 502 `EXTERNAL_UNAVAILABLE` sinon.
5. Ne jamais exposer les détails techniques d'une exception.

**Exercice 5 — Service Étudiants de l'Équipe 1 (30 min).** Créez `client_etudiant.py` avec `verifier_etudiant(etudiant_id)`. Utilisez-la avant toute inscription
(séminaire, club, voyage) : étudiant inconnu → 422 `INVALID_STUDENT`, service indisponible → 502 `EXTERNAL_UNAVAILABLE`. En mode simulé, les `etudiant_id`
de 1 à 100 existent. Confirmez avec l'Équipe 1 la route réelle et l'URL (variable `STUDENT_API_URL`).

**Exercice 6 — Tests automatisés (35 min).** `test_api.py` avec au moins six tests exécutables par `python -m pytest -v`, sans Internet : liste, ressource inexistante,
données invalides (422), doublon (409), capacité atteinte, étudiant inconnu, météo simulée, météo en délai dépassé. Complétez :

| ID | Scénario | Résultat attendu | Résultat observé | Statut |
|---|---|---|---|---|
| T01 | Lister les certifications | 200 | À compléter | À compléter |
| T02 | Certification inexistante | 404 | À compléter | À compléter |
| T03 | Création invalide | 422 | À compléter | À compléter |
| T04 | Code en doublon | 409 | À compléter | À compléter |
| T05 | Séminaire complet | 409 `CAPACITY_REACHED` | À compléter | À compléter |
| T06 | Étudiant inconnu | 422 `INVALID_STUDENT` | À compléter | À compléter |
| T07 | Météo en mode simulé | 200, `mode: simule` | À compléter | À compléter |
| T08 | Météo en délai dépassé | 504 | À compléter | À compléter |

**Exercice 7 — README, démonstration et bilan (15 min).** Rédigez le `README.md` (installation, lancement, tests, variables d'environnement),
préparez la démonstration (`docs/mp3-cahier-des-charges.md`) et une synthèse de 8 à 10 lignes : fonctionnalités réalisées, tests, difficultés, limites connues,
améliorations (authentification, base de données, Docker).

## Livrables
1. `main.py`, `client_meteo.py`, `client_etudiant.py`.
2. `requirements.txt` et `README.md`.
3. `test_api.py` et résultat de `python -m pytest -v`.
4. Tableau de tests complété.
5. Exemple de réponse JSON normalisée (mode réel et mode simulé).
6. Extrait de `/docs`.
7. Synthèse sur la fiabilité, la sécurité et la réutilisation des API, avec les limites connues.

## Barème indicatif

| Critère | Points |
|---|---|
| Compréhension de l'API externe | 10 |
| Appel HTTP et traitement JSON | 15 |
| Normalisation et mode simulé | 15 |
| Intégration FastAPI et inter-équipes | 20 |
| Gestion des erreurs | 10 |
| Tests automatisés | 15 |
| README, documentation et démonstration | 15 |
| **Total** | **100** |

## Organisation des trois heures

| Activité | Durée |
|---|---|
| Exercice 1 | 15 min |
| Exercice 2 | 30 min |
| Exercice 3 | 20 min |
| Exercice 4 | 35 min |
| Exercice 5 | 30 min |
| Exercice 6 | 35 min |
| Exercice 7 | 15 min |
| **Total** | **180 min** |
