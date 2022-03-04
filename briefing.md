Les observations :

CTFd parse mal les flags avec des virgules

On a eu un down du CTFd pendant env. 2min 20 minutes après le début du CTF. Peut-être à cause d'une montée en charge automatique d'Azure ?

Penser à compiler les binaires de reverse de pwn en statique pour permettre l'exécution et du reverse dynamique (même si des mitigations anti-debugging ont été mises en place {pour mettre tout le monde sur le même pied d'égalité si le version de la libc est trop haute})
