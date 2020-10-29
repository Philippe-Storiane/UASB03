# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 03:49:57 2020

@author: a179415
"""

import spacy
import datetime
#import gensim

nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])

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
text = []
for method_feature in method_features:
#    first_space = method_feature.find(" ")
#    second_space = method_feature.find(" ", first_space + 1)
#    methods_words = nlp( method_feature[ second_space + 1: -1])
    data = method_feature.split()
    words =  " ".join(data[2:]) 
    class_name = data[0]
    text.append(( words, { 'className': class_name}))
#            print(method_word.lemma_)

def part_of_speech( text, pos):
    t1 = datetime.datetime.now()
    docs = nlp.pipe( text[0:20000], as_tuples=True)
    parts = {}
    for doc,context in docs:
        for tok in doc:
            if  tok.pos_ == pos:
                if tok.text in parts:
                    parts[ tok.text ] += 1
                else:
                    parts[ tok.text ] = 1
    t2 = datetime.datetime.now()
    print ( t2 - t1)
    return parts

