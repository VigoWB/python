FROM docker.io/node:18.13.0

ARG email="vigo@example.com"
LABEL maintainer=$email
LABEL "rating"="Piec Gwiazdek" "class"="Pierwsza Klasa"

USER root

ENV AP /data/app
ENV SCPATH /etc/supervisor/comf.d

RUN apt-get -y update

# demony
RUN apt-get -y install supervisor
RUN mkdir -p /var/log/supervisor


# konfiguracja supervisora
COPY ./supervisord/conf.d/* $SCPATH/

#kod aplikacji
COPY *.js* $AP/

WORKDIR $AP

RUN npm install

CMD ["supervisord", "-n"]