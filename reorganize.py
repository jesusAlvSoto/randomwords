import json

try:
    # Read the current JSON file
    with open('palabras.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("Successfully loaded JSON file")

    # Create new structure with words grouped by difficulty
    new_data = {
        'facil': [],
        'medio': [],
        'dificil': []
    }

    # Keep track of words we've seen to avoid duplicates
    seen_words = set()

    # Process all words from all difficulty levels
    for difficulty in ['facil', 'medio', 'dificil']:
        if difficulty not in data['palabras']:
            print(f"Warning: Difficulty level '{difficulty}' not found in data")
            continue
            
        for word in data['palabras'][difficulty]:
            try:
                # Skip duplicates
                if word['palabra'] in seen_words:
                    print(f"Warning: Duplicate word found: {word['palabra']}")
                    continue
                seen_words.add(word['palabra'])

                # Add difficulty to the word object if not present
                if 'dificultad' not in word:
                    word['dificultad'] = difficulty

                new_data[difficulty].append(word)
            except Exception as e:
                print(f"Error processing word:", e)
                print("Word data:", word)

    # Sort words alphabetically within each difficulty level
    for difficulty in new_data:
        new_data[difficulty].sort(key=lambda x: x['palabra'])

    # Create the final structure
    final_data = {
        'palabras': {
            'facil': new_data['facil'],
            'medio': new_data['medio'],
            'dificil': new_data['dificil']
        },
        'total_palabras': {
            'facil': len(new_data['facil']),
            'medio': len(new_data['medio']),
            'dificil': len(new_data['dificil']),
            'total': sum(len(words) for words in new_data.values())
        }
    }

    # Write the reorganized data back to the file
    with open('palabras.json', 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    # Print summary
    print('\nReorganización completada:')
    print(f'Palabras fáciles: {len(new_data["facil"])}')
    print(f'Palabras medias: {len(new_data["medio"])}')
    print(f'Palabras difíciles: {len(new_data["dificil"])}')
    print(f'Total de palabras: {sum(len(words) for words in new_data.values())}')

except Exception as e:
    print("Error:", e) 