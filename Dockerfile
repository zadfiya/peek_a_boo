FROM ubuntu:latest
LABEL authors="naren"

FROM python
COPY . .
CMD [ "python", "game.py", "2" ]