FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get upgrade -y

RUN apt-get install -y tzdata
ENV TZ="Europe/Moscow"

RUN apt-get install -y python3 python3-pip

RUN apt-get install -y libgl1-mesa-dev tk python3-tk
RUN apt-get install -y libsdl2-mixer-2.0-0

RUN mkdir /root/TicTacToe

WORKDIR /root/TicTacToe

COPY Pipfile Pipfile.lock TicTacToe.spec ./

RUN mkdir ./app

COPY app ./app/

RUN pip3 install pipenv && \
    pipenv install --dev --system --deploy && \
    pyinstaller TicTacToe.spec



