#!/usr/bin/env python

import gzip
import time
import sys
import urllib2
import urllib
import re

# this is the method that will transform your query before either indexing it or querying it - in this case does nothing with the query
def analyze_query(query):
    return(query)

# this is the method that will transform your url before either indexing it or testing it - in this case does nothing with the url
def analyze_url(url):
    return(url)

# this is the method that will query the phrase "q" from the index and return a dictionary of the results ("url": score)
def query_index(q, search_index):
    if search_index.has_key(q):
        return search_index[q]
    return dict()

# this is the method that will index the phrase "q" linked to the url "u" with a score of "n" in the search index "search_index"
def index_line(q, u, n, search_index):
    search_index[q][u]=search_index.setdefault(q,dict()).setdefault(u,0)+n
    return

# DO NOT MODIFY ANYTHING BELOW THIS




















# HARNESS PART - DO NOT MODIFY THIS

def create_index(file_name, search_index):
    f = gzip.open(file_name, 'r')
    while True:
        line = f.readline()
        if line == "":
            break
        items = line.split("\t")
        index_line(items[0], items[1], int(items[2]), search_index)

def answer_queries(search_index):
    print "Type queries ([Enter] to quit)"
    while True:
        q = sys.stdin.readline().strip()
        start = time.time()
        if q == "":
            break;
        results = query_index(q, search_index)
        if (len(results) == 0):
            print "no results"
            continue
        for r in sorted(results, key=results.get, reverse=True):
            print str(results[r])+"\t"+r
        print "done in ", (time.time() - start) * 1000, " ms"
    print "bye."



if __name__ == "__main__":
    print "Indexing..."
    search_index = dict()
    file_name = sys.argv[1]
    start = time.time()
    create_index(file_name, search_index)
    print "Indexing done in ", int(time.time() - start), " seconds"

    answer_queries(search_index)


    
