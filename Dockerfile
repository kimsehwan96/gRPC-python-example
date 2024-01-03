FROM python:3.8-slim
WORKDIR server

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "greeter_server.py"]
