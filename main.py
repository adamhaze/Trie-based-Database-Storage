from MetricCollector import *
from TrieTree import *
from radix_tries import *
from plotting import *


def main():
    # input_data = 'input_data.csv'
    input_data = 'ip_list.csv'
    
    trie = TrieTree()
    mc_trie = MetricCollector(trie, input_data)
    mc_trie.execute()
    
    radix_trie = RadixTrie()
    mc_radix = MetricCollector(radix_trie, input_data)
    mc_radix.execute()

    make_plots()
    
    
if __name__=="__main__":
    main()
    