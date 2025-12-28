FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir streamlit requests

COPY ./app /app

EXPOSE 8501

CMD ["streamlit", "run", "app/main.py", "--server.address=0.0.0.0"]
