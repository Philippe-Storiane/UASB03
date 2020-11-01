# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 03:49:57 2020

@author: a179415
"""

import json
import spacy
import datetime
#import gensim

import spacy.lang.en.stop_words as st
st.STOP_WORDS |= {"[", "]", "(", ")", "%", "+", "<", ">", ":", "*", "/", "//", "=", "void", "int", "override", "char", "long", "float", "string", "short", "boolean", "exception", "--", "null", "true", "false","main", "test", "assert", "equal", "set"}
nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
# NUM and BNANK to be explictily added as stop_word
nlp.vocab['BLANK'].is_stop = True
nlp.vocab['NUM'].is_stop = True
raw_text_filename="text-embedding"
word2vec_model = ""
spacy_pos = set()

# https://spacy.io/api/annotation#pos-tagging
spacy_pos={'ADJ',
 'ADP', #adposition in, to
 'ADV', # adverb very, tomorrow, down, where
 'AUX', # auxiliary is, has
 'CCONJ', # coordinating conj, and or but
 'DET', # determiner a, an, the
 'INTJ', # interjection ppst, ouch
 'NOUN', # noun
 'NUM', # number
 'PART', # particle s, not
 'PRON', # pronoun i, you, she
 'PROPN', # proper name Mary, Johhn
 'PUNCT', # punctuation
 'SPACE', # space
 'SYM', # symbol
 'VERB', #
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

def part_of_speech( text, pos_list):
    t1 = datetime.datetime.now()
    docs = nlp.pipe( text, as_tuples=True)
    poses = {}
    for pos in pos_list:
        poses[ pos ] = {}
    for doc,context in docs:
        for tok in doc:
            if  tok.pos_ in pos_list:
                parts = poses[ tok.pos_ ]
                if tok.text in parts:
                    parts[ tok.text ] += 1
                else:
                    parts[ tok.text ] = 1
    t2 = datetime.datetime.now()
    print ( t2 - t1)
    for pos in pos_list:
        file=open( pos+".json", "w")
        json.dump( poses[ pos ], file)
        print("dumping to file " + pos)
        # print( poses[ pos ])
        file.close()

to_remove = [
#        'ADP',
#       'ADV',
#       'CCONJ',
#       'DET',
#        'INTJ',
#       'NUM',
#       'PART',
#        'PRON',
#        'PROPN',
        'PUNCT', #yes
        'SYM' #yes
#        'X'
    ]        
# part_of_speech( text, [ 'ADP', 'ADV','CCONJ', 'DET','INTJ', 'NUM', 'PART','PRON', 'PROPN', 'SYM', 'X'])


def text_process( text, result_file ):
    # lemmatize
    # remove stop words
    # remove unecessayre part of speech
    # remove additioal stop word
    t1 = datetime.datetime.now()
    docs = nlp.pipe( text, as_tuples=True)
    result = open( result_file, 'w')
    for doc, context in docs:
        filtered_text = []
        for toc in doc:
            if (toc.pos in ['PUNCT', 'SYM'] ) or ( toc.is_stop) or ( len(toc.text) == 1):
                continue
            filtered_text.append( toc.lemma_)
        line = " ".join( filtered_text)
        result.write(context['className'])
        result.write( " ")
        result.write(line)
        result.write('\n')
    result.close()
    t2 = datetime.datetime.now()
    print( t2 - t1 )
        
        

