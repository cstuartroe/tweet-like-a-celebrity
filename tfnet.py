import math
print('imported math')
##import tensorflow
##print('imported tensorflow')
import numpy as np
print('imported numpy')
from preprocess import *
print('imported preprocess')
import operator
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
print('imported sys')
from datetime import datetime
print('imported datetime')

unknowns = []   #it shouldn't need to get used, so I'm resetting unknowns to an empty array
                #so I don't accidentally use it

vocab_size = len(knowns)

word_indices = {}
for i  in range(vocab_size):
    word_indices[knowns[i]] = i

def word2int(word):
    if is_known(word):
        return word_indices[word]
    else:
        return vocab_size
    return vec

def word2vec(word):
    vec = [0] * (vocab_size + 1)
    vec[word2int(word)] = 1
    return vec

def tweet2vec(tweet):
    #assert(tweet[0] == '<tweet>' and tweet[-1] == '</tweet>')
    vec = [0] * (vocab_size + 1)
    for word in tweet:
        vec[word2int(word)] += 1
    return vec

def softmax(array):
    exps = [math.e**n for n in array]
    total = sum(exps)
    return [n/total for n in exps]

def magnitude(vec):
    return math.sqrt(np.dot(vec,vec))

def scale_vector(vec,length=1):
    mag = magnitude(vec)
    return [(x/mag)*length for x in vec]

def veccos(vec1,vec2):
    return np.dot(vec1,vec2)/(magnitude(vec1)*magnitude(vec2))

def angle(vec1,vec2):
    return np.arccos(veccos(vec1,vec2))

average_word_vector = scale_vector(tweet2vec(all_tweets)[:-1])

user_word_vectors = {}

for user in users:
    unnormed_vector = scale_vector(tweet2vec(by_user_corpus[user])[:-1])
    user_word_vectors[user] = scale_vector(np.subtract(unnormed_vector,average_word_vector))

def percent_alike(tweet):
    tweet_vector = tweet2vec(preprocess(tweet))[:-1]
    similarities = [angle(tweet_vector,user_word_vectors[user]) for user in users]
    maximum = max(similarities)
    similarities = [maximum - value for value in similarities]
    return softmax(scale_vector(similarities, length=5))

