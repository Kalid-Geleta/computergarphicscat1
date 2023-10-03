import json

languages = ["sw", "de"]  # Add more languages as needed
combined_data = []

# Load English train data
with open("en_train.jsonl", "r", encoding="utf-8") as en_file:
    en_data = [json.loads(line) for line in en_file]

# Load translations for other languages
for lang in languages:
    with open(f"{lang}_train.jsonl", "r", encoding="utf-8") as lang_file:
        lang_data = [json.loads(line) for line in lang_file]

    # Combine English and translation data
    combined_data.extend([{"id": en["id"], "en_utt": en["utt"], f"{lang}_utt": lang_item["utt"]} for en, lang_item in zip(en_data, lang_data)])

# Save combined data to a JSON file
with open("combined_train.json", "w", encoding="utf-8") as combined_file:
    json.dump(combined_data, combined_file, ensure_ascii=False, indent=4)

print("Combined train data saved to combined_train.json")
