FROM ubuntu:latest
LABEL authors="linux"

ENTRYPOINT ["top", "-b"]