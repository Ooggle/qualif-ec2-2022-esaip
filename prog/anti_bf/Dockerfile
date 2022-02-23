FROM python:3.9.7

# Install package dependences
RUN apt -y -qq update;

# Copy flask files
WORKDIR /usr/app
ADD ./src/ .

# Install python requirements
RUN python -m pip install -r requirements.txt;

# Start flask srv on any local IP
CMD [ "python", "app.py" ]
