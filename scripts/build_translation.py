import os
import re
import json
import subprocess
import shutil

MANUAL_TRANSLATIONS = {
    'Characters/Dialogue/Alex.json': {
        'AcceptGift_Negative_book_item': 'Uhhh... Membaca? Ya, um... Kurasa aku bisa mencobanya.$s',
        'AcceptGift_Positive_category_egg': '$c 0.8#Hei, terima kasih. Telur sangat bagus untuk membentuk otot.#*kreeek*... *srrruuup*... Mmmm. Baru ini namanya camilan mantap.'
    },
    'Characters/Dialogue/Dwarf.json': {
        'AcceptGift_Neutral_milk_item': 'Ah, \'susu\'... *slurp*... Menarik sekali. Coba ingatkan aku lagi... dari mana sebenarnya jus ini berasal?#$b#...!!! *byur*'
    },
    'Characters/Dialogue/Elliott.json': {
        'AcceptGift_Positive_forage_item_beach': 'Ah, kamu habis mencari barang di tepi pantai... Hobi yang bagus! Terima kasih.',
        'AcceptGift_Positive_book_item': 'Ah, sebuah buku... Ya, mungkin untaian kata di dalam halaman-halaman ini bisa memberikan wawasan baru. Terima kasih.'
    },
    'Characters/Dialogue/Evelyn.json': {
        'AcceptGift_Positive_forage_item_beach': 'Terima kasih, sayang. Ini membangkitkan kenangan manis masa lalu...'
    },
    'Characters/Dialogue/Gus.json': {
        'AcceptGift_Positive_category_cooking': '*hirup*... Ah. Masakan yang luar biasa lezat. Kamu tahu betul apa yang kusukai, @.$h'
    },
    'Characters/Dialogue/Jas.json': {
        'AcceptGift_Positive_doll_item': 'Oh, aku suka dia! Dia akan cocok berteman dengan boneka-bonekaku yang lain.$h',
        'AcceptGift_Negative_alcohol_item': 'Umm... Aku tidak boleh minum ini. Bukankah ini untuk orang dewasa?$s',
        'AcceptGift_Negative_coffee_item': 'Oh... Bibi Marnie belum mengizinkanku minum kopi...$s'
    },
    'Characters/Dialogue/Leah.json': {
        'fall_Mon': '#$c .5#Aku menemukan beberapa jamur liar di akhir pekan kemarin!#$e#Sarapanku hari ini sepiring penuh jamur liar dan telur... Aku masih kenyang sampai sekarang.#$e#Perhatikan langkahmu baik-baik dan kamu pasti akan menemukan jamur juga... Aku yakin itu.'
    },
    'Characters/Dialogue/Linus.json': {
        'AcceptGift_Positive_category_greens': 'Temuan yang bagus! Aku selalu senang saat menyantap makanan dari alam liar. Terima kasih.',
        'AcceptGift_Positive_category_fish': 'Ah, kelihatannya masih segar. Aku bakal makan enak malam ini!$h'
    },
    'Characters/Dialogue/Penny.json': {
        'AcceptGift_Positive_ancient_item': 'Wah... ini kelihatan sangat kuno. Aku harus menanyakannya ke Gunther. Terima kasih!$h',
        'AcceptGift_Positive_book_item': 'Terima kasih! Aku hampir selesai membaca buku yang sekarang, tapi yang ini akan kubaca berikutnya!$h',
        'Resort_Towel_2_Married': 'Hei sayang, apa kamu keberatan bergeser sedikit ke kiri?#$b#Terima kasih, silau mataharinya tadi bikin agak susah membaca!$h'
    },
    'Characters/Dialogue/Vincent.json': {
        'AcceptGift_Negative_alcohol_item': '*endus*... apa ini? Baunya nggak enak banget... Ibuuuu!!!$s'
    },
    'Characters/Dialogue/Willy.json': {
        'AcceptGift_Positive_coffee_item': 'Ah, ini bisa menghangatkan tulang-tulang tuaku. Terima kasih.'
    },
    'Data/Festivals/FestivalDates.json': {
        'spring13': 'Festival Telur',
        'spring24': 'Tarian Bunga',
        'summer11': 'Luau',
        'summer28': 'Tarian Ubur-ubur Cahaya Bulan',
        'fall16': 'Pekan Raya Stardew Valley',
        'fall27': 'Malam Roh',
        'winter8': 'Festival Es',
        'winter25': 'Pesta Bintang Musim Dingin'
    },
    'Data/Festivals/fall27.json': {
        'Elliott': 'Wah, halo @. Udaranya dingin sekali, ya?'
    },
    'Strings/Buildings.json': {
        'Barn_GeneralName': 'Kandang Besar',
        'Coop_GeneralName': 'Kandang Unggas',
        'Shed_GeneralName': 'Gudang'
    },
    'Strings/Locations.json': {
        'ScienceHouse_Carpenter_NotEnoughWood': 'Maaf... Uangmu cukup, tapi aku juga membutuhkan {0} kayu.',
        'ScienceHouse_Carpenter_NotEnoughHardwood': 'Maaf... Uangmu cukup, tapi aku juga membutuhkan {0} kayu keras.'
    },
    'Strings/NPCNames.json': {
        'Bear': 'Beruang',
        'Bouncer': 'Penjaga Pintu',
        'Governor': 'Gubernur',
        'Grandpa': 'Kakek',
        'Henchman': 'Anak Buah',
        'OldMariner': 'Pelaut Tua',
        'Wizard': 'Penyihir'
    },
    'Strings/UI.json': {
        'Character_FarmNameSuffix': ''
    },
    'Strings/Objects.json': {
        'DriedFruit_Description': 'Potongan {0} kering yang kenyal.',
        'SmokedFish_Description': 'Seekor {0} utuh, diasapi dengan sempurna.'
    },
    'Strings/SpeechBubbles.json': {
        'SeedShop_Pierre_Greeting2': 'Halo petani {0}!'
    }
}

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

