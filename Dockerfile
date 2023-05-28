FROM ubuntu:latest
LABEL authors="naren"

FROM python
WORKDIR /app
COPY . .
CMD [ "python", "game.py", "2" ]