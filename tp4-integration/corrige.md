# Corrigé indicatif du TP4

## Code de référence
Projet complet et testé : [`DOS-IDL-TP4/`](DOS-IDL-TP4/)

```
DOS-IDL-TP4/
├── main.py             API du TP3 + contrôle des étudiants + route météo
├── client_meteo.py     client Open-Meteo, normalisation, mode simulé, exceptions dédiées
├── client_etudiant.py  client du service Étudiants (Équipe 1), mode simulé
├── test_api.py         10 tests pytest, sans Internet
├── requirements.txt
└── README.md           installation, variables d'environnement
```

## Points clés
- `client_meteo.obtenir_meteo` : la requête et la conversion JSON sont dans deux `try` séparés. Dans les versions récentes de `requests`,
  l'erreur de décodage JSON peut aussi être une `RequestException` et serait sinon confondue avec une indisponibilité du fournisseur.
- Hiérarchie d'exceptions : `MeteoTimeout` et `MeteoReponseInvalide` héritent de `MeteoIndisponible` ; la route traduit Timeout → 504, le reste → 502.
- `controler_etudiant` est appelé après la vérification d'existence de la ressource (le 404 passe avant le contrôle de l'étudiant).
- Mode simulé : `MODE_SIMULATION=true` (ou paramètre `?simulation=true` pour la météo). La réponse porte `mode: simule` ou `mode: reel`.
- La route `/etudiants/{id}` du service de l'Équipe 1 reprend la spécification indicative de MP1 ; à confirmer avec cette équipe.

Exemple de réponse en mode simulé :
```json
{
  "voyage_id": 1,
  "destination": "Tozeur",
  "meteo": {"temperature_c": 22.0, "vent_kmh": 10.0, "heure": null,
            "source": "simulation", "mode": "simule"}
}
```

## Réponses attendues aux questions de sécurité
1. **Délai d'attente :** sans lui, un fournisseur lent bloque l'API indéfiniment.
2. **Données confidentielles :** on ne transmet à un tiers que les données nécessaires (ici des coordonnées publiques, jamais de données d'étudiants).
3. **Erreur du client ou indisponibilité du fournisseur :** une requête incorrecte donne un 4xx ; un fournisseur en panne ou trop lent donne 502 ou 504.
4. **Conditions d'utilisation et limites :** une API publique peut limiter le nombre d'appels ou restreindre l'usage commercial.
5. **Mode simulé :** tests prévisibles, reproductibles et indépendants du réseau.
6. **Avant la production :** authentification (JWT/OAuth2), base de données, journalisation, cache de la météo, Docker, passerelle API.

## Critères de réussite
- Fonctionnalités principales accessibles et contrats cohérents avec le code.
- Erreurs attendues (404, 409, 422, 502, 504) gérées au format commun.
- Mode simulé et mode réel distingués dans la réponse.
- Tests rejouables sans Internet.
- README permettant à un autre étudiant de démarrer le projet.
- Étudiants capables d'expliquer leurs choix et les limites de leur solution.
