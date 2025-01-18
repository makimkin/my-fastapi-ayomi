# AYOMI

The project proposes a solution for the following use-case:

Context
A company currently provides a valuation tool to their clients and aim to enhance it by integrating an advanced calculator to assist them in their calculations.

Goal
This project involves the design, implementation, and deployment of the calculator system, leveraging Python for backend development and Docker for deployment.

Objectives
- [x] Develop a Reverse Polish Notation (RPN) calculator algorithm in Python.
- [x] Create a REST API with FastAPI to handle calculation requests and return results.
- [x] Store all calculation operations and results in a database for auditability and reporting.
- [x] Provide an API route to export calculations and results as a CSV file.
- [x] Deploy the complete system using Docker and Docker Compose for portability and scalability.



## Installation

For usage only:

```bash
rm -rf .venv
python3.13 -m venv .venv
source .venv/bin/activate
poetry install
```

For developers:

```bash
git init
rm -rf ./.git/hooks
git clone git@github.com:makimkin/hooks.git ./.git/hooks
pre-commit install
```

## Usage

### Running

#### Docker + MongoDB

Build and run [in detached mode] the application using Docker:

```bash
[export APP_DB=mongo]
just up [-d]
```

#### Docker + PostgreSQL

Build and run [in detached mode] the application using Docker:

```bash
export APP_DB=postgres
just up [-d]
just app-migration-up
```

### Shut down

Shutting down the application [and remove its volumes]:

```bash
just down [-v]
```

## Test

Run tests [with outputs] [and exit of the first test failure]

```bash
[export APP_DB=mongo]
just test [-s] [--sw]
```
