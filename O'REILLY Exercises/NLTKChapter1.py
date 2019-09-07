#/Users/randou/Esther/Brandeis/2019 Fall/LING131A NLP/Exercises
# -*- coding: utf-8 -*-

import nltk
nltk.download()
from nltk.book import *
from nltk.book import text1
import pandas as pd


# =============================================================================
# 1.3 Searching Text
# =============================================================================

text1.concordance('monstrous')  #appearance of a word
text1.similar('monstrous')  #words used in the similar context
text1.common_contexts(['monstrous', 'mystifying'])
text1.dispersion_plot(['love', 'peace', 'luck', 'fortune'])
text1.generate()


# =============================================================================
# 1.4 Counting Vocabulary
# =============================================================================

len(text1)
len(sorted(set(text1)))
len(set(text1)) / len(text1) # lexical richness
text1.count('love')

def lexical_diversity(text):
    return len(set(text)) / len(text)
def percentage(count, total):
    return 100 * count / total
lexical_diversity(text1)
percentage(text1.count('success'), len(text1))

text = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
summary = {'Name': [i.name for i in text],
           'Tokens': [len(i) for i in text],
           'Types': [len(set(i)) for i in text],
           'Lexical diversity': [len(set(i)) / len(i) for i in text]}
summary = pd.DataFrame(summary)


# =============================================================================
# 2. A Closer Look at Python: Texts as Lists of Words
# =============================================================================

sent1 + sent4
sent1.append('some')
sent1.index('me')
' ',join(['Monty', 'Python'])
'Monty Python'.split()


# =============================================================================
# 3. Computing with Language: Simple Statistics
# =============================================================================

fdist1 = FreqDist(text1)
fdist1.most_common(50)
fdist1['fortune']
fdist1.plot(50, cumulative=True)
fdist1.hapaxes() # words that only happened once

# Search for long words
V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)
sorted(w for w in set(text1) if len(w) > 7 and fdist1[w] > 7)

# Collocation: sequence of words that occur together unusually often
# Bigrams: a list of word pairs
list(bigrams(['more', 'is', 'said', 'than', 'done']))
text4.collocations()

# Other Functions for NLTK Frequency Districutions
fdist1 = FreqDist(text1)
fdist = FreqDist(samples)    # create a frequency distribution containing the given samples
fdist[sample] += 1	         # increment the count for this sample
fdist['monstrous']	         # count of the number of times a given sample occurred
fdist.freq('monstrous')	     # frequency of a given sample
fdist.N()	                 # total number of samples
fdist.most_common(n)	         # the n most common samples and their frequencies
for sample in fdist:	 sample  # iterate over the samples
fdist.max()	                 # sample with the greatest count
fdist.tabulate()	             # tabulate the frequency distribution
fdist.plot()	                 # graphical plot of the frequency distribution
fdist.plot(50, cumulative=True)	 # cumulative plot of the frequency distribution
fdist1 |= fdist2	             # update fdist1 with counts from fdist2
fdist1 < fdist2	             # test if samples in fdist1 occur less frequently than in fdist2


# =============================================================================
# 4. Back to Python: Making Decisions and Taking Control
# =============================================================================

# Word Comparison Operators
t = 'test'
s = 'String For test'
s.startswith(t)	# test if s starts with t
s.endswith(t)	# test if s ends with t
t in s	        # test if t is a substring of s
s.islower()	    # test if s contains cased characters and all are lowercase
s.isupper()	    # test if s contains cased characters and all are uppercase
s.isalpha()	    # test if s is non-empty and all characters in s are alphabetic
s.isalnum()	    # test if s is non-empty and all characters in s are alphanumeric
s.isdigit()	    # test if s is non-empty and all characters in s are digits
s.istitle()	    # test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)

tricky = sorted(w for w in set(text1) if 'cie' in w or 'cei' in w)
for word in tricky:
    print(word, end=' ')

# =============================================================================
# 5. Automatic Natural Language Understanding
# =============================================================================

# Challengings:
    # Word Sense Disambiguation
    # Pronoun Resolution
    # Generating Language Output
    # Machine Translation
    # Spoken Dialog Systems
    # Textual Entailment
    # Limitations of NLP



# =============================================================================
# 8. Exercises
# =============================================================================

# Exercise 3
['Monty', 'Python'] * 20
3 * sent1

# Exercise 4
len(text2)
len(set(text2))

# Exercise 8
# the purpose of this expression is to count distinct words
# first step: use set() to drop duplicate words
# second step: counting

# Exercise 15
sorted(w for w in text5 if w.startswith('b'))

# Exercise 22
sorted(w for w in FreqDist(text5) if len(w)==4)

# Exercise 24
[w for w in text6 if w.endswith('ise')]
[w for w in text6 if 'z' in w]
[w for w in text6 if 'pt' in w]
[w for w in text6 if w.islower() or w.istitle()]

# Exercise 25
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
[w for w in sent if w.startswith('sh')]
[w for w in sent if len(w)>4]
























