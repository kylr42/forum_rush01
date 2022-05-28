FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apk update && apk upgrade --available && sync \
    && apk add gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY app /usr/src/app

CMD ["python", "/usr/src/app/main.py"]
