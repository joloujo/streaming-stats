import json
from pathlib import Path
from scrobbles_types import ScrobblesJSON, Scrobble, Artist, Album, Date

scrobbles_path = Path("data") / "scrobbles-joloujo-1762202519.json"

scrobbles_file = open(scrobbles_path, 'r', encoding='utf-8')
scrobbles_dict: ScrobblesJSON = json.load(scrobbles_file)

scrobbles: list[Scrobble] = [scrobble for page in scrobbles_dict for scrobble in page]

print(len(scrobbles))