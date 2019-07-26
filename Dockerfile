FROM python:2.7-slim

WORKDIR /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "docker_demo.py"]

COPY docker_demo.py /app
