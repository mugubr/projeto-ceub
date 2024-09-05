FROM python:3.12.5-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/

COPY doceria-backend/pyproject.toml .

COPY doceria-backend/poetry.lock .

COPY doceria-backend/entrypoint.sh /app/entrypoint.sh

COPY doceria-backend/ ./

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 fast_zero.app:app