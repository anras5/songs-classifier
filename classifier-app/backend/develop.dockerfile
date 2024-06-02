FROM ghcr.io/mlflow/mlflow:v2.13.1

WORKDIR /app

ENV GIT_PYTHON_REFRESH=quiet
ENV MLFLOW_EXPERIMENT_NAME=songs-classifier

RUN apt-get update && \
    apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://pyenv.run | /bin/bash && \
    python -m pip install virtualenv

ENV PATH="/root/.pyenv/bin:$PATH"

EXPOSE 5000

CMD ["tail", "-f", "/dev/null"]