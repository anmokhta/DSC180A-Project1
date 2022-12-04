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
    connect = sqlite3.connect('data/raw/database.sqlite')
    query = """
    SELECT pa.paper_id, pa.author_id, a.name AS author_name
    FROM paper_authors AS pa JOIN papers AS p ON pa.paper_id = p.id
    JOIN authors as a ON pa.author_id = a.id
    WHERE p.Year BETWEEN '2015' AND '2018'
    ORDER BY paper_id
    """
    df_nips = pd.read_sql(query, connect)
    df_nips.to_csv('data/temp/df_nips.csv')





# def read_edge(gph, n0, n1): #add switch between plus and multiply
# if gph.has_edge(n0, n1):
#     gph[n0][n1]['weight'] +=1 #*= 2
#     return gph[n0][n1]['weight']
# else:
#     gph.add_edge(n0, n1, weight=1)
#     return 1

# #https://www.kaggle.com/code/kevinvdsk/community-detection


# connect = sqlite3.connect('../data/NIPS/database.sqlite')
# query = """
# SELECT pa.paper_id, pa.author_id, a.name AS author_name
# FROM paper_authors AS pa JOIN papers AS p ON pa.paper_id = p.id
# JOIN authors as a ON pa.author_id = a.id
# WHERE p.Year BETWEEN '2015' AND '2018'
# ORDER BY paper_id
# """
# df_nips = pd.read_sql(query, connect)

# # Have a look at data
# df_nips.head(10)

# G = nx.Graph()

# for p, a in df_nips.groupby('paper_id')['author_name']: 
#     # TESTING print(a)
#     for a1, a2 in itertools.combinations(a, 2):
#         # creates an edge
#         read_edge(G, a1, a2)
        
# #SAVE THIS GRAPH AS A PICKLE GRAPH IN TEMP