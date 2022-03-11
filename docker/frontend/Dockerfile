ARG VARIANT="16-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:0-${VARIANT}

WORKDIR /app/
COPY ./ /app

RUN sudo apt update
RUN sudo npm install -g create-react-app
