import json
import random

# Predefined lists of words by category
peliculas = [
    "avengers", "avatar", "titanic", "matrix", "starwars", "jurasicpark", "frozen", "inception", "gladiador",
    "batman", "superman", "spiderman", "shrek", "pocahontas", "mulan", "aladdin", "tarzan", "thor", "joker",
    "narnia", "hobbit", "godzilla", "alien", "terminator", "rocky", "jaws", "kong", "transformers", "zorro",
    "cars", "toystory", "nemo", "coco", "moana", "ratatouille", "up", "brave", "tangled", "incredibles",
    "deadpool", "venom", "aquaman", "wonderwoman", "blackpanther", "ironman", "antman", "flash", "hulk", "wolverine",
    "madagascar", "kungfupanda", "minions", "iceage", "rio", "zootopia", "dumbo", "bambi", "cinderella", "pinocchio",
    "maleficent", "cruella", "minionrise", "avatar2", "topgun", "dune", "interstellar", "gravity", "martian", "passengers"
]

acciones = [
    "correr", "saltar", "bailar", "cantar", "nadar", "volar", "dormir", "comer", "beber", "reír",
    "llorar", "gritar", "susurrar", "aplaudir", "silbar", "gatear", "trepar", "empujar", "jalar", "patear",
    "abrazar", "besar", "pelear", "jugar", "cocinar", "leer", "escribir", "pintar", "dibujar", "construir",
    "caminar", "trotar", "marchar", "arrastrar", "deslizar", "girar", "rodar", "agitar", "sacudir", "golpear",
    "acariciar", "pellizcar", "masticar", "soplar", "estornudar", "toser", "respirar", "meditar", "soñar", "pensar",
    "estudiar", "trabajar", "descansar", "ejercitar", "entrenar", "competir", "ganar", "perder", "celebrar", "festejar"
]

naturaleza = [
    "montaña", "río", "mar", "bosque", "desierto", "selva", "playa", "lago", "volcán", "glaciar",
    "cascada", "arcoiris", "nube", "sol", "luna", "estrella", "planeta", "cometa", "aurora", "tornado",
    "huracán", "tsunami", "terremoto", "avalancha", "iceberg", "coral", "geyser", "cueva", "cañón", "pradera"
]

conceptos = [
    "amor", "paz", "libertad", "justicia", "verdad", "honor", "lealtad", "amistad", "valentía", "sabiduría",
    "fe", "esperanza", "destino", "tiempo", "eternidad", "vida", "muerte", "sueño", "memoria", "pensamiento",
    "alma", "espíritu", "mente", "conciencia", "voluntad", "razón", "lógica", "intuición", "creatividad", "imaginación"
]

objetos = [
    "mesa", "silla", "cama", "espejo", "reloj", "libro", "lápiz", "papel", "tijeras", "cuchara",
    "tenedor", "cuchillo", "vaso", "plato", "taza", "botella", "bolsa", "caja", "llave", "candado",
    "paraguas", "sombrero", "zapato", "camisa", "pantalón", "vestido", "anillo", "collar", "pulsera", "reloj"
]

profesiones = [
    "doctor", "profesor", "abogado", "ingeniero", "arquitecto", "chef", "piloto", "bombero", "policía", "enfermera",
    "dentista", "veterinario", "carpintero", "electricista", "plomero", "pintor", "escritor", "músico", "actor", "bailarín",
    "científico", "investigador", "periodista", "fotógrafo", "diseñador", "programador", "contador", "vendedor", "agricultor", "pescador"
]

lugares = [
    "casa", "escuela", "hospital", "parque", "museo", "biblioteca", "teatro", "cine", "restaurante", "hotel",
    "aeropuerto", "estación", "mercado", "plaza", "iglesia", "castillo", "palacio", "pirámide", "estadio", "gimnasio",
    "playa", "montaña", "bosque", "desierto", "selva", "isla", "volcán", "glaciar", "cascada", "cueva"
]

ciencia = [
    "átomo", "molécula", "célula", "ADN", "gravedad", "energía", "materia", "tiempo", "espacio", "luz",
    "sonido", "calor", "fuerza", "velocidad", "presión", "temperatura", "masa", "volumen", "densidad", "frecuencia",
    "evolución", "genética", "química", "física", "biología", "astronomía", "geología", "meteorología", "ecología", "neurología"
]

