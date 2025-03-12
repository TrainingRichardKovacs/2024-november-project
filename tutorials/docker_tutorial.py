"""
Docker

Containerization technológia
Platformfüggetlen módon tudjunk applikációkat, adatbázisokat,
egyéb szoftverkomponenseket elindítani / hostolni / telepíteni.

Nem lokálisan telepíted fel az applikációkat, hanem a Docker által nyújtott 
úgynevezett konténerekben fogod betelepíteni.

A Docker-t egy Dockerfile nevű paraméterfile-al hozod létre
és rengeteg megoldás van arra a piacon, hogy ezeket a Dockerfile-okat 
megfelelően tudjuk kezelni / üzemeltetni.

Docker Desktop - UI
 - Docker CLI - parancssorból vezérelhető inteface

Docker flow:

1. flow: Custom image-et haszálsz
    1. lebuildeled a Dockerfile-t docker build -> docker image
    2. docker run image -> docker container -> 
           -> a container a végső állapot, ez már a containerizált service / app / adatbázis

2. flow: meglévő image-t használsz
    1. docker pull -> letöltőd a Dockerhub-ról, vagy valamilyen egyéb repository-ból a már előre buildelt image-t
    2. docker run image -> docker container -> 
           -> a container a végső állapot, ez már a containerizált service / app / adatbázis
 
Docker Daemon - a lelke a Docker-nek
                    
###############################################################################
Custom Dockerfile:

from base_image
parancsok

###############################################################################

"""