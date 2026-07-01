# FLASK Certification Project

Certifikačné cvičenie **Alta3 Research** — dve malé Flask aplikácie na precvičenie
základov Flasku (routing, JSON odpoveď, Jinja2 šablóny).

## Aplikácie

| Súbor | Popis | Endpoint |
|-------|-------|----------|
| `alta3research-flask01.py` | Vráti zoznam `peoples` ako JSON | `GET /` |
| `alta3research-requests02.py` | Vyrenderuje `index.html` so zoznamom ľudí (Jinja2) | `GET /` |

Dáta sú v `static_data.py`, šablóna v `templates/index.html`, štýly v `static/css/style.css`.

## Inštalácia

```bash
# 1. Virtuálne prostredie
python -m venv venv
source venv/Scripts/activate      # Windows (Git Bash)
# source venv/bin/activate        # Linux / macOS

# 2. Závislosti
pip install -r requirements.txt
```

## Spustenie

```bash
# JSON API
python alta3research-flask01.py

# HTML stránka so zoznamom ľudí
python alta3research-requests02.py
```

Appka beží na http://127.0.0.1:5000/

## Štruktúra

```
alta3research-flask01.py      # JSON API
alta3research-requests02.py   # HTML render (Jinja2)
static_data.py                # zdrojové dáta (peoples, messages)
templates/index.html          # Jinja2 šablóna
static/css/style.css          # štýly
```

> Pozn.: Pôvodne bol projekt uložený ako jeden `.zip` (vrátane `venv/`).
> Rozbalený do reálnych súborov, `venv/` a archívy sú teraz v `.gitignore`.
