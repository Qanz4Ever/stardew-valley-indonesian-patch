import os
import re
import json

def clean_json_comments(text):
    pattern = r'("(?:\\.|[^"\\])*")|(/\*[\s\S]*?\*/|//[^\r\n]*)'
    regex = re.compile(pattern)
    
    def replace(match):
        if match.group(2):
            return ""
        return match.group(1)
        
    cleaned = regex.sub(replace, text)
    cleaned = re.sub(r',\s*([\]}])', r'\1', cleaned)
    return cleaned

def load_jsonc(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    cleaned = clean_json_comments(content)
    return json.loads(cleaned)

def build_mod_map(mod_dir):
    mod_map = {}
    for root, dirs, files in os.walk(mod_dir):
        for f in files:
            if not f.endswith('.json'):
                continue
            full_p = os.path.join(root, f)
            rel = os.path.relpath(full_p, mod_dir).replace('\\', '/')
            
            if '_Indonesia.json' in rel:
                canonical = rel.replace('_Indonesia.json', '.json')
                mod_map[canonical] = full_p
            elif '_Tidak berubah.json' in rel:
                pass
            else:
                mod_map[rel] = full_p
    return mod_map

def extract_mod_dict(mod_data):
    if isinstance(mod_data, dict):
        if 'Changes' in mod_data and isinstance(mod_data['Changes'], list):
            res = {}
            for ch in mod_data['Changes']:
                if 'Entries' in ch and isinstance(ch['Entries'], dict):
                    res.update(ch['Entries'])
            return res
        return mod_data
    return {}

def run():
    mod_dir = 'E:/data/Stardew Valley/Mods/[CP] PM - Mod Bahasa Indonesia/Assets'
    extracted_dir = 'D:/Stardew_ID_Project/extracted_original_json'
    
    mod_map = build_mod_map(mod_dir)
    print(f"Total mapped files in mod: {len(mod_map)}")
    
    total_keys = 0
    translated_count = 0
    untranslated_by_file = {}
    untranslated_samples = []

    for root, dirs, files in os.walk(extracted_dir):
        for f in files:
            if not f.endswith('.json'):
                continue
            ext_path = os.path.join(root, f)
            rel = os.path.relpath(ext_path, extracted_dir).replace('\\', '/')
            
            with open(ext_path, 'r', encoding='utf-8') as jf:
                try:
                    orig_data = json.load(jf)
                except Exception as e:
                    print(f"Error reading original {rel}: {e}")
                    continue
            
            content = orig_data.get('content')
            if not isinstance(content, dict):
                continue
                
            file_keys = len(content)
            total_keys += file_keys
            
            mod_path = mod_map.get(rel)
            mod_dict = {}
            if mod_path:
                try:
                    raw_mod = load_jsonc(mod_path)
                    mod_dict = extract_mod_dict(raw_mod)
                except Exception as e:
                    print(f"Failed to load mod for {rel}: {e}")
            
            missing_in_file = {}
            for k, orig_v in content.items():
                if k in mod_dict and mod_dict[k]:
                    translated_count += 1
                else:
                    missing_in_file[k] = orig_v
            
            if missing_in_file:
                untranslated_by_file[rel] = missing_in_file
                if len(untranslated_samples) < 10:
                    for k, v in list(missing_in_file.items())[:2]:
                        untranslated_samples.append((rel, k, str(v)[:80]))

    print(f"\n===== SUMMARY =====")
    print(f"Total original string keys: {total_keys}")
    print(f"Translated by mod:          {translated_count} ({translated_count/total_keys*100:.2f}%)")
    print(f"Untranslated keys:          {total_keys - translated_count} ({(total_keys - translated_count)/total_keys*100:.2f}%)")
    print(f"Files needing translation:  {len(untranslated_by_file)} files")
    
    # Save detailed untranslated report
    report_path = 'D:/Stardew_ID_Project/untranslated_report.json'
    with open(report_path, 'w', encoding='utf-8') as rf:
        json.dump(untranslated_by_file, rf, indent=2, ensure_ascii=False)
    print(f"Saved full untranslated report to: {report_path}")
    
    print("\nSample files with untranslated keys:")
    sorted_files = sorted(untranslated_by_file.items(), key=lambda x: len(x[1]), reverse=True)
    for rel, missing in sorted_files[:15]:
        print(f"  {rel}: {len(missing)} untranslated keys")

if __name__ == '__main__':
    run()
