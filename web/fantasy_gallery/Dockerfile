FROM python:latest

# Install package dependences
RUN apt -y -qq update;\
    apt -y -qq install sqlite3;

# Copy flask files
WORKDIR /usr/app
ADD ./src/ .

# Install app requirements
RUN sqlite3 sqlite.db < init.sql; \
    python -m pip install -r requirements.txt;
RUN sed -i 's/R2Lille{SQL1_4r3_3v3ryWh3R3}/\*sensored\*/g' init.sql; \
    sed -i 's/flag_is/\*sensored\*/g' init.sql;

# Start flask srv on any local IP
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]
