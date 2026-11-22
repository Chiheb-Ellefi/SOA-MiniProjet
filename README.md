# DOS-IDL-Campus — Mini-Projet 3 et TPs de formation pratique

**Équipe 6** — Certifications de formations, Clubs, Restauration, Séminaires et Voyages
Module Développement Orienté Service (DOS) — 3 IDL 1 & 2 — ISI — AU 2026/2027
Format : Formateur Ingénieur (TPs + corrigés). Équipe : Chiheb Ellefi, Ibtihel Khemili, [membre 3], [membre 4]

Fil rouge : un mini-projet unique, **DOS-IDL-Campus**, qui regroupe les services de vie étudiante et de
formation complémentaire de l'ISI. Toutes les données sont **fictives**.

## Formation : 4 TPs, 12 heures, deux week-ends

| Journée | TP | Durée | Technologie | Dossier |
|---|---|---|---|---|
| Week-end 1, samedi | TP1 — Analyse et conception orientée services | 3 h | UML, PlantUML | [tp1-conception](tp1-conception/) |
| Week-end 1, dimanche | TP2 — Service SOAP en Java (XML, WSDL) | 3 h | Java 17, Maven, JAX-WS | [tp2-soap-java](tp2-soap-java/) |
| Week-end 2, samedi | TP3 — API REST avec FastAPI | 3 h | Python, FastAPI, Pydantic | [tp3-rest-fastapi](tp3-rest-fastapi/) |
| Week-end 2, dimanche | TP4 — Intégration, API externe, tests | 3 h | requests, pytest | [tp4-integration](tp4-integration/) |

Chaque dossier contient `sujet.md` (énoncé), `corrige.md` (corrigé indicatif) et le code de référence.

## Contenu du dépôt

```
dos-idl-campus/
├── README.md
├── docs/
│   ├── mp3-cahier-des-charges.md     périmètre, contrat d'API commun, MP3
│   └── planning-et-scrum.md          planning 12 semaines, présentations, validations
├── scrum/backlog.md                  user stories
├── tp1-conception/                   sujet, corrigé, diagrammes PlantUML
├── tp2-soap-java/                    sujet, corrigé, projet Maven DOS-IDL-TP2
├── tp3-rest-fastapi/                 sujet, corrigé, projet DOS-IDL-TP3
└── tp4-integration/                  sujet, corrigé, projet DOS-IDL-TP4
```

## Démarrage rapide

```
cd tp4-integration/DOS-IDL-TP4
python -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
MODE_SIMULATION=true uvicorn main:app --reload     # puis http://127.0.0.1:8000/docs
```

## État de vérification

- Code Python (TP3, TP4) : tests automatisés exécutés avec succès (11 tests pour le TP3, 10 pour le TP4).
- Code Java (TP2) : **non compilé** dans l'environnement de génération ; à vérifier avec `mvn compile` (JDK 17) et à figer
  (versions JAX-WS) avant la séance.
- Appel réel à Open-Meteo : non testé en ligne ; le mode simulé et les erreurs sont testés par simulation.
