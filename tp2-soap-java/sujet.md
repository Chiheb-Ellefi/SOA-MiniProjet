# TP2 — Développement d'un service SOAP en Java avec XML et WSDL

**Module :** DOS — **Durée :** 3 heures — **Organisation :** trinôme
**Technologies :** Java 17, Maven, JAX-WS (Metro), XML, WSDL, SoapUI — **Projet :** DOS-IDL-Campus, Service Certifications

## Contexte
Dans le TP1, vous avez conçu l'application. Ce TP met en œuvre un premier service SOAP en Java : le **Service Certifications**.
SOAP est un protocole d'échange de messages XML ; le WSDL décrit le contrat (opérations, paramètres, messages).
Les données restent en mémoire : aucune base de données n'est exigée.

## Prérequis
- Programmation orientée objet en Java (classes, méthodes, collections).
- Notions de base sur XML et HTTP.
- Architecture orientée services (TP1).

Environnement : JDK 17, Maven, un IDE (IntelliJ IDEA ou Eclipse), SoapUI ou équivalent. Depuis Java 11, JAX-WS n'est plus fourni par le JDK :
les dépendances Jakarta XML Web Services et Metro doivent être déclarées dans le `pom.xml`. Tous les participants utilisent le même JDK
et les mêmes versions de dépendances (à figer avant la séance).

## Objectifs pédagogiques
1. Expliquer le rôle de SOAP, XML et WSDL.
2. Développer et publier un service SOAP en Java.
3. Définir des opérations avec des objets structurés et des erreurs métier.
4. Lire un WSDL : service, opérations, messages, point d'accès.
5. Envoyer des requêtes SOAP et interpréter les réponses, erreurs comprises.
6. Comparer SOAP et REST.

## Travail demandé

**Exercice 1 — Découverte de SOAP, XML et WSDL (20 min).**
1. Définissez SOAP, XML et WSDL.
2. Quelle différence entre une opération métier et un message SOAP ?
3. Rôle du client et rôle du fournisseur.
4. Pourquoi le contrat WSDL est-il utile ?
5. Comparez SOAP et REST : format des messages, description du contrat, cas d'utilisation.

**Exercice 2 — Préparation du projet Maven (25 min).** Créez le projet `DOS-IDL-TP2`. Séparez la classe de service, la classe de publication,
le modèle (`Certification`) et le `pom.xml`. Déclarez les dépendances, puis vérifiez que `mvn compile` réussit avant d'écrire les opérations.

**Exercice 3 — Implémentation du Service Certifications (40 min).** Sur une liste en mémoire :
- `listerCertifications` : retourne toutes les certifications ;
- `consulterCertification(code)` : retourne une certification, ou une erreur métier si elle n'existe pas ;
- `rechercherParDomaine(domaine)` : retourne les certifications d'un domaine (liste vide si aucune) ;
- `reserverPlaceSeminaire(idSeminaire, matricule)` *(avancé)* : message de confirmation, avec contrôle des paramètres.

Documentez chaque opération par un commentaire.

**Exercice 4 — Publication et découverte du WSDL (25 min).** Publiez le service sur `http://localhost:8080/services/certifications`,
démarrez-le, ouvrez `?wsdl` et repérez : le nom du service, les opérations, les messages d'entrée et de sortie, le point d'accès.
Livrable : l'URL et un extrait annoté.

**Exercice 5 — Tests SOAP (35 min).** Avec SoapUI, créez un projet depuis le WSDL et complétez :

| Test | Entrée | Résultat attendu | Résultat observé |
|---|---|---|---|
| Lister les certifications | Aucune | Liste de 4 certifications | À compléter |
| Consultation valide | code `PCEP` | Détail de la certification | À compléter |
| Consultation invalide | code `XXX` | Fault contrôlée | À compléter |
| Recherche par domaine | `cloud` | Liste filtrée | À compléter |

**Exercice 6 — Bilan et préparation du TP3 (15 min).** Synthèse de 8 à 10 lignes : rôle du service, fonction du WSDL,
communication client-service, difficultés rencontrées, différences anticipées avec REST.

## Livrables
1. Projet Maven et sources Java.
2. `pom.xml`.
3. WSDL accessible à l'adresse locale (ou fichier exporté).
4. Requêtes et réponses SOAP de trois tests minimum.
5. Tableau de tests complété.
6. Synthèse technique.

## Barème indicatif

| Critère | Points |
|---|---|
| Compréhension de SOAP, XML, WSDL | 15 |
| Configuration et compilation | 15 |
| Implémentation des opérations | 30 |
| Publication et lecture du WSDL | 15 |
| Tests et analyse | 20 |
| Qualité du livrable | 5 |
| **Total** | **100** |

## Organisation des trois heures

| Activité | Durée |
|---|---|
| Introduction et installation | 15 min |
| Exercice 1 | 20 min |
| Exercice 2 | 25 min |
| Exercice 3 | 40 min |
| Exercice 4 | 25 min |
| Exercice 5 | 35 min |
| Exercice 6 | 15 min |
| Vérification et dépôt | 5 min |
| **Total** | **180 min** |
