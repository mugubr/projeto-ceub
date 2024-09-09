#!/bin/bash
set -e

echo "Migrando banco de dados"
poetry run alembic upgrade head

echo "Iniciando aplicação"
exec poetry run uvicorn --host 0.0.0.0 --port 8000 doceria_backend.app:app
