FROM python:3.9.12-slim

RUN pip install fastapi uvicorn poetry wheel

EXPOSE 8000

WORKDIR /usr/src/projectname

ENV PORT 8000
ENV HOST "0.0.0.0"