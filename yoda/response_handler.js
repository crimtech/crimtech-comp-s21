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
    console.log("Hello World!");
    // var a = document.getElementById("yodaimg")
    // a.setAttribute("src", "./img/cute-force.jpg");

    // var b = document.getElementById("yodachat")
    // b.textContent="Hehe";

    var txtinput = document.getElementById('myText');
    console.log(txtinput.value); 

    c=txtinput.value
    // console.log(c.search("baby"))

    if (c.search("baby") != -1 || c.search("cute") != -1){
        console.log(" 'baby' or 'cute' detected");
        var a = document.getElementById("yodaimg")
        a.setAttribute("src", "./img/cute-std.jpg");
    }
    if (c.search("force") != -1){
        if (c.search("dark") != -1){
            var a = document.getElementById("yodaimg")
            a.setAttribute("src", "./img/regular-dark.jpg");       
        }
        else{
            var a = document.getElementById("yodaimg")
            a.setAttribute("src", "./img/regular-force.jpg");
        }

    }

    var b = document.getElementById("yodachat");
    random_m = Math.floor(Math.random() * 5);
    console.log(random_m)
    random_list = Math.floor(Math.random() * 3);
    console.log("list: " + random_list)
    random_quote = Math.floor(Math.random() * 5); 
    console.log("list index: " + random_quote)
    mstr=" hmm"
    newstr=""

    for (let i=0; i<random_m; i++){
        mstr=mstr.concat("m");
    }

    if (random_list == 0){
        newstr=dark_quotes[random_quote];
    }
    else if (random_list == 1){
        newstr=force_quotes[random_quote];
    }
    else{
        newstr=std_quotes[random_quote]; 
    }
    console.log("newstr: " + newstr);
    b.textContent= newstr.concat(mstr);

    // c = "example here".search("here");
    // console.log(c);
}