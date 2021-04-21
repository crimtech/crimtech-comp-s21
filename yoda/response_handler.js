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

function respond() {
    // Your Code Here
    //console.log("Hello World!");
    //document.getElementById("yodathought").innerHTML = dark_quotes[0]
    //console.log(document.getElementById("entry").value)
    
    var input = document.getElementById("entry").value;
    var pic = document.getElementById("yodapic");
    var text = "";

    if (input.includes("baby") || input.includes("cute")) {
        pic.setAttribute("src", "img/cute-std.jpg");
    }
    else if (input.includes("force") && input.includes("dark")) {
        pic.setAttribute("src", "img/regular-dark.jpg");
        var text = dark_quotes[Math.floor(Math.random()*dark_quotes.length)];
    }
    else if (input.includes("force")) {
        pic.setAttribute("src", "img/regular-force.jpg");
        var text = force_quotes[Math.floor(Math.random()*force_quotes.length)];
    }
    else {
        pic.setAttribute("src", "img/regular-std.jpg");
        var text = std_quotes[Math.floor(Math.random()*std_quotes.length)];
    }
    var str = " hm";
    for (i = 0; i < range(Math.floor(Math.random() * 50)); i++) {
        str = str.concat("m");
    }
    document.getElementById("yodathought").innerHTML = text.concat(str);
}