# Corrigé indicatif du TP1

Ce corrigé est une proposition. Plusieurs conceptions sont acceptables si les responsabilités sont cohérentes,
les échanges bien représentés et les choix justifiés.

## Exercice 1 — Analyse des besoins

| Acteur | Besoin | Exigence fonctionnelle |
|---|---|---|
| Étudiant | Trouver une certification adaptée | Lister et filtrer les certifications par domaine et niveau |
| Étudiant | S'inscrire à un séminaire | Enregistrer une inscription si une place est disponible |
| Étudiant | Rejoindre un club | Enregistrer une adhésion sans doublon |
| Responsable de formation continue | Publier une offre | Ajouter une certification ou un séminaire avec validation |
| Responsable de club | Connaître ses membres | Lister les membres d'un club |
| Responsable de la restauration | Publier le menu | Créer le menu d'un jour |
| Responsable des voyages | Organiser un voyage | Créer un voyage et suivre les places |

Exigences non fonctionnelles possibles :
- **Interopérabilité :** les échanges respectent le contrat d'API commun (JSON, ISO 8601, format d'erreur).
- **Disponibilité dégradée :** si un service externe est indisponible, l'application reste utilisable grâce au mode simulé ou à une erreur contrôlée.
- **Confidentialité :** seules des données fictives sont stockées ; la liste des membres n'est visible que du responsable du club.

Fonctionnalités indispensables : inscription à un séminaire, adhésion à un club. Fonctionnalité ultérieure : paiement simulé d'un voyage.

## Exercice 2 — Services et opérations

| Service | Opération | Entrées | Résultat attendu | Consommateur |
|---|---|---|---|---|
| Certifications et Séminaires | listerCertifications | domaine, niveau (facultatifs) | Liste de certifications | Application étudiante |
| Certifications et Séminaires | consulterCertification | code | Détail d'une certification | Application étudiante |
| Certifications et Séminaires | inscrireSeminaire | id du séminaire, etudiant_id | Confirmation d'inscription | Application étudiante |
| Clubs | listerClubs | domaine (facultatif) | Liste de clubs | Application étudiante |
| Clubs | adhererClub | id du club, etudiant_id | Confirmation d'adhésion | Application étudiante |
| Clubs | listerMembres | id du club | Liste d'etudiant_id | Responsable de club, Équipe 8 |
| Restauration et Voyages | consulterMenu | date | Menu du jour | Application étudiante |
| Restauration et Voyages | inscrireVoyage | id du voyage, etudiant_id | Confirmation d'inscription | Application étudiante |
| Restauration et Voyages | consulterMeteo | id du voyage | Température et vent à destination | Application étudiante |

Une **fonctionnalité** est un besoin (« s'inscrire à un séminaire »), une **opération** est un appel précis (`inscrireSeminaire`),
un **service** regroupe des opérations cohérentes.

## Exercice 3 — Architecture

Une architecture correcte distingue quatre couches : les consommateurs (web, mobile), l'interface des services (API REST FastAPI),
les trois services métier avec leurs données, et les systèmes externes (service Étudiants de l'Équipe 1, API météo).

1. Le **consommateur** demande une opération ; le **fournisseur** l'exécute et applique les règles métier. Un même composant peut jouer les deux rôles :
   notre API est fournisseur pour l'application étudiante et consommatrice du service météo.
2. Séparer les responsabilités améliore la réutilisation, la testabilité et la maintenabilité, et permet à plusieurs équipes de travailler en parallèle.
3. Les deux applications appellent la même interface en respectant le contrat et les règles d'accès ; aucune logique métier n'est dupliquée.
4. Un service unique devient difficile à maintenir, à tester et à faire évoluer. La séparation doit cependant rester raisonnable : trop de services augmentent la complexité.

## Exercice 4 — Diagramme de séquence

Voir `diagrammes/sequence-inscription-seminaire.puml` (PlantUML). Points de vigilance : tous les appels et réponses sont représentés,
les deux erreurs sont distinctes et le code HTTP de chaque cas est indiqué.

## Exercice 5 — Contrat de l'opération inscrireSeminaire

| Élément | Proposition |
|---|---|
| Nom | inscrireSeminaire |
| Objectif | Inscrire un étudiant à un séminaire s'il reste une place |
| Entrées | `id` du séminaire (entier, dans l'URL), `etudiant_id` (entier, dans le corps JSON) |
| Résultat | `{seminaire_id, etudiant_id, statut: "confirmee"}`, code 201 |
| Erreurs | 404 séminaire inconnu ; 409 `ALREADY_EXISTS` ; 409 `CAPACITY_REACHED` ; 422 `INVALID_STUDENT` ; 502 service Étudiants indisponible |
| Autorisation | Un étudiant ne peut inscrire que lui-même (vérification d'identité hors périmètre en version pédagogique) |

## Exercice 6 — Synthèse et backlog

*Synthèse :* L'application est organisée en trois services (Certifications et Séminaires, Clubs, Restauration et Voyages) exposés par une API REST.
Chaque service a une responsabilité claire et des contrats explicites : routes, paramètres, résultats et erreurs. Les consommateurs (web, mobile)
dépendent de l'interface et non de l'implémentation. Cette séparation facilite la réutilisation, les tests et le travail en parallèle entre équipes.
Les services externes (Étudiants, météo) sont isolés derrière des clients dédiés avec un mode simulé. Nous utiliserons Java pour un composant SOAP (TP2)
puis Python et FastAPI pour l'API principale (TP3 et TP4).

Backlog : voir `../scrum/backlog.md`.
