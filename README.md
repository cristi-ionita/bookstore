# Book store project

## Stack of technologies:
* Code:
    * FastApi
    * SqlAlchemy
    * Alembic
* Infrastructure:
    * Docker
    * Docker-compose
    * PostgreSQL

## How setup project
1. Make sure that you have pyenv to manage python versions easy in OS
2. Make sure that you have poetry installed to manage python packages easy in project
3. Make sure that you have docker and docker compose installed on system
4. Make sure that you have make installed in system to be able run targets
5. Run target:
```
make install_pre_commit
```
6. Make sure you are in root folder of the project
7. Activate environment
```
pyenv env activate
```
8. Install all dependencies for project:
```
poetry install
```

## How to run project
1. Run api locally and db in docker container:
```
make run_locally
```

2. Run everything in docker containers: TBD