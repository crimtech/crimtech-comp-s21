// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

function search() {
    if (event.key === 'Enter') {
        response()
    }
}

function response() {
    // Your Code Here
    input = document.getElementById("desc").value
    document.getElementById("desc").value = ''
    console.log(input);

    imgs = [[['regular-std', 'cute-std'], ['regular-std', 'cute-std']],
            [['regular-force', 'cute-force'], ['regular-dark', 'cute-dark']]]
    quotes = [dark_quotes, force_quotes, std_quotes]
    hm = ['', ' Yes, h' + 'm'.repeat(Math.floor(Math.random() * 10) + 10)]

    img = ''
    quote = ''

    baby = input.includes('cute') || input.includes('baby')
    force = input.includes('force')
    dark = input.includes('dark')
    img = imgs[+ force][+ dark][+ baby]
    if (baby) {
        quote = hm[1]
    }
    else {
        quote = random_choice(quotes[force ? (dark ? 0 : 1) : 2]) + random_choice(hm)
    }

    document.getElementById("yoda_pic").setAttribute("src", "img/" + img + ".jpg")
    document.getElementById("yoda_text").textContent = quote
}

function random_choice(lst) {
    return lst[Math.floor(Math.random() * lst.length)]
}