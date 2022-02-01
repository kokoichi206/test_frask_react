# intel
# FROM python:3.8-slim-buster as runner
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git vim ruby && \
    apt-get install build-essential

# 下は pip install -r requirements.txt と同じ内容
RUN pip install aniso8601==9.0.1 && \
    pip install click==8.0.1 && \
    pip install cmake==3.21.2 && \
    pip install cycler==0.10.0 && \
    pip install dlib==19.22.1 && \
    pip install face-recognition==1.3.0 && \
    pip install face-recognition-models==0.3.0 && \
    pip install Flask==2.0.1 && \
    pip install Flask-Cors==3.0.10 && \
    pip install Flask-RESTful==0.3.9 && \
    pip install greenlet==1.1.1 && \
    pip install gunicorn==20.1.0 && \
    pip install itsdangerous==2.0.1 && \
    pip install Jinja2==3.0.1 && \
    pip install kiwisolver==1.3.2 && \
    pip install MarkupSafe==2.0.1 && \
    pip install matplotlib==3.4.3 && \
    pip install numpy==1.21.2 && \
    pip install pandas==1.3.3 && \
    pip install Pillow==8.3.2 && \
    pip install pyparsing==2.4.7 && \
    pip install python-dateutil==2.8.2 && \
    pip install pytz==2021.1 && \
    pip install six==1.16.0 && \
    pip install SQLAlchemy==1.4.23 && \
    pip install Werkzeug==2.0.1
