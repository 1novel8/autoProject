FROM python:3.10.5


EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /autoProject/src

COPY ./requirements.txt /autoProject/requirements.txt

RUN pip install -r /autoProject/requirements.txt

COPY . /autoProject/src

