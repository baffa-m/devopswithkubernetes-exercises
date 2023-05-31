FROM python:3-alpine 

WORKDIR /app

RUN pip install pydantic uvicorn fastapi
RUN pip install pydantic[dotenv]

COPY . /app

ENV port=5001

CMD ["python3",  "main.py"]