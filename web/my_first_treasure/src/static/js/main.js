// Init
texts = ["An enemy approch!", "You found a chest!", "Wait this is realy a flag?!", "Nice sword man!", "Hé ho hé", "Tutuluuu!", "You found a cool shield!", "10 rupees for the beer!"]

function getRandomInt(max) {
	return Math.floor(Math.random() * max);
}

// Write console msg 
var write = () => {
	x = getRandomInt(texts.length)
    console.log(texts[x])
};

// Infinity run
setInterval(write, 10000);

// Part 3: NG_HTML
// Robots seems to have steal admin credentials, please help me to find them back
