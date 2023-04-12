# Dockerfile

FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN chmod +x app/prestart.sh