musica = [
    "guitarra", "piano", "violín", "batería", "flauta", "saxofón", "trompeta", "clarinete", "arpa", "acordeón",
    "tambor", "maracas", "pandero", "xilófono", "bajo", "violonchelo", "tuba", "oboe", "banjo", "ukelele",
    "ritmo", "melodía", "armonía", "compás", "nota", "acorde", "escala", "tempo", "sonata", "sinfonía"
]

tecnologia = [
    "computadora", "teléfono", "tablet", "robot", "internet", "wifi", "bluetooth", "satélite", "drone", "chip",
    "pantalla", "teclado", "mouse", "impresora", "scanner", "cable", "batería", "memoria", "disco", "programa",
    "aplicación", "red", "servidor", "router", "antena", "sensor", "cámara", "micrófono", "altavoz", "procesador"
]

comida = [
    "pizza", "hamburguesa", "sushi", "tacos", "pasta", "arroz", "sopa", "ensalada", "pollo", "pescado",
    "carne", "pan", "queso", "huevo", "leche", "fruta", "verdura", "chocolate", "helado", "galleta",
    "tortilla", "enchilada", "burrito", "paella", "ceviche", "empanada", "arepa", "tamales", "pozole", "mole"
]

animales = [
    "perro", "gato", "león", "tigre", "elefante", "jirafa", "mono", "cebra", "hipopótamo", "rinoceronte",
    "cocodrilo", "serpiente", "águila", "pingüino", "delfín", "ballena", "tiburón", "pulpo", "cangrejo", "tortuga",
    "panda", "koala", "canguro", "oso", "lobo", "zorro", "conejo", "ardilla", "hamster", "pájaro"
]

emociones = [
    "alegría", "tristeza", "enojo", "miedo", "sorpresa", "asco", "amor", "odio", "celos", "vergüenza",
    "orgullo", "culpa", "ansiedad", "calma", "euforia", "melancolía", "nostalgia", "esperanza", "frustración", "satisfacción",
    "soledad", "empatía", "compasión", "gratitud", "admiración", "desprecio", "entusiasmo", "apatía", "serenidad", "angustia"
]

deportes = [
    "fútbol", "baloncesto", "tenis", "voleibol", "béisbol", "rugby", "golf", "hockey", "boxeo", "natación",
    "atletismo", "gimnasia", "ciclismo", "surf", "esquí", "patinaje", "karate", "judo", "yoga", "ajedrez",
    "cricket", "polo", "remo", "vela", "buceo", "escalada", "skateboard", "snowboard", "parkour", "crossfit"
]

arte = [
    "pintura", "escultura", "fotografía", "danza", "teatro", "cine", "música", "literatura", "poesía", "arquitectura",
    "dibujo", "grabado", "cerámica", "tejido", "orfebrería", "caligrafía", "mosaico", "vitral", "mural", "collage",
    "performance", "instalación", "videoarte", "grafiti", "ballet", "ópera", "circo", "marioneta", "origami", "acuarela"
]

# New categories
mitologia = [
    "zeus", "poseidon", "hades", "ares", "hermes", "apolo", "artemisa", "afrodita", "atenea", "hefesto",
    "dionisio", "hera", "demeter", "persefone", "medusa", "minotauro", "pegaso", "centauro", "quimera", "hidra",
    "fenix", "dragon", "unicornio", "grifo", "sirena", "kraken", "titan", "ciclope", "esfinge", "basilisco",
    "thor", "odin", "loki", "freya", "valquiria", "yggdrasil", "fenrir", "midgard", "asgard", "ragnarok"
]

historia = [
    "piramides", "coliseo", "acropolis", "murallachina", "tajmahal", "stonehenge", "azteca", "inca", "maya", "egipto",
    "roma", "grecia", "babilonia", "persia", "vikingos", "samurai", "ninja", "faraon", "emperador", "rey",
    "guerra", "paz", "revolucion", "independencia", "conquista", "descubrimiento", "invencion", "renacimiento", "medieval", "moderno",
    "antiguo", "futuro", "presente", "pasado", "siglo", "decada", "milenio", "era", "epoca", "periodo"
]

