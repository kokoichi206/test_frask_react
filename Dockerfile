FROM python:3.8-slim-buster as runner

WORKDIR /root/opt

RUN python -m pip install numpy && \
    python -m pip install pandas && \
    python -m pip install matplotlib
RUN python -m pip install flask && \
    python -m pip install flask_restful && \
    python -m pip install flask flask_cors
RUN apt-get update
RUN apt-get install -y git vim ruby

EXPOSE 8000
