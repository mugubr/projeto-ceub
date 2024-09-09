FROM python:3.12.5-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN apt-get update && apt-get install -y bash

COPY doceria-backend/pyproject.toml ./
COPY doceria-backend/poetry.lock ./

RUN pip install poetry
RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

COPY doceria-backend/ ./

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

CMD poetry run uvicorn --host 0.0.0.0 doceria_backend.app:app