instrumentos = [
    "violin", "piano", "guitarra", "bateria", "flauta", "saxofon", "trompeta", "clarinete", "arpa", "acordeon",
    "bajo", "violonchelo", "contrabajo", "oboe", "fagot", "trombon", "tuba", "xilofono", "triangulo", "tambor",
    "pandereta", "maracas", "bongo", "conga", "timbal", "castañuela", "armonica", "banjo", "ukelele", "mandolina",
    "gaita", "dulzaina", "ocarina", "sitar", "koto", "shamisen", "didgeridoo", "balalaika", "charango", "cuatro"
]

# Additional categories
ropa = [
    "camisa", "pantalon", "vestido", "falda", "zapatos", "calcetines", "sombrero", "gorra", "bufanda", "guantes",
    "abrigo", "chaqueta", "sueter", "corbata", "cinturon", "pijama", "traje", "blusa", "shorts", "medias",
    "botas", "sandalias", "zapatillas", "gabardina", "chaleco", "sudadera", "bermudas", "bikini", "gafas", "reloj",
    "anillo", "collar", "pulsera", "pendientes", "diadema", "bolso", "cartera", "mochila", "maleta", "paraguas"
]

herramientas = [
    "martillo", "destornillador", "sierra", "taladro", "llave", "alicate", "pinza", "serrucho", "nivel", "metro",
    "cinta", "tijera", "cuchillo", "hacha", "pala", "rastrillo", "brocha", "pincel", "rodillo", "espátula",
    "lima", "tornillo", "clavo", "tuerca", "arandela", "grapa", "cepillo", "lija", "soldador", "soplete",
    "escalera", "andamio", "carretilla", "gato", "compresor", "taladrador", "fresadora", "torno", "yunque", "prensa"
]

plantas = [
    "rosa", "margarita", "tulipan", "girasol", "orquidea", "clavel", "lirio", "jazmin", "violeta", "amapola",
    "cactus", "palmera", "pino", "roble", "sauce", "bambu", "helecho", "musgo", "algas", "hierba",
    "lavanda", "menta", "romero", "tomillo", "albahaca", "perejil", "cilantro", "oregano", "salvia", "hinojo",
    "cebolla", "ajo", "zanahoria", "papa", "tomate", "lechuga", "espinaca", "calabaza", "pepino", "brocoli"
]

transporte = [
    "coche", "autobus", "tren", "avion", "barco", "bicicleta", "moto", "camion", "helicoptero", "submarino",
    "tranvia", "metro", "taxi", "furgoneta", "ambulancia", "policia", "bomberos", "grua", "tractor", "carreta",
    "patinete", "monopatín", "segway", "globo", "dirigible", "cohete", "nave", "crucero", "velero", "kayak",
    "canoa", "lancha", "yate", "ferry", "gondola", "teleferico", "funicular", "zeppelin", "ultraligero", "parapente"
]

bebidas = [
    "agua", "leche", "cafe", "te", "cerveza", "vino", "refresco", "zumo", "batido", "coctel",
    "limonada", "horchata", "sangria", "champan", "sidra", "tequila", "ron", "whisky", "vodka", "ginebra",
    "cola", "fanta", "sprite", "nestea", "aquarius", "gatorade", "smoothie", "milkshake", "chocolate", "mate",
    "sake", "mojito", "margarita", "daiquiri", "pisco", "mezcal", "absenta", "brandy", "cognac", "licor"
]

# More categories
juegos = [
    "ajedrez", "damas", "monopoly", "scrabble", "jenga", "domino", "poker", "ruleta", "dados", "cartas",
    "tetris", "pacman", "mario", "sonic", "zelda", "pokemon", "minecraft", "fortnite", "fifa", "candy",
    "uno", "risk", "pictionary", "trivial", "twister", "bingo", "solitario", "parchis", "oca", "batalla",
    "rompecabezas", "sudoku", "crucigrama", "sopa", "laberinto", "memoria", "simon", "conecta4", "tres", "ahorcado"
]

colores = [
    "rojo", "azul", "verde", "amarillo", "naranja", "morado", "rosa", "marron", "gris", "negro",
    "blanco", "dorado", "plateado", "turquesa", "celeste", "violeta", "magenta", "cyan", "beige", "coral",
    "indigo", "carmesi", "escarlata", "borgoña", "ocre", "cobre", "bronce", "jade", "esmeralda", "zafiro",
    "purpura", "lavanda", "lila", "fucsia", "salmon", "crema", "oliva", "granate", "bermejo", "carmin"
]

