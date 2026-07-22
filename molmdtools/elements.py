import json
from pathlib import Path

path = Path(__file__).parent / "data" / "elements.json"

with open(path, 'w', encoding='utf-8') as f:
    ATOM_MASSES = json.load(f)