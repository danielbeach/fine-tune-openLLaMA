FROM ubuntu:20.04

ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget vim software-properties-common python3.9 python3-pip curl unzip libpq-dev build-essential libssl-dev libffi-dev pypy-dev python3.9-dev && \
    apt-get clean

WORKDIR app
COPY . /app

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2
RUN update-alternatives --config python3
RUN pip3 install --upgrade pip
RUN python3 -m pip install bs4
RUN python3 -m pip install -r requirements.txt