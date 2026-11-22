# DOS-IDL-TP2 — Service SOAP des certifications (Java)

Prérequis : JDK 17, Maven. Port 8080 libre.

```
mvn compile
mvn exec:java
```

WSDL : http://localhost:8080/services/certifications?wsdl

Tests : importer le WSDL dans SoapUI ; un exemple de requête est fourni dans
`requete-consulterCertification.xml` (code `PCEP` valide, code `XXX` -> Fault SOAP).

Note : ce composant Java n'a pas pu être compilé dans l'environnement de génération du dépôt
(pas d'accès à Maven Central). Vérifier `mvn compile` et figer les versions des dépendances
avant la séance.
