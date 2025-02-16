FROM python:3.12-bookworm
#FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip "poetry==1.8.4"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main --no-root

COPY fastapi-app /var/app

RUN chmod +x /var/app/prestart.sh

EXPOSE 8000

ENTRYPOINT ["/var/app/prestart.sh"]

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["gunicorn", "main:app", "--workers=4", "--worker-class=uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
