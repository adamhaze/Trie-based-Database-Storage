import numpy as np
from random import shuffle
import time
import csv
import os
from TrieTree import *

# number between 0 and 1
shuffle_seed = 0.5

class MetricCollector:
    
    def __init__(self, data_struct, filepath):
        
        self.DS = data_struct
        self.filepath = filepath
        
        # string name for saving results specific to given structure
        self.name = self.DS.name 
        
        self.interval = 1000
        
        # METRICS
        self.node_cnt = []
        self.insert_time = []
        self.query_time = []

        
    def load_data(self):
        with open(self.filepath, 'r') as file:
            self.data = file.read()
            self.data = self.data.split('\n')
        file.close()
        # shuffle(self.data, shuffle_seed)
        # print(len(self.data))
        
    def log_node_count(self):
        self.node_cnt.append(self.DS.nodeCount)
        
    def log_insert_time(self):
        self.insert_time.append(time.time() - self.time_tracker)
        self.time_tracker = time.time()
        
    def log_query_time(self):
        self.query_time.append(time.time() - self.time_tracker)
        self.time_tracker = time.time()

    def perform_inserts(self):
        self.time_tracker = time.time()
        for i,word in enumerate(self.data):
            self.DS.insert(word)
            if (i % self.interval == 0) & (i > 0):
                self.log_node_count()
                self.log_insert_time()
                
    def perform_queries(self):
        self.time_tracker = time.time()
        for i,word in enumerate(self.data):
            self.DS.query(word)
            if (i % self.interval == 0) & (i > 0):
                self.log_query_time()
                
    def save_results(self):
        def write_to_file(save_file, data):
            with open(save_file, 'w') as results:
                wr = csv.writer(results)
                for elem in data:
                    wr.writerow([elem])
            results.close()
                    
        if not os.path.exists('results'): os.makedirs('results')
                
        save_file_nodecnt = 'results/{}_node_count.csv'.format(self.name)
        save_file_instime = 'results/{}_insert_time.csv'.format(self.name)
        save_file_querytime = 'results/{}_query_time.csv'.format(self.name)

        write_to_file(save_file_nodecnt, self.node_cnt)
        write_to_file(save_file_instime, self.insert_time)
        write_to_file(save_file_querytime, self.query_time)
                
    def execute(self):
        self.load_data()
        self.perform_inserts()
        self.perform_queries()
        self.save_results()
        
        
        

# trie = TrieTree()
# mc = MetricCollector(trie, 'input_data.csv')
# mc.execute()

# print(mc.query_time)