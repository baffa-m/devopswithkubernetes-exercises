FROM python:3-alpine 

WORKDIR /app

RUN pip install apscheduler

COPY . /app

CMD [ "python", "-u", "main.py" ]