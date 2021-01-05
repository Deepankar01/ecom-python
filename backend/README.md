# Setup

### Steps to run the code

1. install dependencies from `requirements.txt`
2. run migration `alembic upgrade head`
3. database config are in `app.db.database`
4. run `python api.py`
5. open in browser http://0.0.0.0:8000/gq to view gq editor

### Database setup (Postgres Container)

1. `docker run --name some-postgres -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres`
2. create database `ecom`
3. (Use any database tool like DBeaver or pgAdmin)

### TODO

1. Use `.env` variable for the database

### Docs

Head over to the docs folder
