FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY src src

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "src/main.py", "--server.port=8080", "--server.address=0.0.0.0"]