muebles = [
    "mesa", "silla", "sofa", "cama", "armario", "estanteria", "comoda", "escritorio", "taburete", "banco",
    "mecedora", "hamaca", "tocador", "espejo", "lampara", "alfombra", "cortina", "perchero", "zapatero", "vitrina",
    "cajonera", "biblioteca", "taquillon", "consola", "aparador", "recibidor", "rinconera", "butaca", "puff", "ottoman",
    "tresillo", "divan", "chaise", "banqueta", "reposapiés", "mesita", "cabecero", "biombo", "credenza", "alacena"
]

oficina = [
    "papel", "boligrafo", "lapiz", "goma", "regla", "tijeras", "grapadora", "clips", "carpeta", "archivo",
    "impresora", "scanner", "fotocopiadora", "ordenador", "monitor", "teclado", "raton", "agenda", "calendario", "notas",
    "marcador", "resaltador", "corrector", "pegamento", "chinchetas", "sacapuntas", "compas", "cartulina", "sobre", "sello",
    "archivador", "papelera", "bandeja", "tarjeta", "libreta", "cuaderno", "bloc", "portafolio", "maletín", "pluma"
]

cocina = [
    "sarten", "olla", "cacerola", "plato", "vaso", "taza", "cuchara", "tenedor", "cuchillo", "espumadera",
    "colador", "rallador", "batidora", "licuadora", "tostadora", "microondas", "horno", "nevera", "congelador", "cafetera",
    "tetera", "exprimidor", "mortero", "tabla", "escurridor", "tupperware", "freidora", "bascula", "temporizador", "termometro",
    "delantal", "manopla", "trapo", "bayeta", "estropajo", "papel", "aluminio", "film", "bolsa", "recipiente"
]

# Final categories
personajes = [
    "superman", "batman", "spiderman", "ironman", "hulk", "thor", "wonderwoman", "flash", "aquaman", "robin",
    "sherlock", "watson", "gandalf", "frodo", "aragorn", "legolas", "gollum", "voldemort", "potter", "hermione",
    "mickey", "donald", "goofy", "pluto", "popeye", "garfield", "snoopy", "asterix", "obelix", "tintin",
    "pikachu", "mario", "luigi", "sonic", "pacman", "link", "samus", "kratos", "lara", "snake"
]

deportistas = [
    "messi", "ronaldo", "neymar", "pele", "maradona", "zidane", "beckham", "ronaldinho", "iniesta", "xavi",
    "federer", "nadal", "djokovic", "serena", "sharapova", "jordan", "lebron", "kobe", "curry", "durant",
    "bolt", "phelps", "biles", "tyson", "ali", "pacquiao", "mayweather", "schumacher", "hamilton", "rossi",
    "woods", "mcilroy", "nicklaus", "palmer", "gretzky", "messi", "ronaldo", "neymar", "pele", "maradona"
]

celebridades = [
    "einstein", "newton", "darwin", "tesla", "edison", "davinci", "mozart", "beethoven", "picasso", "dali",
    "chaplin", "monroe", "elvis", "jackson", "madonna", "beyonce", "gaga", "swift", "adele", "queen",
    "spielberg", "disney", "hitchcock", "tarantino", "kubrick", "shakespeare", "hemingway", "twain", "dickens", "poe",
    "aristoteles", "platon", "socrates", "freud", "jung", "gandhi", "mandela", "teresa", "diana", "kennedy"
]

festividades = [
    "navidad", "pascua", "halloween", "carnaval", "nochevieja", "reyes", "sanvalentin", "thanksgiving", "diwali", "hanukkah",
    "ramadan", "añonuevo", "independencia", "revolucion", "constitucion", "victoria", "paz", "trabajo", "primavera", "verano",
    "otoño", "invierno", "semana", "fiesta", "cumpleaños", "boda", "graduacion", "aniversario", "jubilacion", "bautizo",
    "comunion", "confirmacion", "funeral", "velorio", "ceremonia", "ritual", "tradicion", "costumbre", "celebracion", "festejo"
]

