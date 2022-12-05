# POLITICAL DATA EXTRACT LOAD TRANSFER
# Pulls and prepares political data for community detection
# ---------------------------------------------------------
# link_dir = link where data will be pulled from (http://www-personal.umich.edu/~mejn/netdata/polblogs.zip)
# temp_dir = location where data prepared for community detection will reside (data/political/temp/)
# data_dir = location where raw data downloaded will reside (data/political/raw/)

import networkx as nx
import numpy as np
import requests
import zipfile
from io import BytesIO

def pull_political_data(link_dir, temp_dir, data_dir, raw_data_filename, temp_pickle_graph_filename, ground_truth_filename):
    filename = link_dir.split('/')[-1]

    print('Beginning Political Data Download')
    req = requests.get(link_dir)
    print('Political Data Download Completed')

    # extracting the zip file contents
    zf= zipfile.ZipFile(BytesIO(req.content))
    zf.extractall(data_dir)
    print('Data Extracted in ' + data_dir)

def prepare_political(link_dir, temp_dir, data_dir, raw_data_filename, temp_pickle_graph_filename, ground_truth_filename):
    print("make pickle graph and ground truth json")
