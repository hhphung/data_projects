data projects building ETL pipeline to extract data sources, transform, and load them into a new database. These projects including learning new technologies

1. 



2. This code is a Docker command that runs a container based on the PostgreSQL 13 image. This is run in git bash

winpty docker run -it \    # this command is used to run a Docker container
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="Vietnam#1" \
    -e POSTGRESS_BD="LOCAL \
    -v /c/Users/Hoi Phung/data_projects/Docker_pipeline/ny_taxi_postgress_data:/var/lib/postgresql/data \   #Mounts a volume from the host machine to the container. This is used to persist the PostgreSQL data. 
    -p 5432:5432 \  #port
    postgress: 13   #PostgreSQL version 13.


3. pgcli: library in library pytthon that help to access postgresql db as an interface.

4: jupyter