clima = [
    "lluvia", "nieve", "granizo", "viento", "tormenta", "huracan", "tornado", "tifon", "ciclon", "tsunami",
    "sol", "calor", "frio", "templado", "humedad", "sequia", "inundacion", "avalancha", "ventisca", "neblina",
    "niebla", "rocio", "escarcha", "hielo", "deshielo", "brisa", "vendaval", "rafaga", "relampago", "trueno",
    "rayo", "arcoiris", "amanecer", "atardecer", "anochecer", "alba", "ocaso", "mediodia", "noche", "dia"
]

# Additional final categories
paises = [
    "españa", "francia", "italia", "alemania", "portugal", "inglaterra", "holanda", "belgica", "suiza", "austria",
    "grecia", "rusia", "china", "japon", "india", "brasil", "argentina", "mexico", "colombia", "peru",
    "chile", "uruguay", "paraguay", "bolivia", "ecuador", "venezuela", "panama", "cuba", "jamaica", "canada",
    "egipto", "marruecos", "sudafrica", "australia", "indonesia", "tailandia", "vietnam", "corea", "turquia", "israel"
]

ciudades = [
    "madrid", "barcelona", "valencia", "sevilla", "bilbao", "malaga", "granada", "toledo", "salamanca", "cordoba",
    "paris", "londres", "roma", "berlin", "amsterdam", "bruselas", "lisboa", "atenas", "viena", "praga",
    "tokio", "pekin", "seul", "dubai", "bombay", "singapur", "bangkok", "cairo", "estambul", "moscu",
    "newyork", "losangeles", "chicago", "miami", "toronto", "mexico", "rio", "buenosaires", "santiago", "lima"
]

baile = [
    "salsa", "tango", "flamenco", "ballet", "jazz", "hiphop", "breakdance", "bachata", "merengue", "cumbia",
    "samba", "rumba", "cha", "vals", "polka", "swing", "rock", "disco", "reggae", "pop",
    "contemporaneo", "folclore", "tap", "ballet", "danza", "baile", "ritmo", "paso", "giro", "salto",
    "pirueta", "acrobacia", "coreografia", "musica", "compas", "pareja", "grupo", "solo", "dueto", "conjunto"
]

medicina = [
    "hospital", "clinica", "consultorio", "farmacia", "ambulancia", "quirofano", "radiologia", "laboratorio", "urgencias", "pediatria",
    "cardiologia", "neurologia", "oncologia", "traumatologia", "dermatologia", "psiquiatria", "ginecologia", "oftalmologia", "dental", "cirugia",
    "medicina", "enfermeria", "terapia", "rehabilitacion", "diagnostico", "tratamiento", "curacion", "prevencion", "vacuna", "receta",
    "pastilla", "jarabe", "inyeccion", "vendaje", "muleta", "silla", "camilla", "estetoscopio", "termometro", "jeringa"
]

materiales = [
    "madera", "metal", "plastico", "vidrio", "ceramica", "papel", "carton", "tela", "cuero", "goma",
    "oro", "plata", "bronce", "cobre", "hierro", "acero", "aluminio", "titanio", "platino", "niquel",
    "marmol", "granito", "pizarra", "cemento", "hormigon", "ladrillo", "yeso", "arcilla", "arena", "piedra",
    "cristal", "porcelana", "caucho", "corcho", "espuma", "fibra", "lana", "algodon", "seda", "nylon"
]

# Final set of categories
insectos = [
    "hormiga", "abeja", "avispa", "mariposa", "polilla", "mosca", "mosquito", "libelula", "grillo", "saltamontes",
    "cigarra", "cucaracha", "escarabajo", "mariquita", "mantis", "araña", "escorpion", "ciempies", "milpies", "gusano",
    "oruga", "termita", "pulga", "chinche", "garrapata", "tarantula", "viuda", "luciernaga", "tijereta", "cochinilla",
    "caracol", "babosa", "lombriz", "larva", "ninfa", "crisalida", "capullo", "colmena", "panal", "hormiguero"
]

flores = [
    "rosa", "clavel", "tulipan", "margarita", "girasol", "orquidea", "jazmin", "lirio", "violeta", "amapola",
    "dalia", "gardenia", "azucena", "petunia", "geranio", "begonia", "crisantemo", "narciso", "azahar", "lavanda",
    "hortensia", "pensamiento", "gladiolo", "jacinto", "nomeolvides", "calendula", "camelia", "magnolia", "buganvilla", "hibisco",
    "flor", "ramo", "jardin", "maceta", "semilla", "tallo", "hoja", "petalo", "polen", "nectar"
]

