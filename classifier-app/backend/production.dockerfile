FROM ghcr.io/mlflow/mlflow:v2.13.1

WORKDIR /app

ENV GIT_PYTHON_REFRESH=quiet
ENV MLFLOW_EXPERIMENT_NAME=songs-classifier

COPY models models

EXPOSE 5000

CMD ["sh", "-c", "mlflow models serve -m /app/models/GradBoostClassifier --no-conda -p 5000 -h 0.0.0.0"]