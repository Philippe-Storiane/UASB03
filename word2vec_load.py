# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 03:49:57 2020

@author: a179415
"""

import spacy
import datetime
#import gensim

nlp = spacy.load("en_core_web_sm")

raw_text_filename="text-embedding"
word2vec_model = ""
spacy_pos = set()
spacy_pos={'ADJ',
 'ADP',
 'ADV',
 'AUX',
 'CCONJ',
 'DET',
 'INTJ',
 'NOUN',
 'NUM',
 'PART',
 'PRON',
 'PROPN',
 'PUNCT',
 'SPACE',
 'SYM',
 'VERB',
 'X'}
i = 0
method_file = open(raw_text_filename, encoding="utf-8")
method_features = method_file.readlines()
t1 = datetime.datetime.now()
for method_feature in method_features:
#    first_space = method_feature.find(" ")
#    second_space = method_feature.find(" ", first_space + 1)
 #   methods_words = nlp( method_feature[ second_space + 1: -1])
    data = method_feature.split()
    method_words = nlp( " ".join(data[2:])) 
    i = i  + 1   
    if (i > 5000):
        break
    if ( i % 1000) == 0:
        t2 = datetime.datetime.now()
        print("line " + str(i))
        print( t2 - t1)
        t1 = t2
#    for method_word in methods_words:
#        if ( method_word.pos_ == 'NUM'):
#            print(method_word.lemma_)
