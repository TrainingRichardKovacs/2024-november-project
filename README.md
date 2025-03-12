Hogyan futtasd Dockerizálva a loadert, ha buildelted az imaget:

docker network create mynetwork

docker run -it --rm --name mydataloader     --network mynetwork     docker_data_loader:1.1

docker run -d 
--name mypostgres 
--network mynetwork 
-e POSTGRES_USER=postgres
-e POSTGRES_PASSWORD=postgres 
-e POSTGRES_DB=postgres
-p 5433:5432 postgres:latest


