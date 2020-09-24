FROM python:3.8-slim

WORKDIR /code

COPY src/ .

CMD [ "python3", "./script1.py" ]
