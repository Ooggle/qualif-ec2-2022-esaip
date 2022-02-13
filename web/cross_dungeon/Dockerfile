FROM python:latest

# Install package dependences
RUN apt -y -qq update; \
    apt -y -qq install sqlite3 nodejs npm;

# Chrome driver installation
RUN apt install alsa-topology-conf alsa-ucm-conf fonts-liberation libasound2 libasound2-data libgbm1 libnspr4 libnss3 libwayland-server0; \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/chrome.deb; \
    dpkg -i /tmp/chrome.deb;

# Install npm packages & bot files
WORKDIR /usr/app/bot
ADD ./bot .
RUN npm install --save puppeteer; \
    npm install --save sqlite3;

# Copy flask files
WORKDIR /usr/app/src
ADD ./src .

# Init sqlite database
RUN sqlite3 sqlite.db < init.sql; \
    python -m pip install -r requirements.txt;

# Start bot
RUN /bin/node /usr/app/bot/client_bot.js &

# Start flask srv on any local IP
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]
