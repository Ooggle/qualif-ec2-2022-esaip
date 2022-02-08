FROM python:latest

# Install package dependences
RUN apt -y -qq update;

# Copy challenge files
WORKDIR /usr/app
ADD ./src/run.py .
ADD ./src/requirements.txt .

# Install python requirements
RUN python -m pip install -r requirements.txt;

# Start flask srv on any local IP
CMD [ "python", "run.py" ]
