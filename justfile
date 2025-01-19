dc := "docker compose"

file_app := "--file docker-compose.app.yaml"
file_db := "--file docker-compose." + "${APP_DB:-mongo}" + ".yaml"

container_db_ui := "db-ui"
container_app := "app"
container_db := "db"

command := dc + " " + file_app + " " + file_db

default:
  just --list

build +args="":
  {{command}} build {{args}}

up +args="":
  {{command}} up --build --remove-orphans {{args}}

down +args="":
  {{command}} down {{args}}

test +args="":
  clear && python -m pytest {{args}}

ruff +args="":
  ruff check ./src --fix

restart +args="":
  {{command}} restart {{args}}

app-restart +args="":
  {{command}} restart {{container_app}} {{args}}

app-logs +args="":
  {{command}} logs {{container_app}} {{args}}

app-migration-gen:
  {{command}} exec {{container_app}} alembic revision --autogenerate

app-migration-up:
  {{command}} exec {{container_app}} alembic upgrade head

app-migration-base:
  {{command}} exec {{container_app}} alembic downgrade base

db-ui-logs +args="":
  {{command}} logs {{container_db_ui}} {{args}}

sql-connect:
  {{command}} exec {{container_db}} psql -U dev_user kot-db

ci-build:
  {{command}} build

ci-test:
  {{command}} run --rm {{container_app}} sh -c "python -m pytest -s --sw -vvv"
