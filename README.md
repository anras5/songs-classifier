# Songs Classifier

## Data analysis

```shell
cd data-analysis
docker compose up
```

The jupyter lab is available at `localhost:8888`.

## Classifier App

```shell
cd classifier-app
docker compose up
```

Frontend app is available at `localhost:8080` and backend app (model) is available at `localhost:5000`.

### Develop backend

```shell
cd classifier-app/backend
docker build -f develop.dockerfile -t mlflow-develop-image .
docker run -it -v "${PWD}:/app" -p 5000:5000 --rm mlflow-develop-image /bin/bash
```

Change the `${PWD}` to `$(pwd)` if you are on Linux. If you have already built the image in the past skip the second
command.

**Run the training**

```shell
python3 src/train.py --file_path=/app/data/dataset_cleaned.csv
```

Script prints out `runid` at the end.

**Serve the model**

```shell
mlflow models serve --model-uri runs:/<runid>/GradBoostClassifier --no-conda -p 5000 -h 0.0.0.0
```
