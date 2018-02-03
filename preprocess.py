from nltk.tokenize import word_tokenize
print('imported tokenize')
import re
print('imported re')
import ngrams #we made this file

known_threshold = 1

def binary_search(key,l):
    low_bound = -1
    high_bound = len(l)
    while True:
        check = (low_bound + high_bound)//2
        if check == low_bound:
            return False
        item = l[check]
        if item == key:
            return True
        elif item < key:
            low_bound = check
        else:
            high_bound = check

def preprocess(text):
    return word_tokenize(re.sub(r'[\*~\^]',r'',text.lower()))

users = ['neiltyson','realDonaldTrump','rihanna','elonmusk','KingJames']
by_user_corpus = {}
all_tweets = []

for user in users:
    with open(user + '_tweets.txt','r',encoding = 'utf-8') as f:
        text = f.read()

    tokenized = preprocess(text)
    corpus_word_count = len(tokenized)

    by_user_corpus[user] = tokenized
    all_tweets.extend(tokenized)

print('finished tokenizing')

words = ngrams.ngram(all_tweets,1)
print('counted words')

flipped = ngrams.flip_dict(words)
counts = sorted(list(flipped))
print('flipped')

unknowns = sorted([word for i in counts[:known_threshold] for word in flipped[i]])
print('enumerated unknowns')

knowns = sorted([word for i in counts[known_threshold:] for word in flipped[i]])
print('enumerated knowns')

assert(len(unknowns) + len(knowns) == sum(len(value) for key, value in flipped.items()))

def is_known(word):
    return binary_search(word,knowns)

print('Preprocessed')

##tweets_by_user_unks = {}
##
##for user in users:
##    tweets_by_user_unks[user] = [[(word if is_known(word) else '<unk/>') for word in comment] for comment in tweets_by_user[user]]
##    
##print('marked unknowns')
##
##with open('dict.txt','w',encoding='utf-8') as fh:
##	fh.write(str(tweets_by_user_unks))
