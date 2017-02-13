FROM python:alpine
MAINTAINER David Gasquez <davidgasquez@gmail.com>

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

# Add the application
COPY server /app
WORKDIR /app

CMD ["python", "app.py"]
