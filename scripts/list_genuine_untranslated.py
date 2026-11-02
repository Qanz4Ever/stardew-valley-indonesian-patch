import os
import re
import json

with open('D:/Stardew_ID_Project/untranslated_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

skip_files = {
    'Data/ChairTiles.json',
    'Data/AquariumFish.json',
    'Data/CookingRecipes.json',
    'Data/CraftingRecipes.json',
    'Data/animationDescriptions.json'
}

genuine_untranslated = {}
for rel, missing in report.items():
    if rel in skip_files:
        continue
    genuine_untranslated[rel] = missing

total_keys = sum(len(v) for v in genuine_untranslated.values())
print(f"Total genuine text files: {len(genuine_untranslated)}")
print(f"Total genuine untranslated keys: {total_keys}\n")

with open('D:/Stardew_ID_Project/genuine_untranslated.json', 'w', encoding='utf-8') as out:
    json.dump(genuine_untranslated, out, indent=2, ensure_ascii=False)

for rel, missing in sorted(genuine_untranslated.items()):
    print(f"=== {rel} ({len(missing)} keys) ===")
    for k, v in missing.items():
        val_str = str(v).replace('\n', '\\n')
        print(f"  {k}: {val_str}")
