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
	var imagess = document.getElementById("imagess");
	var newimage = "img/";
	var newtext = "";
	var message = document.getElementById("hello").value;
	if (message.includes("cute") || message.includes("baby")) {
		newimage = newimage.concat("cute");
		if (message.includes("force")) {
			if (message.includes("dark")) {
				newimage = newimage.concat("-dark");
			}
			else {
				newimage = newimage.concat("-force");
			}
		}
		else {
			newimage = newimage.concat("-std");
		}
	}
	else {
		newimage = newimage.concat("regular");
		var quote = getRandomInt(0, 5);
		// put the code for a random quote generator here
		if (message.includes("force")) {
			if (message.includes("dark")) {
				newimage = newimage.concat("-dark");
				newtext = newtext.concat(dark_quotes[quote]);
			}
			else {
				newimage = newimage.concat("-force");
				newtext = newtext.concat(force_quotes[quote]);
			}
		}
		else {
			newimage = newimage.concat("-std");
			newtext = newtext.concat(std_quotes[quote]);
		}
	}

	newimage = newimage.concat(".jpg");
	if (message.includes("strawberry")) {
		newimage = "strawberry.png"
	}
	var hmmm = getRandomInt(1, 20);
	var sayinghm = "m".repeat(hmmm);
	newtext = newtext.concat("h");
	newtext = newtext.concat(sayinghm);

	imagess.setAttribute("src", newimage);
	document.getElementById("textt").innerHTML = newtext;
	document.getElementById("hello").value = "";
	// clear out the value of the textbox
}

function getRandomInt(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max - min)) + min;
}