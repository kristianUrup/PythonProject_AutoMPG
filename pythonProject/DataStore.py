import os
import tarfile
from six.moves import urllib
import pandas as pd

DOWNLOAD_ROOT_HOUSING = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT_HOUSING + "datasets/housing/housing.tgz"

DOWNLOAD_ROOT_AUTOMOBILE = "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg.data"
AUTOMOBILE_PATH = os.path.join("datasets", "automobile")
AUTOMOBILE_URL = DOWNLOAD_ROOT_AUTOMOBILE + "datasets/automobile/automobiles.tgz"
AUTOMOBILE_FILEPATH = "datasets/automobile/auto-mpg.data"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def loading_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def fetch_automobile_data(automobile_url=HOUSING_URL, automobile_path=HOUSING_PATH):
    if not os.path.isdir(automobile_path):
        os.makedirs(automobile_path)
    tgz_path = os.path.join(automobile_path, "auto-mpg.data")
    urllib.request.urlretrieve(automobile_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=automobile_url)
    housing_tgz.close()

def loading_automobile_data(automobile_path=HOUSING_PATH):
    csv_path = os.path.join(automobile_path, "auto-mpg.data")
    return pd.read_csv(csv_path)