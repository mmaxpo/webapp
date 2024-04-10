FROM ubuntu:20.04

MAINTAINER mehdi <xpo77@yahoo.com>
RUN mkdir /webapp
WORKDIR /webapp

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev libpq-dev postgresql-client netcat && \
    rm -rf /var/lib/apt/lists/*

ADD requirements.txt /webapp
RUN pip3 install -r requirements.txt

ADD . /webapp



