# Prepare


## create environment

```
make env-create
```

```make env-create``` command is alias of command below defined in Makefile.

```
conda env create --prefix ./.env --file environment.yml
```

If you place this repository on WSL2 /mnt/* or AzureML Compute Instance working directory, we recommend to change ```--prefix ./.env``` to ```--prefix ~/azureml-mlops-env``` because of storage latency.

Affected:
- .vscode/setting.json ```python.defaultInterpreterPath```
- Makefile

## update environment

1. Add new package name and version to environment.yml.
1. ```make env-update```

```make env-update``` command is alias of command below defined in Makefile.

```conda env update --prefix ./.env --file environment.yml```


## pre-commit

```
pre-commit install
```

# Step by Step

## Step 0 : Run on AML

Execute base Jupyter notebook on Azure Machine Learning.

## Step 1 : Use MLflow

Add MLflow experiment management.

## Step 2 : Convert ipynb to py

Convert base Jupyter notebook to Python script.

```
jupyter nbconvert --to script "01_mlflow/Hands_on_NoteBook_model_build.ipynb"
mv 01_mlflow/Hands_on_NoteBook_model_build.py 02_python_script/build_model.py
```

Refactor and fix generated python script file, and run.

```
cd 02_python_script
python build_model.py
```

(Recommend) For Step 3, add `input_train_data` and `input_valid_data` properties that mean csv file path.

## Step 3 : Create AML Job

Define dependency-assets and execute Python script on Azure Machine Learning as a Job.

```bash
az ml data create -f ./03_job/data-train.yml
az ml data create -f ./03_job/data-valid.yml
az ml job create -f ./03_job/job-train.yml
```

## Step 4 : Create AML Pipeline

Define pipeline and reproduce training job.

```bash
az ml job create -f 04_pipeline/pipeline.yml 
```

## Step 5 : Deploy model as API

```bash
az ml online-endpoint create -f online-endpoint.yml 
az ml online-deployment create -n version-01 --endpoint w207-endpoint -f ./05_deploy/online-deployment.yml
```