mar = [
    "ola", "playa", "arena", "concha", "coral", "perla", "estrella", "medusa", "cangrejo", "langosta",
    "pulpo", "calamar", "tiburon", "delfin", "ballena", "foca", "morsa", "tortuga", "pinguino", "gaviota",
    "barco", "velero", "yate", "bote", "remo", "ancla", "timon", "brujula", "mapa", "tesoro",
    "pirata", "marinero", "capitan", "pescador", "buzo", "sirena", "tritón", "nereida", "poseidon", "neptuno"
]

universo = [
    "sol", "luna", "tierra", "marte", "venus", "mercurio", "jupiter", "saturno", "urano", "neptuno",
    "estrella", "planeta", "galaxia", "nebulosa", "cometa", "asteroide", "meteorito", "constelacion", "zodíaco", "aurora",
    "eclipse", "satelite", "astronauta", "cohete", "nave", "estacion", "telescopio", "observatorio", "cosmos", "espacio",
    "orbita", "gravedad", "luz", "energia", "materia", "tiempo", "dimension", "agujero", "big", "bang"
]

escuela = [
    "profesor", "alumno", "estudiante", "director", "maestro", "clase", "aula", "pizarra", "tiza", "borrador",
    "libro", "cuaderno", "lapiz", "boligrafo", "mochila", "regla", "compas", "calculadora", "examen", "tarea",
    "lectura", "escritura", "matematicas", "ciencias", "historia", "geografia", "arte", "musica", "deporte", "recreo",
    "biblioteca", "laboratorio", "gimnasio", "cafeteria", "patio", "pasillo", "salon", "oficina", "baño", "escalera"
]

# Absolute final categories
familia = [
    "padre", "madre", "hijo", "hija", "hermano", "hermana", "abuelo", "abuela", "tio", "tia",
    "primo", "prima", "sobrino", "sobrina", "nieto", "nieta", "esposo", "esposa", "cuñado", "cuñada",
    "suegro", "suegra", "yerno", "nuera", "padrino", "madrina", "ahijado", "ahijada", "familia", "pariente",
    "bebe", "niño", "joven", "adulto", "anciano", "gemelo", "mellizo", "adoptado", "padrastro", "madrastra"
]

casa = [
    "cocina", "salon", "comedor", "dormitorio", "baño", "terraza", "balcon", "jardin", "garage", "sotano",
    "techo", "pared", "suelo", "ventana", "puerta", "escalera", "pasillo", "chimenea", "desvan", "bodega",
    "entrada", "salida", "recibidor", "vestibulo", "despensa", "lavadero", "trastero", "biblioteca", "estudio", "oficina",
    "habitacion", "alcoba", "suite", "buhardilla", "atico", "sotano", "patio", "porche", "veranda", "pergola"
]

cuerpo = [
    "cabeza", "cara", "ojos", "nariz", "boca", "orejas", "cuello", "hombros", "brazos", "manos",
    "dedos", "pecho", "espalda", "cintura", "cadera", "piernas", "rodillas", "pies", "tobillo", "codo",
    "muñeca", "uñas", "pelo", "dientes", "lengua", "mejilla", "frente", "barbilla", "cejas", "pestañas",
    "corazon", "pulmon", "higado", "riñon", "cerebro", "estomago", "intestino", "musculo", "hueso", "arteria"
]

redes = [
    "facebook", "instagram", "twitter", "youtube", "tiktok", "whatsapp", "telegram", "linkedin", "pinterest", "snapchat",
    "reddit", "twitch", "discord", "skype", "zoom", "gmail", "outlook", "yahoo", "hotmail", "messenger",
    "internet", "wifi", "datos", "red", "conexion", "perfil", "usuario", "cuenta", "contraseña", "email",
    "mensaje", "chat", "video", "foto", "audio", "streaming", "viral", "tendencia", "hashtag", "meme"
]

# Very last categories
numeros = [
    "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
    "once", "doce", "trece", "catorce", "quince", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta",
    "setenta", "ochenta", "noventa", "cien", "mil", "millon", "primero", "segundo", "tercero", "ultimo",
    "par", "impar", "mitad", "doble", "triple", "suma", "resta", "multiplicacion", "division", "igual"
]

