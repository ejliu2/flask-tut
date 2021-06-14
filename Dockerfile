# https://towardsdatascience.com/a-journey-into-big-data-with-apache-spark-part-1-5dfcc2bccdd2
FROM python:3.9-buster

RUN apt-get update -y
RUN apt-get install bash -y
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

EXPOSE 8088
# docker run --env-file ./env.list --rm -it -p 8088:8088 ejl2/spark:latest /bin/bash  <- ignore, look in docker-compose.yml instead