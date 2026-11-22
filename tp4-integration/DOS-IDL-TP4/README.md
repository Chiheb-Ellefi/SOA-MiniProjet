# DOS-IDL-TP4 — API REST DOS-IDL-Campus (FastAPI)

Prérequis : Python 3.10+.

```
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Documentation interactive : http://127.0.0.1:8000/docs

Tests (sans Internet) :

```
python -m pytest -v
```

## Variables d'environnement

| Variable | Rôle | Défaut |
|---|---|---|
| `MODE_SIMULATION` | `true` : météo et service Étudiants simulés (étudiants 1 à 100 existent) | `false` |
| `STUDENT_API_URL` | URL du service Étudiants de l'Équipe 1 | `http://localhost:8001` |

Exemple : `MODE_SIMULATION=true uvicorn main:app --reload`
(Windows PowerShell : `$env:MODE_SIMULATION="true"; uvicorn main:app --reload`)

La météo réelle utilise l'API publique Open-Meteo (sans clé) : vérifier ses conditions d'utilisation.
