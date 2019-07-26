FROM python:2.7-slim

WORKDIR /app

COPY docker_demo.py /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "docker_demo.py"]
