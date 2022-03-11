ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# 起動されるまでローカルのファイルは存在しないので、意図的にコピーしてあげる
RUN mkdir /app
COPY ./requirements.txt /app

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git vim ruby && \
    apt-get install build-essential && \
    pip install cmake==3.21.2 && \
    pip install -r requirements.txt
