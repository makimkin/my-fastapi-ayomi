# AYOMI

## Overview

### Context
The company currently provides a valuation tool to its clients and aims to enhance it by integrating an advanced calculator to assist with complex calculations.

### Description
This project involves the design, implementation, and deployment of a calculator system, utilizing Python for backend development, Docker for deployment, and React.js for the front end.

### Technical Objectives
- [x] Develop a Reverse Polish Notation (RPN) calculator algorithm in Python.
- [x] Create a REST API using FastAPI to process calculation requests and return results.
- [x] Store all calculation operations and results in a database for auditability and reporting purposes.
- [x] Provide an API endpoint to export calculations and results as a CSV file.
- [x] Deploy the complete system using Docker and Docker Compose for portability and scalability.

## Installation

### For Usage Only

Set up the environment and install dependencies:

```bash
rm -rf .venv
python3.13 -m venv .venv
source .venv/bin/activate
poetry install
```

### For Developers

1. Install [justfile](https://github.com/casey/just)

2. Install environment

```bash
rm -rf .venv
python3.13 -m venv .venv
source .venv/bin/activate
poetry install
```

3. Initialize the repository and set up pre-commit hooks:

```bash
git init
rm -rf ./.git/hooks
git clone git@github.com:makimkin/hooks.git ./.git/hooks
pre-commit install
```

# STARTING

#### Environment

```bash
cp .env.sample .env
```

#### Docker & MongoDB

Build and run the application in detached mode using Docker:

```bash
export APP_DB=mongo && just up [-d]
```

#### Docker & PostgreSQL

Build and run the application [in detached mode] using Docker, and perform database migrations:

```bash
export APP_DB=postgres && just up [-d]
just app-migration-up
```

# TESTING

Run the tests [with optional output] and [exit on the first failure]:

```bash
just test [-s] [--sw]
```

# SHUTTING DOWN

To shut down the application [and optionally remove its volumes]:

```bash
just down [-v]
```

# USAGE

## Documentation
Once the application is running, you can access:
- **[Swagger UI](http://localhost:8000/docs)**
- **[Redoc](http://localhost:8000/redoc)**

## Examples

### Compute

To calculate an operation like `(4 - 5) / 3 * 2 + 1` written in RPN notation as `1 2 3 4 5 + * / -`, use the following command:

```bash
curl -X 'POST' 'http://localhost:8000/v1/calculator/compute'
-H 'accept: application/json'
-H 'Content-Type: application/json'
-d '{
  "expression": "1 2 3 4 5 + * / -"
}'
```

### Read Many

To retrieve previous inputs in JSON format:

```bash
curl -X 'GET' 'http://localhost:8000/v1/calculator/'
-H 'accept: application/json'
```

### Generate CSV

To generate a CSV containing all previous inputs:

```bash
curl -X 'GET' 'http://localhost:8000/v1/calculator/csv'
-H 'accept: application/json'
```

# STRUCTURE

```
my-fastapi-ayomi/
├── .github/
│   └── workflows/
│       └── <GitHub Actions workflows>
├── src/
│   ├── application
│   │   └── <application layer of the project>
│   ├── domain/
│   │   └── <domain layer of the project>
│   ├── interface/
│   │   └── <interface layer>
│   ├── infrastructure/
│   │   └── <infrastructure layer>
│   ├── settings/
│   │   └── <global configuration of the project>
│   ├── tests/
│   │   └── <all test cases>
│   └── lib/
│       └── <utility functions>
├── .env.sample                 # Sample environment configuration file
├── .gitignore                  # Files and folders ignored by Git
├── .pre-commit-config.yaml     # Pre-commit hook configuration
├── Dockerfile                  # Docker image for the application
├── PLAN.md                     # Detailed project plan
├── README.md                   # Project documentation
├── docker-compose.app.yaml     # Docker Compose configuration for the application
├── docker-compose.mongo.yaml   # Docker Compose configuration for MongoDB
├── docker-compose.postgres.yaml# Docker Compose configuration for PostgreSQL
├── justfile                    # Task automation script
├── poetry.lock                 # Poetry dependency lock file
└── pyproject.toml              # Python project configuration and dependencies
```
