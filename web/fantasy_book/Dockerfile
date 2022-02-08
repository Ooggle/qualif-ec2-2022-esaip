FROM python:latest

# Install package dependences
RUN apt -y -qq update;

# Copy flag
ADD flag.txt /flag.txt

# Copy flask files
WORKDIR /usr/app
ADD ./src/ .

# Install python requirements
RUN python -m pip install -r requirements.txt;

# Start flask srv on any local IP
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]
