FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get upgrade -y

RUN apt-get install -y tzdata
ENV TZ="Europe/Moscow"

RUN apt-get install -y python3 python3-pip

RUN apt-get install -y libgl1-mesa-dev tk python3-tk
RUN apt-get install -y libsdl2-mixer-2.0-0

RUN mkdir /root/TicTacToe

WORKDIR /root/TicTacToe

COPY TicTacToe.spec Pipfile Pipfile.lock ./

RUN mkdir ./app

COPY app ./app/

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip3 install pipenv && \
    pipenv --python 3.6 && \
    pipenv run pip install pipenv && \
    pipenv run pipenv install --dev --skip-lock && \
    pipenv run pyinstaller TicTacToe.spec



