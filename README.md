# Songs Classifier

**Songs Classifier** is a project that consists of two parts.
- In `Data analysis` you can find Jupyter notebook with data analysis of the dataset and a lot of insights into how the data looks like and how the machine learning models were trained.
- In `Classifier App` you can find an app that uses `Streamlit`, `mlflow` and `spotipy` to allow users to classify songs from Spotify with trained Gradient Boosting Tree. Everything is running in containers.

# How to run?
## Data analysis

```shell
cd data-analysis
docker compose up
```

The jupyter lab is available at `localhost:8888`.

## Classifier App

Create a `.env` file inside the `classifier-app/frontend` directory with the same structure as `.env.example`. Get your own
Spotify credentials from [Spotify Developers Website](https://developer.spotify.com/dashboard).

```shell
cd classifier-app
docker compose up
```

Frontend app is available at `localhost:8080` and backend app (model) is available at `localhost:5000`.

### Develop backend (if you want to change the model)

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

# How does the app look like?

![image](https://github.com/anras5/songs-classifier/assets/91278796/a227135e-1172-49f3-85dd-d59ac0a19a32)

