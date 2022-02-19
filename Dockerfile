FROM python:3.8-bullseye

WORKDIR /

COPY . .

CMD ["python", "main.py"]