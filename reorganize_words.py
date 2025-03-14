import json

def reorganize_words():
    try:
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
        for word in data.get("palabras", []):
            try:
                difficulty = word.get("dificultad", "")
                if difficulty not in new_data:
                    print(f"Warning: Unknown difficulty level '{difficulty}' for word '{word.get('palabra', '')}'")
                    continue
                
                new_data[difficulty].append({
                    "palabra": word.get("palabra", ""),
                    "categoria": word.get("categoria", "")
                })
            except Exception as e:
                print(f"Error processing word: {word}")
                print(f"Error details: {str(e)}")
                continue
        
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
        
    except Exception as e:
        print(f"Error general: {str(e)}")
        raise

if __name__ == "__main__":
    reorganize_words() 