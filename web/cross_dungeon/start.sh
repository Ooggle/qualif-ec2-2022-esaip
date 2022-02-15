#!/bin/bash

# Starting bot in background
/usr/bin/node /usr/app/bot/client_bot.js &

# Starting web serveur
cd /usr/app/src
flask run --host=0.0.0.0 --port=80
