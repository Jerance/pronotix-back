# pronotix-back

## Venv

```bash
python -m venv .venv
```

## Activate venv

```bash
source .venv/bin/activate
```

## Installation

```bash
pip install -r requirements.txt
```

## Freeze

```bash
pip freeze > requirements.txt
```

## Run with uvicorn

```bash
uvicorn app.main:app --reload
```
