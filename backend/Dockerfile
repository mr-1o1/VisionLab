# Match your local version
FROM python:3.10-slim

WORKDIR /code

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
