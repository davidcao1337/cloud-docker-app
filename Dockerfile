FROM alpine:latest

RUN apk update
RUN apk add python3

WORKDIR /home

COPY functions.py ./
COPY main.py ./
RUN mkdir -p /data
RUN mkdir -p /output
COPY data ./data
COPY output ./output

CMD [ "python3", "./main.py" ]
