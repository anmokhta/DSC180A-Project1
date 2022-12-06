#!/usr/bin/env python

# fix politcal file - add in multigraph line 
# finish political etl
# spectral file
    # - test
    # - political
    # - nips
# done w/ code

# TODO: REMOVE NOTEBOOK FOLDER AT END

import sys
import json
import networkx as nx

sys.path.insert(0, 'src')

from clean import clean
from test_etl import create_rand_graphs, create_combined, create_combined_edges
from nips_etl import pull_kaggle_data, read_raw_sql
from political_etl import pull_political_data, fix_political_gml, prepare_political
from spectral_analysis import graph_stats, return_sub_graphs, spectral_cluster, prediction_evaluation, spectral_evaluation



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
        create_rand_graphs(**test_etl_config)
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
        
        
    if 'spectral' in targets:
        print("This will check which dataset to load (if REAL data exists, that. otherwise check if test data exists, uest that) and run model")
        if model_test:
            # plitical/temp
            print("using test data to make model!")
            G = nx.read_gpickle('data/test/temp/combined.pickle')
            g0, g1 = return_sub_graphs(G)[0], return_sub_graphs(G)[1]
            g_dict = {'main_graph':G, 'subgraph1':g0, 'subgraph2':g1}
            for i in ['main_graph', 'subgraph1', 'subgraph2']:
                graph_stats(g_dict[i])
                print('graph_stats finished')
                spectral_evaluation(g_dict[i])
        else:
            # test/temp
            print("using real data to make model!")
            G = nx.read_gpickle('data/political/temp/political_graph.pickle')
            g0, g1 = return_sub_graphs(G)[0], return_sub_graphs(G)[1]
            g_dict = {'main_graph':G, 'subgraph1':g0, 'subgraph2':g1}
            for i in ['main_graph', 'subgraph1', 'subgraph2']:
                graph_stats(g_dict[i])
                print('graph_stats finished')
                spectral_evaluation(g_dict[i])
        # Maybe do above with data checker function idk
        
if __name__ == '__main__':
    # run via:
    # python main.py data spectral
    targets = sys.argv[1:]
    main(targets)

