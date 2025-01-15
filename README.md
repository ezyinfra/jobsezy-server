# Jobs Ezy

Jobs Ezy is an application that allows users to search for jobs and apply to them.

This is a sample project that accompanies [AWS Bootcamp](https://aws.amazon.com/bootcamp/) created as part of [EzyInfra](https://ezyinfra.dev/)

This is the Python based backend service and you can find the frontend application [here](https://github.com/ezyinfra/jobs-ezy-frontend)

## Technologies Used

1. [FastAPI](https://fastapi.tiangolo.com/)
2. [Poetry](https://python-poetry.org/)
3. [SQLAlchemy](https://www.sqlalchemy.org/)
4. [PostgreSQL](https://www.postgresql.org/)

## Follow the steps to run the application in your local machine

### Installation

1. Clone the repository
2. Install Poetry using the command `pip install poetry`
3. Install Postgres database from their [homepage](https://www.postgresql.org/) or use Docker container to start the postgres database
4. Create the database - `jobsezy` using the command `createdb jobsezy`
5. Copy the `.env.example` file to `.env` and update the database URL with your database details

### Setting up the Virtual Environment

1. Make sure you're in the project directory
2. Create a new virtual environment with Poetry:
   ```bash
   poetry env use python3.12  # or your preferred Python version
   ```
3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

### Run the application

1. Make sure your Postgres database is running
2. Install the dependencies using the command `poetry install`
3. Run the application using the command `poetry run uvicorn app.main:app --reload`

