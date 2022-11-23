import matplotlib.pyplot as plt
import numpy as np
import os

figsize = 16,8

def plot_num_nodes():
    basic = np.loadtxt('results/basic_trie_node_count.csv')
    # radix = np.loadtxt('results/radix_trie_node_count.csv')
    # fusion = np.loadtxt('results/fusion_trie_node_count.csv')
    
    x = [i for i in range(len(basic))]
    f,ax = plt.subplots(figsize=figsize)
    ax.plot(x, basic, label='basic trie', c='red')
    # ax.plot(x, radix, label='radix trie', c='blue')
    # ax.plot(x, fusion, label='fusion trie', c='green')
    ax.set_xlabel('# intervals')
    ax.set_ylabel('# nodes')
    ax.set_title('# of nodes created in data structure over intervals of insert operations')
    ax.legend()
    f.savefig(os.path.join('figures', 'node_count_comparison.png'), bbox_inches='tight')
    # plt.show()
    
    
def plot_insert_time():
    basic = np.loadtxt('results/basic_trie_insert_time.csv')
    # radix = np.loadtxt('results/radix_trie_insert_time.csv')
    # fusion = np.loadtxt('results/fusion_trie_insert_time.csv')
    
    x = [i for i in range(len(basic))]
    f,ax = plt.subplots(figsize=figsize)
    ax.plot(x, basic, label='basic trie', c='red')
    # ax.plot(x, radix, label='radix trie', c='blue')
    # ax.plot(x, fusion, label='fusion trie', c='green')
    ax.set_xlabel('# insert intervals')
    ax.set_ylabel('time elapsed over insert interval')
    ax.set_title('Time Complexity of Insert Operations')
    ax.legend()
    f.savefig(os.path.join('figures', 'insert_time_comparison.png'), bbox_inches='tight')
    # plt.show()
    
def plot_query_time():
    basic = np.loadtxt('results/basic_trie_query_time.csv')
    # radix = np.loadtxt('results/radix_trie_query_time.csv')
    # fusion = np.loadtxt('results/fusion_trie_query_time.csv')
    
    x = [i for i in range(len(basic))]
    f,ax = plt.subplots(figsize=figsize)
    ax.plot(x, basic, label='basic trie', c='red')
    # ax.plot(x, radix, label='radix trie', c='blue')
    # ax.plot(x, fusion, label='fusion trie', c='green')
    ax.set_xlabel('# query intervals')
    ax.set_ylabel('time elapsed over query interval')
    ax.set_title('Time Complexity of Query Operations')
    ax.legend()
    f.savefig(os.path.join('figures', 'query_time_comparison.png'), bbox_inches='tight')
    # plt.show()
    
    
def make_plots():
    if not os.path.exists('figures'): os.makedirs('figures')
    plot_num_nodes()
    plot_insert_time()
    plot_query_time()
    
make_plots()

    