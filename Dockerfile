FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip3 install numpy

WORKDIR /methodo

COPY . .

CMD [ "python3", "main.py" ]