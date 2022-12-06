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
import os
from io import BytesIO

def pull_political_data(link_dir, temp_dir, data_dir, raw_data_filename, temp_pickle_graph_filename, ground_truth_filename):
    if os.path.exists(data_dir + raw_data_filename):
        print("Raw data already downloaded from internet! Moving on to next step")
    else:
        print('Beginning Political Data Download')
        req = requests.get(link_dir)
        print('Political Data Download Completed')

        # extracting the zip file contents
        zf= zipfile.ZipFile(BytesIO(req.content))
        zf.extractall(data_dir)
        print('Data Extracted in ' + data_dir)
        fix_political_gml(data_dir, raw_data_filename)

def fix_political_gml(data_dir, raw_data_filename):
    # TODO Make into a helper function, do not run if political gml already exists
    # opening raw data network (gml file) and adding fix for netx
    # read file
    with open(data_dir + raw_data_filename, "r") as fh:
        contents = fh.readlines()
    # adding missing line to contents
    missing_line = '  multigraph 1\n'
    contents.insert(3, missing_line)
    # write to file
    with open(data_dir + raw_data_filename, "w") as fh:
        contents = "".join(contents)
        fh.write(contents)
    print("multigraph contents fixed!")

def prepare_political(link_dir, temp_dir, data_dir, raw_data_filename, temp_pickle_graph_filename, ground_truth_filename):
    if os.path.exists(temp_dir + temp_pickle_graph_filename):
        print("Pickle data already prepared for analysis! Moving on to next step")
    else:
        G = nx.read_gml(data_dir + raw_data_filename, label='id')

        # TODO: Write ground truth json for temp folder

        pickle.dump(G, open(temp_dir + temp_pickle_graph_filename, 'wb'))
        print(temp_dir + temp_pickle_graph_filename + ' saved!' )


        ground_truths = {
            0: [] # democrat
            1: []  # republican
        }

        for i in H.nodes:
            ground_truths[H.nodes[i]['value']].append(i)

        with open(temp_dir + 'ground_truth.json', "w") as outfile:
            json.dump(ground_truths, outfile)
        print(temp_dir + 'ground_truth.json saved!' )









