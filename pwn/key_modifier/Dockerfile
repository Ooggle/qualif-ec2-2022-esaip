FROM ubuntu:21.10

RUN apt update && apt upgrade -qqy
RUN apt install -qqy socat
RUN useradd -m ctf
WORKDIR /home/ctf


COPY ./start.sh /start.sh
COPY ./src/challenge /home/ctf/
COPY ./src/flag.txt /home/ctf/

RUN chmod +x /start.sh

RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf

EXPOSE 55556

ENTRYPOINT ["/start.sh"]