tiempo = [
    "segundo", "minuto", "hora", "dia", "semana", "mes", "año", "decada", "siglo", "milenio",
    "ayer", "hoy", "mañana", "amanecer", "mediodia", "tarde", "anochecer", "noche", "alba", "ocaso",
    "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo", "enero", "febrero", "marzo",
    "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre", "calendario"
]

# Absolute final categories
verbos = [
    "ser", "estar", "hacer", "tener", "poder", "querer", "decir", "ver", "dar", "saber",
    "ir", "venir", "poner", "salir", "pasar", "deber", "hablar", "llevar", "dejar", "seguir",
    "encontrar", "pensar", "quedar", "parecer", "conocer", "creer", "pedir", "perder", "esperar", "buscar",
    "sentir", "vivir", "escuchar", "mirar", "trabajar", "jugar", "caminar", "correr", "bailar", "cantar"
]

adjetivos = [
    "grande", "pequeño", "alto", "bajo", "gordo", "delgado", "fuerte", "debil", "rapido", "lento",
    "bueno", "malo", "feliz", "triste", "alegre", "serio", "divertido", "aburrido", "facil", "dificil",
    "bonito", "feo", "nuevo", "viejo", "joven", "antiguo", "moderno", "clasico", "rico", "pobre",
    "caliente", "frio", "dulce", "amargo", "suave", "duro", "limpio", "sucio", "claro", "oscuro"
]

# Last small category
hogar = [
    "casa", "hogar", "familia", "mascota", "jardin", "patio", "garaje", "cocina", "salon", "comedor",
    "dormitorio", "baño", "ducha", "bañera", "espejo", "cama", "sofa", "silla", "mesa", "armario",
    "television", "radio", "telefono", "internet", "wifi", "luz", "agua", "gas", "calefaccion", "aire",
    "ventilador", "aspiradora", "plancha", "lavadora", "secadora", "lavavajillas", "microondas", "horno", "nevera", "congelador"
]

def assign_difficulty(word):
    """Assign difficulty based on word length and complexity"""
    if len(word) <= 5:
        return "facil"
    elif len(word) <= 8:
        return "medio"
    else:
        return "dificil"

def generate_words():
    """Generate words with categories and difficulties"""
    categories = {
        "películas": peliculas,
        "acciones": acciones,
        "naturaleza": naturaleza,
        "conceptos": conceptos,
        "objetos": objetos,
        "profesiones": profesiones,
        "lugares": lugares,
        "ciencia": ciencia,
        "música": musica,
        "tecnología": tecnologia,
        "comida": comida,
        "animales": animales,
        "emociones": emociones,
        "deportes": deportes,
        "arte": arte,
        "mitología": mitologia,
        "historia": historia,
        "instrumentos": instrumentos,
        "ropa": ropa,
        "herramientas": herramientas,
        "plantas": plantas,
        "transporte": transporte,
        "bebidas": bebidas,
        "juegos": juegos,
        "colores": colores,
        "muebles": muebles,
        "oficina": oficina,
        "cocina": cocina,
        "personajes": personajes,
        "deportistas": deportistas,
        "celebridades": celebridades,
        "festividades": festividades,
        "clima": clima,
        "países": paises,
        "ciudades": ciudades,
        "baile": baile,
        "medicina": medicina,
        "materiales": materiales,
        "insectos": insectos,
        "flores": flores,
        "mar": mar,
        "universo": universo,
        "escuela": escuela,
        "familia": familia,
        "casa": casa,
        "cuerpo": cuerpo,
        "redes": redes,
        "números": numeros,
        "tiempo": tiempo,
        "verbos": verbos,
        "adjetivos": adjetivos,
        "hogar": hogar
    }
    
    words = []
    for categoria, palabras in categories.items():
        for palabra in palabras:
            words.append({
                "palabra": palabra,
                "categoria": categoria,
                "dificultad": assign_difficulty(palabra)
            })
    
    return words

def main():
    # Read existing words
    with open('palabras.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        existing_words = {word["palabra"] for word in data["palabras"]}
    
    # Generate new words
    new_words = [word for word in generate_words() if word["palabra"] not in existing_words]
    
    # Combine existing and new words
    data["palabras"].extend(new_words)
    
    # Write back to file
    with open('palabras.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main() 