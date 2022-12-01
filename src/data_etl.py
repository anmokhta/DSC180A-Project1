import sqlite3
import os
import os.path
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab

import itertools


#!pip install kaggle

# TO-DO: get json file read in and remove key
os.environ['KAGGLE_USERNAME']="andrewmokhta"
os.environ['KAGGLE_KEY']="eb7de261bcf48ef0ca684c07e28bb309"

from kaggle.api.kaggle_api_extended import KaggleApi


#TO-DO: check if SQLITE FILE EXISTS
def pull_raw_data():
    if os.path.exists("data/raw/database.sqlite"):
        print("Raw data already downloaded from Kaggle! Moving on to next step")
    else:
        kapi = KaggleApi()
        kapi.authenticate()

        print(kapi.dataset_list_files('benhamner/nips-papers').files)
        kapi.dataset_download_files('benhamner/nips-papers', path='data/raw/', quiet=False, unzip=True)


def read_raw_sql():
    print("sql")