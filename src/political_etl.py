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
import pickle
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

def fix_political_gml(link_dir, temp_dir, data_dir, raw_data_filename, temp_pickle_graph_filename, ground_truth_filename):
    # opening raw data network (gml file) and adding fix for netx
    # read file
    f = open(data_dir + raw_data_filename, "r")
    contents = f.readlines()
    f.close()
    # adding missing line to contents
    missing_line = '  multigraph 1\n'
    contents.insert(3, missing_line)
    # write to file
    f = open(data_dir + raw_data_filename, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

def prepare_political(link_dir, temp_dir, data_dir, raw_data_filename, temp_pickle_graph_filename, ground_truth_filename):
    print("make pickle graph and ground truth json")
    G = nx.read_gml("polblogs.gml")

    # TO-DO: Write ground truth json for temp folder

    pickle.dump(cliq_graph, open(temp_dir + temp_pickle_graph_filename, 'wb'))
    print(temp_dir + temp_pickle_graph_filename + ' saved!' )