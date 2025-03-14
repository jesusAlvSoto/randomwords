$(document).ready(function() {
    let words = null;
    const STORAGE_KEY = 'usedWords';
    const GITHUB_JSON_URL = 'https://raw.githubusercontent.com/jesusAlvSoto/randomwords/master/palabras.json';

    // Initialize used words from localStorage
    let usedWords = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

    // Fetch words from GitHub
    function fetchWords() {
        return $.getJSON(GITHUB_JSON_URL)
            .then(data => {
                words = data;
                return data;
            })
            .catch(error => {
                console.error('Error fetching words:', error);
                $('#word').html('<span style="color: red; font-size: 1.5rem;">Error cargando palabras. Por favor, recarga la página.</span>');
            });
    }

    // Get random word based on difficulty
    function getRandomWord(difficulty) {
        if (!words) return null;

        let availableWords;
        if (difficulty === 'mezcladas') {
            availableWords = [
                ...words.palabras.facil,
                ...words.palabras.medio,
                ...words.palabras.dificil
            ];
        } else {
            availableWords = words.palabras[difficulty];
        }

        // Filter out used words
        const unusedWords = availableWords.filter(word => !usedWords.includes(word.palabra));

        // If all words have been used, clear the used words list
        if (unusedWords.length === 0) {
            usedWords = [];
            localStorage.setItem(STORAGE_KEY, JSON.stringify(usedWords));
            return getRandomWord(difficulty);
        }

        // Get random word from unused words
        const randomIndex = Math.floor(Math.random() * unusedWords.length);
        const selectedWord = unusedWords[randomIndex];

        // Add to used words
        usedWords.push(selectedWord.palabra);
        localStorage.setItem(STORAGE_KEY, JSON.stringify(usedWords));

        return selectedWord;
    }

    // Display new word with animation
    function displayNewWord() {
        const difficulty = $('#difficulty').val();
        const word = getRandomWord(difficulty);
        
        if (word) {
            $('#word')
                .hide()
                .text(word.palabra)
                .removeClass()
                .addClass('word-display animate__animated animate__bounceIn')
                .show();
        }
    }

    // Event Handlers
    $('#start-btn').click(function() {
        fetchWords().then(() => {
            $('#landing-page').hide();
            $('#game-page').show();
            displayNewWord();
        });
    });

    $('#generate-btn').click(function() {
        displayNewWord();
    });

    $('#difficulty').change(function() {
        displayNewWord();
    });

    $('#clear-storage').click(function() {
        localStorage.removeItem(STORAGE_KEY);
        usedWords = [];
        $(this).addClass('animate__animated animate__fadeOut');
        setTimeout(() => {
            $(this).text('¡Almacenamiento borrado!');
            $(this).removeClass('animate__fadeOut').addClass('animate__fadeIn');
            setTimeout(() => {
                $(this).text('Borrar almacenamiento local');
                $(this).removeClass('animate__fadeIn');
            }, 2000);
        }, 500);
    });
}); 