def main():
    project_root = 'D:/Stardew_ID_Project'
    mod_dir = 'E:/data/Stardew Valley/Mods/[CP] PM - Mod Bahasa Indonesia/Assets'
    extracted_dir = os.path.join(project_root, 'extracted_original_json')
    translated_json_dir = os.path.join(project_root, 'translated_json')
    output_content_dir = os.path.join(project_root, 'output_ready_to_replace/Content')
    xnbcli = os.path.join(project_root, 'tools/xnbcli/xnbcli.exe')

    os.makedirs(translated_json_dir, exist_ok=True)
    os.makedirs(output_content_dir, exist_ok=True)

    mod_map = build_mod_map(mod_dir)
    print(f"Mod map loaded: {len(mod_map)} target files.")

    # 1. Merge translations into translated_json
    merged_files = []
    for root, dirs, files in os.walk(extracted_dir):
        for f in files:
            if not f.endswith('.json'):
                continue
            ext_path = os.path.join(root, f)
            rel = os.path.relpath(ext_path, extracted_dir).replace('\\', '/')

            with open(ext_path, 'r', encoding='utf-8') as orig_file:
                orig_json = json.load(orig_file)

            content = orig_json.get('content')
            if not isinstance(content, dict):
                continue

            # Load mod translations if available
            mod_path = mod_map.get(rel)
            mod_dict = {}
            if mod_path:
                try:
                    raw_mod = load_jsonc(mod_path)
                    mod_dict = extract_mod_dict(raw_mod)
                except Exception as e:
                    print(f"Error loading mod file {mod_path}: {e}")

            # Also check manual translations
            manual_dict = MANUAL_TRANSLATIONS.get(rel, {})

            # Apply translations
            translated_keys_in_file = 0
            for k in content.keys():
                if k in manual_dict:
                    content[k] = manual_dict[k]
                    translated_keys_in_file += 1
                elif k in mod_dict and mod_dict[k] is not None:
                    content[k] = mod_dict[k]
                    translated_keys_in_file += 1

            # Save merged JSON
            out_json_path = os.path.join(translated_json_dir, rel.replace('/', os.sep))
            os.makedirs(os.path.dirname(out_json_path), exist_ok=True)
            with open(out_json_path, 'w', encoding='utf-8') as out_f:
                json.dump(orig_json, out_f, indent=4, ensure_ascii=False)

            merged_files.append((rel, len(content), translated_keys_in_file))

    print(f"Generated {len(merged_files)} translated JSON files.")

    # 2. Pack using xnbcli directory by directory
    pack_dirs = set()
    for rel, _, _ in merged_files:
        dirname = os.path.dirname(rel)
        pack_dirs.add(dirname)

    total_packed = 0
    total_expected = len(merged_files)

    for pdir in sorted(pack_dirs):
        in_dir = os.path.join(translated_json_dir, pdir.replace('/', os.sep))
        out_dir = os.path.join(output_content_dir, pdir.replace('/', os.sep))
        os.makedirs(out_dir, exist_ok=True)

        json_count = len([f for f in os.listdir(in_dir) if f.endswith('.json')])
        res = subprocess.run([xnbcli, 'pack', in_dir, out_dir], capture_output=True, text=True)
        success_count = res.stdout.count('Output file saved:')
        total_packed += success_count
        print(f"Packed {pdir or 'root'}: {success_count}/{json_count} XNB files")
        if success_count < json_count:
            print("  Output:\n", res.stdout)
            print("  Error:\n", res.stderr)

    print(f"\n===== PACKING COMPLETE =====")
    print(f"Total packed XNB files: {total_packed}/{total_expected}")

    # 3. Validate output files
    valid_count = 0
    for root, dirs, files in os.walk(output_content_dir):
        for f in files:
            if not f.endswith('.xnb'):
                continue
            fpath = os.path.join(root, f)
            with open(fpath, 'rb') as xf:
                header = xf.read(6)
                if header == b'XNBa\x05@':
                    valid_count += 1
                else:
                    print(f"WARNING: Invalid header in {fpath}: {header}")

    print(f"Header validation: {valid_count}/{total_packed} files have valid Android 'XNBa\\x05@' header.")

if __name__ == '__main__':
    main()
