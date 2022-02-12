/*
Default value for hit bar is 95% to avoid longest bar prob
*/

// Init

// Allow attack
var allow_attack = true;

// Possible ganon action
var ganon_action = ["Sword", "Shield", "Potion"];
document.body.onload = function() {
    // Personnage
    const link = document.getElementById("link");
    const ganon = document.getElementById("enemy");

    // Animation zone
    var battle = document.getElementById("battle");

    // link bar
    const link_health = document.getElementById("link_health");
    const link_hit = document.getElementById("link_hit");

    // Enemy bar
    const ganon_health = document.getElementById("enemy_health");
    const ganon_hit = document.getElementById("enemy_hit");

    // Score
    const ganon_victory = document.getElementById("link_victory");
    const link_victory = document.getElementById("link_victory");
};

// Functions
var getRandomInt = (max) => {
    return Math.floor(Math.random() * max);
}

var make_damage = (damage, from, type) => {
    // Select ganon action
    if(from === "Link") {
        ganon_attack = ganon_action[getRandomInt(3)];
    };

    // Start battle
    if(allow_attack || from === "Ganon") {
        allow_attack = false;

        // Animation
        if(from === "Link" && type === "Sword") {
            link.style.paddingLeft = "10%";
            battle.innerHTML = '<img src="/static/images/green_damage.png">';
        } else if(from === "Link" && type === "Shield") {
            battle.innerHTML = '<img src="/static/images/green_damage.png">';
        } else if(from === "Link" && type === "Potion") {
            battle.innerHTML = '<img src="/static/images/green_heal.png">';
        } else if(from == "Ganon" && type === "Sword") {
            ganon.style.paddingRight = "10%";
            battle.innerHTML = '<img src="/static/images/red_damage.png">';
        } else if(from === "Ganon" && type === "Shield") {
            battle.innerHTML = '<img src="/static/images/red_damage.png">';
        } else if(from === "Ganon" && type === "Potion") {
            battle.innerHTML = '<img src="/static/images/red_heal.png">';
        }

        // Current values
        // Health
        if(from === "Link" && type !== "Potion") {
            var current_health = ganon_health.style.width;
        } else if(from === "Link" && type === "Potion") {
            var current_health = link_health.style.width;
        } else if(from === "Ganon" && type !== "Potion") {
            var current_health = link_health.style.width;
        } else if(from === "Ganon" && type === "Potion") {
            var current_health = ganon_health.style.width;
        };
        if(current_health === ""){
            current_health = "100%";
        };
        // Hit
        if(from === "Link" && type !== "Potion") {
            var current_hit = ganon_hit.style.width;
        } else if(from === "Link" && type === "Potion") {
            var current_hit = link_hit.style.width;
        } else if(from === "Ganon" && type !== "Potion") {
            var current_hit = link_hit.style.width;
        } else if(from === "Ganon" && type === "Potion") {
            var current_hit = ganon_hit.style.width;
        };
        if(current_hit === ""){
            current_hit = "95%";
        };

        // Compute values
        if(type !== "Potion") {
            var new_health = parseInt(current_health) - damage;
            var new_hit = parseInt(current_hit) - damage;
        } else {
            var new_health = parseInt(current_health) + damage;
            var new_hit = parseInt(current_hit) + damage;
        }
        if(new_health < 0) {
            new_health = "0%";
            new_hit = "0%";
        } else if(new_health > 100) {
            new_health = "100%";
            new_hit = "95%";
        } else {
            new_health = `${new_health}%`;
            new_hit = `${new_hit}%`;
        };

        // Update
        //Health
        if(type !== "Potion"){
            if(from === "Link") {
                ganon_health.style.width = new_health
            } else if(from === "Ganon") {
                link_health.style.width = new_health
            }; 
        } else {
            if(from === "Link") {
                link_health.style.width = new_health
            } else if(from === "Ganon") {
                ganon_health.style.width = new_health
            }; 
        }

        setTimeout(() => {
            // Hit
            if(type !== "Potion"){
                if(from === "Link") {
                    ganon_hit.style.width = new_hit
                } else if(from === "Ganon") {
                    link_hit.style.width = new_hit
                }; 
            } else {
                if(from === "Link") {
                    link_hit.style.width = new_hit
                } else if(from === "Ganon") {
                    ganon_hit.style.width = new_hit
                }; 
            }

            // Remove animation
            ganon.style.paddingRight = "0%";
            link.style.paddingLeft = "0%";

            // Check for victory
            if (new_health === "0%") {
                battle.innerHTML = `<p class="mgb-0-5">${from} win the battle!</p>
                <button id="btn-reset" onclick="reset()">reset</button>`;
                if(from === "Link") {
                    link_victory.innerHTML = `Link victory: ${parseInt(link_victory.innerHTML.split(" ")[2]) + 1}`;
                } else if(from === "Ganon") {
                    ganon_victory.innerHTML = `Ganon victory: ${parseInt(ganon_victory.innerHTML.split(" ")[2]) + 1}`;
                }; 
                allow_attack = false;
                return
            } else {
                battle.innerHTML = ""
            }

            // ganon attack back
            if(from === "Link") {
                setTimeout(() => {
                    if(type === "Shield") {
                        make_damage(0, "Ganon", ganon_attack);
                    } else {
                        make_damage(getRandomInt(100), "Ganon", ganon_attack);
                    }

                    allow_attack = true;
                }, 500);
            } else if(from === "Link" && type === "Shield") {
                allow_attack = true;
            };
        }, 500);
    };
};

var reset = () => {
    allow_attack = true;
    battle.innerHTML = ""
    ganon_hit.style.width = "95%";
    link_hit.style.width = "95%";
    setTimeout(() => {
        ganon_health.style.width = "100%";
        link_health.style.width = "100%";
    }, 500);
};
