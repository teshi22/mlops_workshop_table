import argparse
import pickle
from typing import TypedDict

import mlflow
import numpy as np
import pandas as pd
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from catboost import CatBoostRegressor, Pool
from sklearn.metrics import mean_squared_error


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_train_data",
        type=str,
        help="input data",
        default="../data/W207_train_FE.csv",
    )
    parser.add_argument(
        "--input_valid_data",
        type=str,
        help="input data",
        default="../data/W207_dev_FE.csv",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["local", "remote"],
        help="execution mode",
        default="local",
    )

    args = parser.parse_args()

    return args

if __name__ == "__main__":

    args = parse_args()

    if args.mode == "local":
        print("mode local")
        subscription_id = "5290deef-ab3d-4e26-90bb-2296ecd99c71"
        resource_group = "ml-handson"
        workspace = "ml-workspace"

        ml_client = MLClient(
            DefaultAzureCredential(),
            subscription_id,
            resource_group,
            workspace,
        )
        azureml_mlflow_uri = ml_client.workspaces.get(
            ml_client.workspace_name
        ).mlflow_tracking_uri
        mlflow.set_tracking_uri(azureml_mlflow_uri)

        experiment_name = "sale_price_regression_notebook"
        mlflow.set_experiment(experiment_name)

    run = mlflow.start_run()
    # 記述
    mlflow.end_run()
