# -*- coding: utf-8 -*-
# try something like

# -*- coding: utf-8 -*-
# try something like

from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest,nsmallest
from collections import defaultdict,Counter
import sys,os,unicodedata
from itertools import izip


def test():
        read_db_data = db(db.polarion).select()

#         sentence = excel_read('workitems.xlsx',1)

        ranking = defaultdict(int)
        n = len(read_db_data)
        print n
        
        #creating a string reading the excel list data to single string
        sentence1 = ""
        sentence = " "
        new_sentence = ""
        
        # reading the data from db and combining the title and description field
        for x in read_db_data:
#             print x.Title + x.Description
            data = x.TC_ID+str(" ")+x.Title + str(" ")+x.Description
            sentence = sentence + str(". ")+data
        print (sentence)
        sentence1 = sent_tokenize(sentence) # this create the list of sentence broken into title+description
        print sentence1

        #Create tokens of words from sentence string and transform into lower characters
        word_sent= word_tokenize(sentence.lower())
        _stopwords = set(stopwords.words('english') + list(punctuation))
        word_sent = [word for word in word_sent if word not in _stopwords]
        
        #word_sent
        #Finds the frequency of worlds from the list of words word_sent 
        freq = FreqDist(word_sent)
        #freq


        # read from sentence1 list of sentences generated from sentence token and get the ranking.
        for i,sent in enumerate(sentence1):
               for w in word_tokenize(sent.lower()):
                        if w in freq:
                                ranking[i] += freq[w]
        #ranking is the dictionary of values containing the testcases and there rankscore
        print ranking
        
        #test_list is the list of ranking from largest to smallest
        test_list = nlargest(n,ranking,key=ranking.get)
        print test_list
        
        priority_test = []
        
        #Creating the list of priority test cases to iterate in views 
        for j in test_list:
            priority_test = priority_test + [sentence1[j]]
        print priority_test
        
        tc_rank_list = {}
        for values in ranking:
            if ranking[values] in tc_rank_list:
                tc_rank_list[ranking[values]].append(values)
            else:
                tc_rank_list[ranking[values]] = [values]
                
        tc_rank_list_remove_single_val = {}
        for i in tc_rank_list:
            if len(tc_rank_list[i]) > 1:
                tc_rank_list_remove_single_val[i]=tc_rank_list[i]


        
        value_occurance,filtered_dict = dup_val(ranking)
        for i ,j in value_occurance.iteritems():
            for tc_num,tc_rank in filtered_dict.iteritems():
                if tc_rank == i:
                    print tc_num,i,j

        return locals()


##################################################################################################


def dup_val(dict_val):
    import collections
    value_occurrences = {}
    filtered_dict = {}
    value_occurrences = collections.Counter(dict_val.values())
    filtered_dict = {key: value for key, value in dict_val.items() if value_occurrences[value] > 8}
    for i , j in value_occurrences.iteritems():
        if j >= 2:
            print i,":",j

    return (value_occurrences,filtered_dict)


def priotity_result():
    result = summarize(module.tc,int(n1))
    return locals()


def index(): return dict(message="hello from duplicate.py")
