#/Users/randou/Esther/Brandeis/2019 Fall/LING131A NLP/Exercises
# -*- coding: utf-8 -*-
# 2. Accessing Text Corpora and Lexical Resources

import nltk
nltk.download()
from nltk.book import *


# =============================================================================
# 1. Accessing Text Corpora
# =============================================================================

nltk.corpus.gutenberg.fileids() # file indentifier in this corpus
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt')).concordance('surprize')

# Gutenberg Corpus
from nltk.corpus import gutenberg
emma = gutenberg.words('austen-emma.txt')
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))      #letter count
    num_words = len(gutenberg.words(fileid))    #word count
    num_sents = len(gutenberg.sents(fileid))    #sentence count (each sentence is a list of words)
    num_vocab = len([set(w.lower()) for w in gutenberg.words(fileid)])  #unique vocabulary
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

# Web and Chat Text Corpus
from nltk.corpus import webtext # Web texts
[fileid for fileid in webtext.fileids()]
from nltk.corpus import nps_chat # Naval Postgraduate
[fileid for fileid in nps_chat.fileids()]

# Brown Corpus
from nltk.corpus import brown
brown.categories() # categories attribute
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + fdist)































