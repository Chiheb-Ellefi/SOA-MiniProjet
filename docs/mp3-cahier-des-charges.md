# MP3 — Cahier des charges : DOS-IDL-Campus

Module DOS — 3 IDL — Travail en trinôme — Technologies : Python, FastAPI, JSON, OpenAPI, pytest ; complément Java/SOAP/WSDL.

## 1. Périmètre de l'Équipe 6

Les cinq thèmes attribués sont regroupés en **trois services métier**.

| Service | Thèmes | Responsabilité |
|---|---|---|
| Certifications et Séminaires | Certifications de formations, séminaires | Catalogue, séminaires, inscriptions aux sessions |
| Clubs | Clubs | Catalogue des clubs, adhésions, membres |
| Restauration et Voyages | Restaurant, voyages | Menus, réservations de repas, voyages d'études, inscriptions, météo |

### Frontières à valider avec les autres équipes (proposition)

| Sujet | Équipe 6 | Équipe 8 / Équipe 1 |
|---|---|---|
| Clubs | Catalogue, adhésions, membres | Équipe 8 : événements des clubs (référence un `club_id` fourni par notre API) |
| Événements | Séminaires de formation uniquement | Équipe 1 : calendrier général des événements de l'ISI |
| Certifications | Catalogue de certifications et inscriptions | Équipe 8 : à préciser (attestations, certificats délivrés) |

## 2. Contrat d'API commun (conventions inter-équipes)

À confirmer avec l'Équipe 5 (intégration).

| Sujet | Convention |
|---|---|
| Format d'échange | JSON (REST) ; XML/SOAP uniquement pour le composant du TP2 |
| Noms des routes | Minuscules, pluriel, en français : `/clubs`, `/certifications`, `/voyages` |
| Identifiants | Entiers pour les entités (`id`), chaîne pour les codes métier (`code`) |
| Référence à un étudiant | Champ `etudiant_id` (entier), fourni par le service Étudiants de l'Équipe 1 |
| Dates et heures | ISO 8601 : `2026-12-05`, `2026-12-05T09:00:00` |
| Codes HTTP | 200, 201, 400, 404, 409, 422, 502, 504 |
| Format des erreurs | Objet `detail` contenant `code` et `message` |
| Documentation | OpenAPI générée par FastAPI, sur `/docs` |
| Mode simulé | Variable d'environnement `MODE_SIMULATION=true` pour tout appel externe |
| Données | Fictives uniquement |

```json
{
  "detail": {
    "code": "NOT_FOUND",
    "message": "Certification introuvable"
  }
}
```

Codes d'erreur métier : `NOT_FOUND`, `ALREADY_EXISTS`, `CAPACITY_REACHED`, `INVALID_STUDENT`, `EXTERNAL_UNAVAILABLE`, `EXTERNAL_TIMEOUT`.

## 3. Cahier des charges

### Contexte
L'ISI souhaite centraliser les services de vie étudiante et de formation complémentaire : certifications professionnelles,
séminaires, clubs, restauration et voyages d'études, aujourd'hui dispersés entre affichages, tableurs et messages.
Le projet consiste à concevoir, développer et tester une application orientée services qui les expose par des interfaces documentées.

### Acteurs
- **Étudiant** : consulte, s'inscrit, adhère.
- **Responsable de formation continue** : gère certifications et séminaires.
- **Responsable de club** : gère son club, consulte les adhésions.
- **Responsable de la restauration** : publie les menus, consulte les réservations.
- **Responsable des voyages** : crée les voyages, suit les inscriptions.
- **Système externe** : service météo (Open-Meteo) et service Étudiants de l'Équipe 1, pouvant être indisponibles.

### Périmètre fonctionnel minimal
**Certifications et Séminaires** : consulter et filtrer les certifications (domaine, niveau) ; ajouter une certification avec validation ;
consulter les séminaires et s'y inscrire (capacité limitée, pas de doublon).
**Clubs** : lister (filtre domaine), créer un club, adhérer, consulter les membres.
**Restauration et Voyages** : consulter le menu d'un jour, réserver un repas ; consulter les voyages, s'y inscrire (places limitées) ;
consulter la météo de la destination (API externe avec mode simulé).
**Extensions facultatives** : paiement simulé, notifications (Équipe 5), statistiques de participation, recommandations fondées sur des critères explicites.

### Routes REST

| Méthode | Route | Fonction |
|---|---|---|
| GET | `/certifications` | Lister (filtres `domaine`, `niveau`) |
| GET | `/certifications/{code}` | Consulter |
| POST | `/certifications` | Ajouter |
| GET | `/seminaires` | Lister |
| POST | `/seminaires/{id}/inscriptions` | S'inscrire |
| GET | `/clubs` | Lister (filtre `domaine`) |
| POST | `/clubs` | Créer |
| POST | `/clubs/{id}/adhesions` | Adhérer |
| GET | `/clubs/{id}/membres` | Lister les membres |
| GET | `/menus?date=2026-12-05` | Menu d'un jour |
| POST | `/reservations-repas` | Réserver un repas |
| GET | `/voyages` | Lister |
| POST | `/voyages/{id}/inscriptions` | S'inscrire |
| GET | `/voyages/{id}/meteo` | Météo de la destination (API externe) |

### Modèle de données minimal
- **Certification** : `code` (unique), `titre`, `organisme` (facultatif), `domaine`, `niveau` (debutant, intermediaire, avance), `duree_heures` (> 0), `prix_dt` (≥ 0).
- **Séminaire** : `id`, `titre`, `intervenant`, `date`, `salle`, `capacite` (> 0), `inscrits`.
- **Club** : `id`, `nom` (unique), `domaine`, `responsable`, `membres`.
- **Menu** : `date`, `plats` (`nom`, `prix_dt`, `allergenes`).
- **Réservation de repas** : `id`, `etudiant_id`, `date`, `creneau` (midi, soir).
- **Voyage** : `id`, `destination`, `latitude`, `longitude`, `date_depart`, `prix_dt`, `places`, `inscrits`.

### Tests et critères de validation

| Test | Résultat attendu |
|---|---|
| Lister les certifications | 200, liste JSON |
| Certification inexistante | 404 `NOT_FOUND` |
| Certification avec durée négative | 422 |
| Certification avec code existant | 409 |
| Séminaire complet | 409 `CAPACITY_REACHED` |
| Double inscription | 409 `ALREADY_EXISTS` |
| Météo en mode simulé | 200, `mode: simule` |
| Météo en délai dépassé | 504 `EXTERNAL_TIMEOUT` |
| Consulter `/docs` | Documentation accessible |

### Scénario de démonstration finale
1. Lancer l'API et ouvrir `/docs`.
2. Lister les certifications, filtrer par domaine.
3. Ajouter une certification valide, puis tenter un doublon.
4. Inscrire un étudiant à un séminaire, puis provoquer le refus pour capacité atteinte.
5. Faire adhérer un étudiant à un club et lister les membres.
6. Consulter un menu et les voyages.
7. Afficher la météo d'un voyage en mode réel puis simulé.
8. Lancer `python -m pytest -v`.
9. Présenter le service SOAP du TP2 et son rôle.

### Évaluation indicative

| Critère | Points |
|---|---|
| Analyse et conception | 15 |
| Décomposition en services et contrats | 15 |
| API REST | 20 |
| Composant SOAP (XML/WSDL) | 10 |
| Intégration externe et inter-équipes | 10 |
| Tests et validation | 15 |
| Documentation et qualité du code | 10 |
| Démonstration et compréhension individuelle | 5 |
| **Total** | **100** |
