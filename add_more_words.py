import json

# New words to add, categorized by themes
new_words = {
    "animales": [
        ("abeja", "medio"), ("águila", "dificil"), ("araña", "medio"), ("ardilla", "dificil"),
        ("ballena", "dificil"), ("búho", "medio"), ("caballo", "dificil"), ("camello", "dificil"),
        ("canario", "dificil"), ("canguro", "dificil"), ("caracol", "dificil"), ("cebra", "medio"),
        ("cerdo", "medio"), ("ciervo", "medio"), ("cocodrilo", "dificil"), ("conejo", "medio"),
        ("delfín", "medio"), ("elefante", "dificil"), ("foca", "facil"), ("gallina", "dificil"),
        ("gato", "facil"), ("gorila", "dificil"), ("gusano", "medio"), ("hipopótamo", "dificil"),
        ("hormiga", "dificil"), ("jaguar", "medio"), ("jirafa", "dificil"), ("koala", "medio"),
        ("lagarto", "dificil"), ("león", "facil"), ("leopardo", "dificil"), ("lobo", "facil"),
        ("loro", "facil"), ("mariposa", "dificil"), ("mono", "facil"), ("mosca", "medio"),
        ("oso", "facil"), ("oveja", "medio"), ("pájaro", "dificil"), ("paloma", "dificil"),
        ("panda", "medio"), ("pantera", "dificil"), ("pato", "facil"), ("pavo", "facil"),
        ("perro", "medio"), ("pingüino", "dificil"), ("pollo", "medio"), ("pulpo", "medio"),
        ("rana", "facil"), ("ratón", "medio"), ("rinoceronte", "dificil"), ("serpiente", "dificil"),
        ("tigre", "medio"), ("tortuga", "dificil"), ("vaca", "facil"), ("zorro", "medio")
    ],
    "naturaleza": [
        ("aire", "facil"), ("arena", "medio"), ("aurora", "dificil"), ("bosque", "medio"),
        ("brisa", "medio"), ("campo", "medio"), ("cielo", "medio"), ("clima", "medio"),
        ("costa", "medio"), ("desierto", "dificil"), ("estrella", "dificil"), ("flor", "facil"),
        ("fuego", "medio"), ("hierba", "medio"), ("hielo", "medio"), ("hoja", "facil"),
        ("isla", "facil"), ("lago", "facil"), ("lluvia", "medio"), ("luna", "facil"),
        ("mar", "facil"), ("montaña", "dificil"), ("nieve", "medio"), ("nube", "facil"),
        ("océano", "dificil"), ("ola", "facil"), ("playa", "medio"), ("río", "facil"),
        ("roca", "facil"), ("selva", "medio"), ("sol", "facil"), ("tierra", "medio"),
        ("tormenta", "dificil"), ("valle", "medio"), ("viento", "medio"), ("volcán", "dificil")
    ],
    "colores": [
        ("amarillo", "dificil"), ("azul", "facil"), ("beige", "medio"), ("blanco", "medio"),
        ("dorado", "dificil"), ("gris", "facil"), ("marrón", "medio"), ("naranja", "dificil"),
        ("negro", "medio"), ("plateado", "dificil"), ("púrpura", "dificil"), ("rojo", "facil"),
        ("rosa", "facil"), ("verde", "medio"), ("violeta", "dificil")
    ],
    "numeros": [
        ("cero", "facil"), ("cinco", "medio"), ("cuatro", "medio"), ("diez", "facil"),
        ("dos", "facil"), ("nueve", "medio"), ("ocho", "facil"), ("seis", "facil"),
        ("siete", "medio"), ("tres", "facil"), ("uno", "facil")
    ],
    "familia": [
        ("abuelo", "medio"), ("abuela", "medio"), ("esposo", "dificil"), ("esposa", "dificil"),
        ("familia", "dificil"), ("hermana", "dificil"), ("hermano", "dificil"), ("hijo", "facil"),
        ("hija", "facil"), ("madre", "medio"), ("padre", "medio"), ("primo", "medio"),
        ("prima", "medio"), ("sobrino", "dificil"), ("sobrina", "dificil"), ("tío", "facil"),
        ("tía", "facil")
    ]
}

try:
    # Read current JSON file
    with open('palabras.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Get existing words
    existing_words = set()
    for difficulty in data['palabras']:
        for word in data['palabras'][difficulty]:
            existing_words.add(word['palabra'].lower())

    print(f"Found {len(existing_words)} existing words")

    # Add new words that don't exist yet
    words_added = 0
    for categoria, words in new_words.items():
        for palabra, dificultad in words:
            if palabra.lower() not in existing_words:
                data['palabras'][dificultad].append({
                    "palabra": palabra,
                    "categoria": categoria,
                    "dificultad": dificultad
                })
                existing_words.add(palabra.lower())
                words_added += 1

    # Sort words within each difficulty level
    for difficulty in data['palabras']:
        data['palabras'][difficulty].sort(key=lambda x: x['palabra'])

    # Update total counts
    data['total_palabras'] = {
        "facil": len(data['palabras']['facil']),
        "medio": len(data['palabras']['medio']),
        "dificil": len(data['palabras']['dificil'])
    }
    data['total_palabras']['total'] = sum(len(words) for words in data['palabras'].values())

    # Write updated data back to file
    with open('palabras.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nPalabras añadidas: {words_added}")
    print("\nNuevo total:")
    print(f"Palabras fáciles: {data['total_palabras']['facil']}")
    print(f"Palabras medias: {data['total_palabras']['medio']}")
    print(f"Palabras difíciles: {data['total_palabras']['dificil']}")
    print(f"Total de palabras: {data['total_palabras']['total']}")

except Exception as e:
    print("Error:", e)