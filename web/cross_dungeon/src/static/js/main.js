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

    // Logs
    const logs = document.getElementById("logs");
};

// Functions
var getRandomInt = (max) => {
    return Math.floor(Math.random() * max);
}

var add_logs = (from, action, damage) => {
    const list_logs = document.querySelectorAll("#log");
    if(list_logs.length === 5) {
        document.querySelectorAll("#log")[0].remove()
    };
    if(action === "Sword") {
        logs.innerHTML += `<p id="log">[${from}] ${action} -${damage}PV</p>`
    } else if(action === "Shield") {
        logs.innerHTML += `<p id="log">[${from}] ${action}</p>`
    } else if(action === "Potion") {
        logs.innerHTML += `<p id="log">[${from}] ${action} +${damage}</p>`
    } else if(action === "Reset") {
        logs.innerHTML += `<p id="log">[${from}] ${action}</p>`
    }
};

var make_damage = (from, action, damage) => {
    // Select ganon action
    if(from === "Link") {
        ganon_attack = ganon_action[getRandomInt(3)];
    };
    if(from === "Link" && action === "Sword" && ganon_attack === "Shield") {
        damage = 0;
    }

    // Start battle
    if(allow_attack || from === "Ganon") {
        // Block attack spaming
        allow_attack = false;

        // Logs
        add_logs(from, action, damage);

        // Animation
        if(from === "Link" && action === "Sword") {
            link.style.paddingLeft = "10%";
            battle.innerHTML = '<img src="/static/images/green_damage.png" width="200px">';
        } else if(from === "Link" && action === "Shield") {
            battle.innerHTML = '<img src="/static/images/green_shield.png" width="200px">';
        } else if(from === "Link" && action === "Potion") {
            battle.innerHTML = '<img src="/static/images/green_heal.png" width="200px">';
        } else if(from == "Ganon" && action === "Sword") {
            ganon.style.paddingRight = "10%";
            battle.innerHTML = '<img src="/static/images/red_damage.png" width="200px">';
        } else if(from === "Ganon" && action === "Shield") {
            battle.innerHTML = '<img src="/static/images/red_shield.png" width="200px">';
        } else if(from === "Ganon" && action === "Potion") {
            battle.innerHTML = '<img src="/static/images/red_heal.png" width="200px">';
        }

        // Current values
        // Health
        if(from === "Link" && action !== "Potion") {
            var current_health = ganon_health.style.width;
        } else if(from === "Link" && action === "Potion") {
            var current_health = link_health.style.width;
        } else if(from === "Ganon" && action !== "Potion") {
            var current_health = link_health.style.width;
        } else if(from === "Ganon" && action === "Potion") {
            var current_health = ganon_health.style.width;
        };
        if(current_health === ""){
            current_health = "100%";
        };
        // Hit
        if(from === "Link" && action !== "Potion") {
            var current_hit = ganon_hit.style.width;
        } else if(from === "Link" && action === "Potion") {
            var current_hit = link_hit.style.width;
        } else if(from === "Ganon" && action !== "Potion") {
            var current_hit = link_hit.style.width;
        } else if(from === "Ganon" && action === "Potion") {
            var current_hit = ganon_hit.style.width;
        };
        if(current_hit === ""){
            current_hit = "95%";
        };

        // Compute values
        if(action !== "Potion") {
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
        if(action !== "Potion"){
            if(from === "Link") {
                ganon_health.style.width = new_health
            } else if(from === "Ganon") {
                link_health.style.width = new_health
            }; 
        } else {
            if(from === "Link") {
                link_hit.style.width = new_hit
            } else if(from === "Ganon") {
                ganon_hit.style.width = new_hit
            }; 
        }

        setTimeout(() => {
            // Hit
            if(action !== "Potion"){
                if(from === "Link") {
                    ganon_hit.style.width = new_hit
                } else if(from === "Ganon") {
                    link_hit.style.width = new_hit
                }; 
            } else {
                if(from === "Link") {
                    link_health.style.width = new_health
                } else if(from === "Ganon") {
                    ganon_health.style.width = new_health
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
                    if(ganon_attack === "Shield") {
                        make_damage("Ganon", ganon_attack, 0);
                    } else {
                        make_damage("Ganon", ganon_attack, getRandomInt(100));
                    }

                    allow_attack = true;
                }, 500);
            } else if(from === "Link" && action === "Shield") {
                allow_attack = true;
            };
        }, 500);
    };
};

var reset = () => {
    // Logs
    add_logs("Info", "Reset", "");
    // Reset
    allow_attack = true;
    battle.innerHTML = ""
    ganon_hit.style.width = "95%";
    link_hit.style.width = "95%";
    // Animation
    setTimeout(() => {
        ganon_health.style.width = "100%";
        link_health.style.width = "100%";
    }, 500);
};
