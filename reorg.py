import json

# Read the current JSON file
with open('palabras.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create new structure with words grouped by difficulty
new_data = {
    "facil": [],
    "medio": [],
    "dificil": []
}

# Sort words into their respective difficulty levels
for word in data["palabras"]:
    difficulty = word["dificultad"]
    new_data[difficulty].append({
        "palabra": word["palabra"],
        "categoria": word["categoria"]
    })

# Sort words alphabetically within each difficulty level
for difficulty in new_data:
    new_data[difficulty].sort(key=lambda x: x["palabra"])

# Create the final structure
final_data = {
    "palabras": {
        "facil": new_data["facil"],
        "medio": new_data["medio"],
        "dificil": new_data["dificil"]
    },
    "total_palabras": {
        "facil": len(new_data["facil"]),
        "medio": len(new_data["medio"]),
        "dificil": len(new_data["dificil"]),
        "total": sum(len(words) for words in new_data.values())
    }
}

# Write the reorganized data back to the file
with open('palabras.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

# Print summary
print("\nReorganización completada:")
print(f"Palabras fáciles: {len(new_data['facil'])}")
print(f"Palabras medias: {len(new_data['medio'])}")
print(f"Palabras difíciles: {len(new_data['dificil'])}")
print(f"Total de palabras: {sum(len(words) for words in new_data.values())}") 