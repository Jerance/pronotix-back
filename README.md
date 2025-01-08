# pronotix-back

## Venv

```bash
python -m venv .venv
```

## Activate venv

```bash
# mac 
source .venv/bin/activate

# windows
.venv\scripts\activate
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
