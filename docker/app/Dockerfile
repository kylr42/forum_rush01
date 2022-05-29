FROM python:3.5

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apt update && apt upgrade -y \
    && apt install -y gcc g++ python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY app /usr/src

CMD ["manage.py", "runserver"]