import argparse

import mlflow
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

COLUMNS = ['popularity', 'duration_ms', 'explicit', 'danceability', 'energy', 'loudness',
           'mode', 'speechiness', 'acousticness', 'instrumentalness', 'valence', 'tempo', 'track_genre']


def load_data(file_path):
    df = pd.read_csv(file_path, sep=',', usecols=COLUMNS)
    df['mode'] = df['mode'].astype('bool')
    X, y = df.drop('track_genre', axis=1), df['track_genre']
    return X, y


def train_model(X_train, y_train):
    gbc = GradientBoostingClassifier(
        learning_rate=0.5,
        max_depth=8,
        max_features=0.8,
        min_samples_leaf=20,
        min_samples_split=12,
        n_estimators=100,
        subsample=1.0
    )
    gbc.fit(X_train, y_train)
    return gbc


def main(file_path):
    X, y = load_data(file_path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=60)

    with mlflow.start_run():
        model = train_model(X_train, y_train)
        mlflow.sklearn.log_model(model, "GradBoostClassifier")
        print(f"Model saved in run {mlflow.active_run().info.run_uuid}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Train a Gradient Boosting Classifier.")
    parser.add_argument('--file_path', type=str, required=True, help='Path to the CSV data file.')
    args = parser.parse_args()
    main(args.file_path)
