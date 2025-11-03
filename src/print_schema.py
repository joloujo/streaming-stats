from genson import SchemaBuilder
import json
from pathlib import Path

scrobbles_path = Path("data") / "scrobbles-joloujo-1762202519.json"

scrobbles_file = open(scrobbles_path, 'r', encoding='utf-8')
scrobbles = json.load(scrobbles_file)

builder = SchemaBuilder()
builder.add_object(scrobbles)
schema = builder.to_schema()
print(json.dumps(schema, indent=2))