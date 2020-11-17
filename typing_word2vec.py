# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:58:27 2020

@author: a179415
"""

import spacy
from gensim.models import KeyedVectors
from gensim.corpora import Dictionary

nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])

embedding_file = open( "text-embedding")
embeddings=embedding_file.readlines()
classes = set()
for embedding in embeddings:
    data = embedding.split(" ")
    classes.add( data[0])
    word = ''

words = set()
for className in classes:
    word = ''
    print("className " + className)
    begin_word = 0
    begin_separator = -1
    end_separator = -1
    for index in range(len ( className)):
 #       print( begin_separator)
        if not className[ index ].islower():
            end_separator = index
            if begin_separator == -1:
                begin_separator = index
 #               print("begin sep " + str( begin_separator))
                if index > begin_word:
                    word = className[begin_word: index].lower()
                    words.add( word )
                    print( word )
                    begin_word = -1
                
        else:
            if end_separator == index - 1:
 #               print( "end sep " + str(end_separator) )                
                if end_separator > - 1:
                    begin_word = end_separator
 #                   print( "begin word " + str(begin_word) )
                begin_separator =  -1
    if begin_word != -1:
        word = className[begin_word:].lower()
        words.add( word )
        print( word )        
                
