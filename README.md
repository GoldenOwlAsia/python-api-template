# Flask Boilerplate

## Getting Started

### Prerequisites

- Python version: `> python 3.9.5`
- Flask version: `2.2.3`
- Database: `postgresql`

## Installation

- Clone the repository: `git clone https://github.com/GoldenOwlAsia/python-flask-api-template.git`
- Initalize virtual environment: `python3 0m venv venv`
- Activate virtual environment: `source venv/bin/activate`
- Go to python-fast-api-template folder: `cd ./python-fast-api-template`
- Install the dependencies: `pip install -r requirements.txt`
- Create .env file:
```
FLASK_DEBUG=1 or 0
APP_CONFIG=development or production
FLASK_RUN_PORT=5000
SENTRY_KEY=
```
- Create database by docker command: `docker run --name flask -p 5435:5432 -e POSTGRES_PASSWORD=flask -e POSTGRES_USER=flask -e POSTGRES_DB=flask -d postgres:14`
- Turn to line 63 in `alembic.ini` file, change the value follows this structure : postgresql://POSTGRES_USER:POSTGRES_PASSWORD@POSTGRES_HOST:POSTGRES_PORT/POSTGRES_DB
- Run migration: `alembic upgrade head`
- Export env : 
    -   `export FLASK_APP=app/app.py`
- Run application: `flask run --no-debugger ----no-reload`
- Visit `http://127.0.0.1:5000` and start your development
## API documentation

- Visit `http://127.0.0.1:8000/docs` to watch API documentation

## Testing

- python3 -m unittest

## Database diagram

![Database diagram](db_diagram.png)
