# poc-isochrones

PoC around Isochrones using Open Route Service and Python with FastAPI

## Running the application

### Locally (with reload)

#### Pre-configuration

```bash
# Install virtualenvwrapper
brew install virtualenvwrapper

# Create new Virtual Environment
mkvirtualenv isochrones

# Set up you environment
workon isochrones

# Install requirements
pip install -r requirements.txt
```

Don't forget to export the environment variables if you are going to run it locally!
The code that does that is commented in the database.config class.

Please notice that at least the postgres container should be running, and the tables/extensions must be added.

To run on VS Code, please update the Interpreter Path to the current virtual env.

- `which python` to find out the path to the venv (after workon command)
- VS Code Settings > Python > Default Interpreter Path

#### Initialising app

```bash
uvicorn app.main:app --reload
```

Access it on [localhost](http://127.0.0.1:8000/).

### With Docker Compose

```bash
# Starting
docker-compose up -d --build --remove-orphans

# Stopping
docker-compose down -v

```

Now you can access the API via [localhost proxy url](http://isochrones-api.localhost:8008/).

Accessing pgAdmin: [link](http://localhost:5050/).

- email: admin@admin.com
- password: root

Create a server on pgAdmin:

- In general tab create a server name
- Host name/address: pg_container
- User name: root
- Password: root

[Github Repository](https://github.com/livia-delgado-kr/poc-postgres-isochrone)

## Useful links

- [Virtualenvwrapper Documentation](https://virtualenvwrapper.readthedocs.io/en/latest/)
- [Virtualenvwrapper Brew Install](https://formulae.brew.sh/formula/virtualenvwrapper)
- [FastAPI + Docker + Traefik configuration](https://testdriven.io/blog/fastapi-docker-traefik/)
- [Running SQL Files in PostgreSQL](https://kb.objectrocket.com/postgresql/how-to-run-an-sql-file-in-postgres-846)
- [Executing script in Postgres DB with docker-compose](https://levelup.gitconnected.com/creating-and-filling-a-postgres-db-with-docker-compose-e1607f6f882f)
- [PostgreSQL Queries with Python](https://www.postgresqltutorial.com/postgresql-python/insert/)
- [Postgis with Python](https://pypi.org/project/postgis/)
- [Docker Compose - PostgreSQL](https://graspingtech.com/docker-compose-postgresql/)
