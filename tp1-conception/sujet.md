# TP1 — Analyse et conception d'une application orientée services

**Module :** DOS — **Public :** CS, 1 ING, 2 ING, 2 IDL, 3 IDL — **Durée :** 3 heures — **Organisation :** trinôme
**Outils :** diagrams.net, PlantUML ou équivalent — **Projet :** DOS-IDL-Campus (voir `docs/mp3-cahier-des-charges.md`)

## Contexte
Une application orientée services s'organise autour de services indépendants, chacun ayant une responsabilité métier précise
et une interface définie. Dans ce TP, vous analysez et concevez DOS-IDL-Campus. La réalisation du code n'est pas demandée.

## Prérequis
- Notions de programmation et de génie logiciel.
- Notions de client, serveur, requête, réponse.
- Notions élémentaires de diagrammes UML.

## Objectifs pédagogiques
1. Analyser un besoin et identifier les acteurs.
2. Distinguer fonctionnalité, opération et service.
3. Définir les responsabilités de trois services.
4. Représenter une architecture orientée services.
5. Représenter un scénario par un diagramme de séquence, erreurs comprises.
6. Définir le contrat conceptuel d'une opération.
7. Identifier les dépendances avec les services d'autres équipes.

## Travail demandé

**Exercice 1 — Analyse des besoins (25 min).** Identifiez au moins quatre acteurs, leurs besoins et une exigence fonctionnelle associée.
Identifiez deux exigences non fonctionnelles (sécurité, disponibilité, maintenabilité…). Choisissez deux fonctionnalités indispensables
et une fonctionnalité pour une version ultérieure. Présentez le résultat dans un tableau Acteur / Besoin / Exigence.

**Exercice 2 — Identification des services (30 min).** Pour les trois services (Certifications et Séminaires, Clubs, Restauration et Voyages),
précisez la responsabilité, puis définissez au moins trois opérations par service avec : nom, entrées, résultat, consommateur potentiel.

**Exercice 3 — Architecture (30 min).** Réalisez un diagramme d'architecture montrant les consommateurs, l'interface, les trois services,
les données et **les services externes** (service Étudiants de l'Équipe 1, service météo). Répondez ensuite :
1. Quelle différence entre consommateur et fournisseur de service ?
2. Pourquoi séparer les responsabilités en plusieurs services ?
3. Comment une application Web et une application mobile réutilisent-elles le même service ?
4. Quel inconvénient présenterait un service unique regroupant tout ?

**Exercice 4 — Diagramme de séquence (35 min).** Scénario : un étudiant consulte la liste des séminaires, sélectionne un séminaire, puis s'y inscrit.
Le diagramme montre l'étudiant, l'application, le Service Certifications et Séminaires, la vérification de l'étudiant auprès du service Étudiants
de l'Équipe 1, la confirmation, et **deux situations d'erreur** (séminaire complet, étudiant inconnu).

**Exercice 5 — Contrat d'un service (25 min).** Choisissez une opération de l'exercice 2 et décrivez son contrat : nom, objectif, entrées et types,
résultat et type, erreurs possibles, règles d'autorisation.

**Exercice 6 — Synthèse et backlog (15 min).** Synthèse de 8 à 10 lignes (architecture, responsabilités, avantages, rôle des contrats, technologies prévues),
puis six user stories pour le backlog Scrum.

## Livrables
1. Tableau d'analyse des besoins.
2. Tableau des services et opérations.
3. Diagramme d'architecture.
4. Diagramme de séquence UML avec les erreurs.
5. Contrat conceptuel d'une opération.
6. Synthèse de 8 à 10 lignes et backlog de six user stories.

## Barème indicatif

| Critère | Points |
|---|---|
| Analyse des besoins | 20 |
| Identification des services | 25 |
| Architecture orientée services | 20 |
| Diagramme de séquence | 15 |
| Contrat de service | 15 |
| Qualité de la présentation | 5 |
| **Total** | **100** |

## Organisation des trois heures

| Activité | Durée |
|---|---|
| Introduction et lecture du sujet | 15 min |
| Exercice 1 | 25 min |
| Exercice 2 | 30 min |
| Exercice 3 | 30 min |
| Exercice 4 | 35 min |
| Exercice 5 | 25 min |
| Exercice 6 | 15 min |
| Vérification et dépôt | 5 min |
| **Total** | **180 min** |
