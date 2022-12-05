#!/usr/bin/env python

# fix politcal file - add in multigraph line 
# finish political etl
# spectral file
    # - test
    # - political
    # - nips
# done w/ code

import sys
import json

sys.path.insert(0, 'src')

from clean import clean
from test_etl import create_rand_graphs, create_combined, create_combined_edges, plot_graph
from nips_etl import pull_kaggle_data, read_raw_sql
from political_etl import pull_political_data, prepare_political
# from spectral import



def main(targets):
    '''
        Runs the main project pipeline logic, given the targets.
        targets must contain: 'data', 'model'.
        `main` runs the targets in order of data=>model.
    '''

    ##FULL ORDER OF TARGETS BY PRIORITY
    #clean (remove all data)
    #test (test-data model)
    #all (data -> model)

    #test-data
    #data
    #model
    model_test = None
    
    if 'clean' in targets:
        clean()
    
    if 'test' in targets:
        targets.extend(["test-data", "model"])
        model_test = True
        print("extended test-data & model!")

    if 'all' in targets:
        targets.extend(["data", "model"])
        model_test = False
        print("extended data & model!")
    
    if 'test-data' in targets:
        with open('config/test_etl.json') as fh:
            test_etl_config = json.load(fh)
        #check if pickles not exist in raw, if true run function below (ADD INTO ETL PY FILE)
        create_rand_graphs(**test_etl_config)
        #check if gt or combined_seperated not exist in temp
        create_combined(**test_etl_config)
        create_combined_edges(**test_etl_config)

    if 'nips' in targets:
        print("This will make data prepped for the model! use src/nips_etl.py for making functions")
        with open('config/nips_etl.json') as fh:
            nips_etl_config = json.load(fh)
        pull_kaggle_data(**nips_etl_config)
        read_raw_sql(**nips_etl_config)


    if ('data' in targets) or ('political' in targets):
        print("This will make data prepped for the model! use src/political_etl.py for making functions")
        with open('config/political_etl.json') as fh:
            political_etl_config = json.load(fh)
        pull_political_data(**political_etl_config)
        prepare_political(**political_etl_config)
        
        
    if 'model' in targets:
        print("This will check which dataset to load (if REAL data exists, that. otherwise check if test data exists, uest that) and run model")
        if model_test:
            print("using test data to make model!")
        else:
            print("using real data to make model!")
        # Maybe do above with data checker function idk
        
if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)

