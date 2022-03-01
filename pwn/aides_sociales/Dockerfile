FROM ubuntu:21.10

RUN apt update && apt upgrade -qqy
RUN apt install -qqy socat
RUN useradd -m ctf
WORKDIR /home/ctf


COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
COPY ./dist/* /home/ctf/

RUN chmod +x /start.sh

RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf
RUN chown 750 /home/ctf/challenge
RUN chown 750 /home/ctf/flag.txt
RUN chmod +x /home/ctf/challenge

EXPOSE 55555

ENTRYPOINT ["/start.sh"]
