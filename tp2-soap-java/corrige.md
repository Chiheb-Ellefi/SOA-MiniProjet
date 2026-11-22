# Corrigé indicatif du TP2

## Code de référence
Projet Maven complet : [`DOS-IDL-TP2/`](DOS-IDL-TP2/)

```
DOS-IDL-TP2/
├── pom.xml
├── requete-consulterCertification.xml
└── src/main/java/tn/idl/campus/
    ├── Certification.java                      modèle (constructeur vide + accesseurs)
    ├── CertificationIntrouvableException.java  erreur métier (@WebFault)
    ├── ServiceCertifications.java              service (@WebService, 4 opérations)
    └── Main.java                               publication (Endpoint.publish)
```

Lancement : `mvn compile` puis `mvn exec:java` ; WSDL sur `http://localhost:8080/services/certifications?wsdl`.

**Statut :** ce code n'a pas été compilé dans l'environnement de génération. Les versions (`jakarta.xml.ws-api` 4.0.2,
`jaxws-rt` 4.0.3, `jakarta.jws-api` 3.0.0) doivent être vérifiées et figées avant la séance.

## Réponses de l'exercice 1
1. **SOAP** : protocole d'échange de messages structurés en XML. **XML** : format de données balisé. **WSDL** : description XML du contrat du service.
2. Une **opération métier** est une fonction offerte (`consulterCertification`) ; un **message SOAP** est l'enveloppe XML qui transporte l'appel ou la réponse.
3. Le client formule la requête ; le fournisseur exécute le traitement et répond.
4. Le WSDL permet de connaître opérations, types et point d'accès, et de générer automatiquement des clients.
5. SOAP : XML, contrat WSDL formel, adapté aux échanges d'entreprise strictement typés ; REST : JSON le plus souvent, contrat OpenAPI facultatif, adapté aux applications web et mobiles.

## Exercice 4 — Éléments à repérer dans le WSDL
Nom du service `ServiceCertifications`, espace de noms `http://campus.idl.tn/certifications`, les quatre opérations dans le `portType`,
les messages d'entrée et de sortie, la `Fault` `CertificationIntrouvable`, et l'adresse du point d'accès dans l'élément `service`.

## Exercice 5 — Exemple de requête
Voir `DOS-IDL-TP2/requete-consulterCertification.xml`. Avec le code `PCEP`, la réponse contient code, titre, domaine, niveau, durée et prix.
Avec `XXX`, la réponse est un `Fault` SOAP portant le message « Certification introuvable : XXX ».

## Points de vigilance
- Mélange d'annotations `javax.*` et de dépendances `jakarta.*` : utiliser uniquement `jakarta.*`.
- Dépendances JAX-WS absentes du `pom.xml`, port déjà occupé, URL du WSDL incorrecte.
- Classe modèle sans constructeur vide ou sans accesseurs : la sérialisation XML échoue.
- Si la `Fault` pose problème dans un environnement donné, retourner un objet de réponse contenant un champ `erreur` et le documenter.
- Le matricule simulé n'est pas une authentification : en production, l'identité et les droits seraient vérifiés avant de retourner des données.
- Une capture d'écran ne suffit pas comme preuve : les tests doivent être reproductibles.

## Transition vers le TP3
Le TP2 a utilisé SOAP, XML et un contrat WSDL. Le TP3 introduit REST avec Python, FastAPI et JSON ; les deux approches seront comparées.
