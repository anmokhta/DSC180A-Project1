#!/usr/bin/env python

import sys
import json

sys.path.insert(0, 'src')

from test_etl import create_rand_graphs, create_combined, create_combined_edges, plot_graph
#from model import train



def main(targets):
    '''
        Runs the main project pipeline logic, given the targets.
        targets must contain: 'data', 'model'.
        `main` runs the targets in order of data=>model.
    '''

    ##FULL ORDER OF TARGETS BY PRIORITY
    #clean (remove all data)
    #test (data -> model)
    #all (test-data model)

    #test-data
    #data
    #model
    
    
    if 'test' in targets:
        with open('config/test_etl.json') as fh:
            test_etl_config = json.load(fh)
        #check if pickles not exist in raw, if true run function below
        create_rand_graphs(**test_etl_config)
        #check if gt or combined_seperated not exist in temp
        create_combined(**test_etl_config)
        create_combined_edges(**test_etl_config)

        
        
if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)

