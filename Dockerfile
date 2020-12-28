FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y git python3-pip python3-dev

WORKDIR /
COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt
COPY . /
CMD ["python3", "src/main.py"]
