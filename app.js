$(document).ready(function() {
    // Player counter logic
    function getRandomNumber(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    let isIncreasing = true;

    function updatePlayerCount() {
        const currentCount = parseInt($('#players-count').text());
        const change = getRandomNumber(1, 20);
        const newCount = isIncreasing ? currentCount + change : currentCount - change;
        
        // Ensure count stays within bounds (1000-5000)
        const boundedCount = Math.min(Math.max(newCount, 1000), 5000);
        $('#players-count').text(boundedCount);
        
        // Toggle between increasing and decreasing
        isIncreasing = !isIncreasing;
    }

    // Initialize with random number between 1000 and 5000
    $('#players-count').text(getRandomNumber(1000, 5000));

    // Update count every 10 seconds
    setInterval(updatePlayerCount, 10000);

    let words = null;
    let currentWord = null;
    let wordCounter = 0;
    const STORAGE_KEY = 'usedWords';
    const GITHUB_JSON_URL = 'https://raw.githubusercontent.com/jesusAlvSoto/randomwords/master/palabras.json';

    // Initialize used words from localStorage
    let usedWords = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

    // Difficulty labels in Spanish
    const difficultyLabels = {
        'facil': 'Fácil',
        'medio': 'Media',
        'dificil': 'Difícil'
    };

    // Update past words list display
    function updatePastWordsList() {
        const $list = $('#past-words-list');
        const $clearButton = $('#clear-list');
        $list.empty();
        
        // Show words with their numbers
        const pastWords = usedWords.map((word, index) => 
            `<div>#${index + 1} - ${word}</div>`
        ).reverse();
        
        if (pastWords.length === 0) {
            $list.html('<div class="text-center text-muted">No hay palabras pasadas</div>');
            $clearButton.hide();
        } else {
            $list.html(pastWords.join(''));
            $clearButton.show();
        }
    }

    // Find word object from words list
    function findWordObject(palabra) {
        if (!words) return null;
        
        for (const difficulty in words.palabras) {
            const found = words.palabras[difficulty].find(w => w.palabra === palabra);
            if (found) return found;
        }
        return null;
    }

    // Fetch words from GitHub
    function fetchWords() {
        return $.getJSON(GITHUB_JSON_URL)
            .then(data => {
                words = data;
                return data;
            })
            .catch(error => {
                console.error('Error fetching words:', error);
                $('#word .word-text').html('<span style="color: red; font-size: 1.5rem;">Error cargando palabras. Por favor, recarga la página.</span>');
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

        // Add current word to used words if it exists
        if (currentWord) {
            usedWords.push(currentWord.palabra);
            localStorage.setItem(STORAGE_KEY, JSON.stringify(usedWords));
            updatePastWordsList();
        }

        // Filter out used words
        const unusedWords = availableWords.filter(word => !usedWords.includes(word.palabra));

        // If all words have been used, clear the used words list
        if (unusedWords.length === 0) {
            usedWords = [];
            localStorage.setItem(STORAGE_KEY, JSON.stringify(usedWords));
            wordCounter = 0;
            return getRandomWord(difficulty);
        }

        // Get random word from unused words
        const randomIndex = Math.floor(Math.random() * unusedWords.length);
        const selectedWord = unusedWords[randomIndex];

        return selectedWord;
    }

    // Display new word with animation
    function displayNewWord() {
        const difficulty = $('#difficulty').data('value') || 'mezcladas';
        const word = getRandomWord(difficulty);
        
        if (word) {
            currentWord = word;
            wordCounter++;

            // Update the title
            $('#main-title')
                .removeClass()
                .addClass('main-title game-mode text-center animate__animated animate__fadeIn')
                .text(`Palabra #${wordCounter}`);

            // Display the word
            $('#word')
                .hide()
                .removeClass()
                .addClass('word-display animate__animated animate__bounceIn');

            $('.word-text').text(word.palabra);
            $('.word-difficulty-label').text(difficultyLabels[word.dificultad]);

            $('#word').show();
        }
    }

    // Event Handlers
    $('#start-btn').click(function() {
        fetchWords().then(() => {
            $('#landing-page').fadeOut(400, function() {
                $('#game-page').fadeIn(400);
                displayNewWord();
                updatePastWordsList();
            });
        });
    });

    $('#generate-btn').click(function() {
        displayNewWord();
    });

    $('#difficulty').change(function() {
        if ($('#game-page').is(':visible')) {
            displayNewWord();
        }
    });

    $('#clear-list').click(function() {
        localStorage.removeItem(STORAGE_KEY);
        usedWords = [];
        currentWord = null;
        wordCounter = 0;
        updatePastWordsList();
        $(this).addClass('animate__animated animate__fadeIn');
        setTimeout(() => {
            $(this).removeClass('animate__fadeIn');
        }, 500);
    });

    // Handle dropdown item clicks
    $('.dropdown-item').click(function(e) {
        e.preventDefault();
        const value = $(this).data('value');
        const text = $(this).text();
        
        // Update button text and value
        $('#difficulty')
            .text(text)
            .data('value', value);
        
        // Update active state
        $('.dropdown-item').removeClass('active');
        $(this).addClass('active');
    });
}); 