# Planning, méthodologie agile et validations

## Méthodologie
- Scrum léger, un Scrum Master dans l'équipe ; un sprint = une semaine ; présentation d'avancement de 30 minutes par semaine.
- Le Scrum Master de l'Équipe 6 coordonne avec les chefs de projet des autres équipes et avec l'Équipe 5 (intégration et gestion de projet agile).
- Public cible des TPs : CS, 1 ING, 2 ING, 2 IDL, 3 IDL, département GLSI.

| Public | Utilisation recommandée |
|---|---|
| CS, 1 ING | TP1 et TP3 (versions guidées, sans les exercices « avancé ») |
| 2 ING, 2 IDL | TP1 à TP4 avec le corrigé en appui |
| 3 IDL, GLSI | TP1 à TP4 complets plus extensions (intégration inter-équipes, agilité) |

## Modèle de présentation hebdomadaire (30 minutes)

| Partie | Durée | Contenu |
|---|---|---|
| Objectif du sprint | 3 min | Ce qui était prévu |
| Réalisé | 10 min | Démonstration courte (service, API, test) |
| Intégration | 7 min | Contrats validés ou en attente avec les autres équipes |
| Difficultés et risques | 5 min | Blocages, dépendances |
| Prochain sprint | 5 min | Éléments du backlog retenus |

## Plan sur 12 semaines (4 phases du planning de la classe)

| Phase | Semaines | Livrable de l'équipe |
|---|---|---|
| Phase 1 | 1 à 3 | Périmètre validé avec les Équipes 1, 5, 8 ; contrat d'API commun ; TP1 rédigé |
| Phase 2 | 4 à 6 | TP2 (SOAP Java) et TP3 (API REST) rédigés et testés |
| Phase 3 | 7 à 9 | TP4 : intégration, tests, mode simulé ; corrigés complétés |
| Phase 4 | 10 à 12 | Dépôt GitHub finalisé, essai pilote, formation de 12 h, démonstration finale |

## Répartition par semaine et par personne (proposition)

| Semaine | Chiheb | Ibtihel | Membre 3 |
|---|---|---|---|
| 1 | Périmètre + contrat API commun | Analyse des besoins | Réunion Éq. 1/5/8 + backlog |
| 2 | Diagramme d'architecture | Services + opérations | Diagramme de séquence |
| 3 | Contrat OpenAPI | TP1 sujet + corrigé | Validation + présentation |
| 4 | TP2 : projet Maven + modèle | TP3 : setup FastAPI | TP2 sujet |
| 5 | TP2 : WSDL + tests SoapUI | Routes Certifications + Séminaires | Routes Clubs |
| 6 | TP2 corrigé | Routes Restauration + Voyages | TP3 sujet + corrigé |
| 7 | Client météo + mode simulé | Client service Étudiants (Éq. 1) | Tests pytest |
| 8 | Route météo | Contrôle étudiant dans les inscriptions | Tableau de tests |
| 9 | Intégration avec Éq. 5 | TP4 sujet + corrigé | README + corrections |
| 10 | Dépôt GitHub final | Relecture croisée des TPs | Essai pilote avec un groupe |
| 11 | Week-end 1 : TP1 + TP2 | Week-end 1 : TP1 + TP2 | Corrections après retours |
| 12 | Week-end 2 : TP3 + TP4 | Week-end 2 : TP3 + TP4 | Démo finale + bilan |

Chaque semaine : « Présentation d'avancement » (30 min). Les semaines 11 et 12 sont à ajuster aux dates des deux week-ends.

## Checklist de l'essai pilote (semaine 10)
- Un groupe test suit un TP complet sans aide, chronomètre en main.
- Relever les exercices dont la durée est mal estimée, les ambiguïtés de l'énoncé et les erreurs du corrigé.
- Vérifier que le code du corrigé s'exécute sur un poste de laboratoire neuf (JDK 17, Python 3.10+).
- Corriger les documents avant les week-ends de formation.

## Points à valider avec l'enseignant et les autres équipes
1. La répartition clubs / événements / certifications avec les Équipes 1 et 8.
2. La route et l'URL du service Étudiants de l'Équipe 1.
3. Le format de la passerelle d'intégration de l'Équipe 5.
4. Les dates des deux week-ends de formation.
5. Le format Chercheur (article IEEE) en complément, si souhaité.
