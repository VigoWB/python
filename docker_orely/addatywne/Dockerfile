FROM docker.io/fedora
RUN dnf install -y httpd && \
    dnf clean all
#RUN dnf clean all
CMD ["/usr/sbin/httpd","DFOREGROUND"]
LABEL authors="Wiktor"


#polecenie && jest kluczowe dziala na zasadzie AND nie rozdziela warstw
#bo jak rozdzieli to juz nie da sie zedytowac