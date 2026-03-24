# The Void 

A screen-free, AI-assisted memo app

## To run:

- Clone this repo
- make a `.env` file that follows the `.env-example` template
- run `docker compose up`
- Open a browser at `localhost:8002`

## Architecture

- The app is written using <https://www.djangoproject.com/>, and 
    - served via 
<https://gunicorn.org/>
    - with <https://whitenoise.readthedocs.io/en/latest/> for static files
- Database backend is <https://www.postgresql.org/download/>
- The docker-compose.yml spins up the app and the database in separate containers
and establishes the network connection between them