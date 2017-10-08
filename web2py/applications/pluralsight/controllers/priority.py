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

        #sents = excel_read('workitems.xlsx',1)

#         assert n <= len(sentence)
#         n = len(sentence)

#         if('.py' in sys.argv[1]):
#                 word_sent= word_tokenize(tc.lower())

        n = len(read_db_data)
        print n
        #creating a string reading the excel list data to single string
        sentence1 = ""
        sentence = " "
        new_sentence = ""
        for x in read_db_data:
#             print x.Title + x.Description
            data = x.TC_ID+str(" ")+x.Title + str(" ")+x.Description
            sentence = sentence + str(". ")+data
        print (sentence)
        sentence1 = sent_tokenize(sentence)
        print sentence1
        
        
#         word_sent= word_tokenize(sentence.lower())

        word_sent= word_tokenize(sentence.lower())
        _stopwords = set(stopwords.words('english') + list(punctuation))
        word_sent = [word for word in word_sent if word not in _stopwords]
        
        #word_sent

        freq = FreqDist(word_sent)
        #freq

# ranking = defaultdict(int)
#         ranking_with_tc = defaultdict(int)
        
        for i,sent in enumerate(sentence1):
               for w in word_tokenize(sent.lower()):
                        if w in freq:
                                ranking[i] += freq[w]

        print ranking
        
        test_list = nlargest(n,ranking,key=ranking.get)
        print test_list
        priority_test = []
        
        for j in test_list:
            priority_test = priority_test + [sentence1[j]]
        print priority_test
        
        
        return locals()

    
    
    
    
    
    
##################################################################################################

def summarize(tc,n=10):
        read_db_data = db(db.polarion).select()

#         sentence = excel_read('workitems.xlsx',1)

        ranking = defaultdict(int)

        #sents = excel_read('workitems.xlsx',1)

#         assert n <= len(sentence)
#         n = len(sentence)

#         if('.py' in sys.argv[1]):
#                 word_sent= word_tokenize(tc.lower())

        n = len(read_db_data)
        #creating a string reading the excel list data to single string
        for x in read_db_data:
            data = x.Title + x.Description
            new_sentence = ". ".join(data)
        print type(new_sentence)

        #for_lower=excel_read('workitems.xlsx',1)

        #print for_lower
        word_sent= word_tokenize(new_sentence.lower())

        _stopwords = set(stopwords.words('english') + list(punctuation) + list("RHCert-TC"))
        
         # _stopwords

        word_sent = [word for word in word_sent if word not in _stopwords]
        #word_sent

        freq = FreqDist(word_sent)
        #freq


        ranking = defaultdict(int)
        ranking_with_tc = defaultdict(int)

        for i,sent in enumerate(sentence):
                for w in word_tokenize(sent.lower()):
                        if w in freq:
                                ranking[i] += freq[w]

        print ranking

        #Setting the rank afer adding the tc_rank dictionary values from testcase.py file
        if('.py' in sys.argv[1]):
                ranking_with_tc = Counter(ranking) +  Counter(module.tc_rank)

        if('.xlsx' in sys.argv[1]):
                ranking_with_tc = Counter(ranking) +  Counter(tc_rank)





        #sent_idx1 = nsmallest(n,ranking,key=ranking.get)

        sent_idx2 = nlargest(n,ranking,key=ranking.get)

        #sent_idx

        #[sentence[j] for j in sorted(sent_idx)]
        #for j in sent_idx1:
        #       print j," -> "+sentence[j]

        print ("/nLarget_Priority/n")
        for j in sent_idx2:
                print "TC",j," -> "+sentence[j]
                #print sentence[j]

        print("---------#####--Priority Considering Feature and Bug Fixes---######------------")
         #ranking_with_tc = Counter(ranking) +  Counter(module.tc_rank)

        sent_idx_rank = nlargest(n,ranking,key=ranking_with_tc.get)



# Adding the workbook sheet for Priortized test considering Bugs and Feature
        data = []
        x = []
        #wb = xlwt.Workbook()
        ws = wb.add_sheet("Priority_Test")


        for j in sent_idx_rank:
                print "TC",j," -> "+sentence[j]
                x = ("TC"+str(j),sentence[j])
                data.append(x)
#       print data
        ws.write(0,0,"Test case No")
        ws.write(0,1,"Test case title")

        for i, row in enumerate(data):
                for j, col in enumerate(row):
                        ws.write(i+1, j, col)
        #ws.col(0).width = 256 * max([len(row[0]) for row in data])
        #wb.save("myworkbook.xls")


#Adding the ranking values
        excel_func("ranking","ranking.xlx",ranking_with_tc,"Tc_case","Rank_score")
        # Adding the workbook sheet for Priortized test

        data1 = []
        x1 = []
        #wb = xlwt.Workbook()
        ws = wb.add_sheet("Priority_Test_wo")


        for j in sent_idx2:
                print "TC",j," -> "+sentence[j]
                x1 = ("TC"+str(j),sentence[j])
                data1.append(x1)
        #print data

        for i, row in enumerate(data1):
                for j, col in enumerate(row):
                        ws.write(i, j, col)

        wb.save("myworkbook.xls")

        #excel_func("ranking","ranking.xlx",ranking)

def excel_func(sheet_name,wb_name,dict_val,col1_name,col2_name):
        ws = wb.add_sheet(sheet_name)
        ws.write(0,0,col1_name)
        ws.write(0,1,col2_name)

        for i,row in enumerate(dict_val.items()):
                for j,col in enumerate(row):
                        ws.write(i+1,j,col)

def excel_read(sheet_name,col_number):
        data = xlrd.open_workbook(sheet_name)
        table = data.sheets()[0]
        val =  table.col_values(col_number)
        return val
        #print(val)


def priotity_result():
    result = summarize(module.tc,int(n1))
    return locals()

def index(): return dict(message="hello from priority.py")
