FROM ghcr.io/mlflow/mlflow:v2.13.1

WORKDIR /app

ENV GIT_PYTHON_REFRESH=quiet
ENV MLFLOW_EXPERIMENT_NAME=songs-classifier

RUN apt-get update && \
    apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5000
