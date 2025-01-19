# AYOMI

## Overview

### Context
A company currently provides a valuation tool to their clients and aims to enhance it by integrating an advanced calculator to assist them in their calculations.

### Goal
This project involves the design, implementation, and deployment of a calculator system, leveraging Python for backend development and Docker for deployment.

### Objectives
- [x] Develop a Reverse Polish Notation (RPN) calculator algorithm in Python.
- [x] Create a REST API with FastAPI to handle calculation requests and return results.
- [x] Store all calculation operations and results in a database for auditability and reporting.
- [x] Provide an API route to export calculations and results as a CSV file.
- [x] Deploy the complete system using Docker and Docker Compose for portability and scalability.

---

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

Initialize the repository and set up pre-commit hooks:

```bash
git init
rm -rf ./.git/hooks
git clone git@github.com:makimkin/hooks.git ./.git/hooks
pre-commit install
```

---

## Usage

#### Running | Docker & MongoDB

Build and run the application in detached mode using Docker:

```bash
APP_DB=mongo && just up [-d]
```

#### Running | Docker & PostgreSQL

Build and run the application [in detached mode] using Docker, and perform database migrations:

```bash
APP_DB=postgres && just up [-d]
just app-migration-up
```

---

### Shutting Down the Application

To shut down the application [and optionally remove its volumes]:

```bash
just down [-v]
```

---

## Testing

Run the tests [with optional output] and [exit on the first failure]:

```bash
export APP_DB=mongo
just test [-s] [--sw]
```
