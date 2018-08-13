# use natural language toolkit
import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
import json,os
from numpy.random import np
from firebase import firebase
firebase = firebase.FirebaseApplication('https://nlpdb-993b1.firebaseio.com', None)

# word stemmer;l;kk
stemmer = LancasterStemmer()
training_data = []
BASE = os.path.dirname(os.path.realpath(__file__))
config = json.loads(open(BASE+'//merge.json').read())
training_data = config
# capture unique stemmed words in the training corpus
corpus_words = {}
class_words = {}
# we now have each stemmed word and the number of occurances of the word in our training corpus (the word's commonality)
# print ("Corpus words and counts: %s \n" % corpus_words)
# also we have all words in each class
# print ("Class words: %s" % class_words)
# we can now calculate a score for a new sentence


# calculate a score for a given class
def calculate_class_score(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for word in nltk.word_tokenize(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words[class_name]:
            # treat each word with same weight
            score += 1
            
            
    return score

	


# calculate a score for a given class taking into account word commonality
def calculate_class_score_commonality(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for word in nltk.word_tokenize(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words[class_name]:
            # treat each word with relative weight
            score += (1 / corpus_words[stemmer.stem(word.lower())])

            # if show_details:
            # print ("match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))
    return score

def responseId(high_class,company):
    ans_data=[]
    result = firebase.get('/'+company,None)
    ans_data = result
    for i in range(len(ans_data)):
        if ans_data[i]['class'] == high_class:
            random_ans=len(ans_data[i]['fulfillmentMessages'])
            random_ans=np.random.choice(random_ans)
            print(ans_data[i]['fulfillmentMessages'][random_ans])
            return ans_data[i]['fulfillmentMessages'][random_ans]

def getIntent(sentence,company):
    # 3 classes of training data
    # turn a list into a set (of unique items) and then a list again (this removes duplicates)
    classes = list(set([a['class'] for a in training_data]))
    for c in classes:
        # prepare a list of words within each class
        class_words[c] = []

    # loop through each sentence in our training data
    for data in training_data:
        # tokenize each sentence into words
        for word in nltk.word_tokenize(data['sentence']):
            # ignore a some things
            if word not in ["?", "'s","'t"]:
                # stem and lowercase each word
                stemmed_word = stemmer.stem(word.lower())
                # have we not seen this word already?
                if stemmed_word not in corpus_words:
                    corpus_words[stemmed_word] = 1
                else:
                    corpus_words[stemmed_word] += 1

                # add the word to our words in class list
                class_words[data['class']].extend([stemmed_word])
    # now we can find the class with the highest score
    high_class = None
    high_score = 0
    for c in class_words.keys():
        score =  calculate_class_score(sentence, c)
        print ("Class: %s  Score: %s \n" % (c, score))
        if score > high_score:
                high_class = c
                high_score = score
    # print("calculate_class_score",high_score,"class",high_class)
    high_class1 = None
    high_score1 = 0
    # now we can find the class with the highest score
    for c in class_words.keys():
        print ("Class: %s  Score: %s \n" % (c, calculate_class_score_commonality(sentence, c)))
        score =  calculate_class_score_commonality(sentence, c)
        if score > high_score1:
                high_class1 = c
                high_score1 = score
    # topScoringIntent=high_score+high_score1
    print("calculate_class_score",high_score,"class",high_class)
    print("calculate_class_score",high_score1,"class",high_class1)
    high_class2 = None
    high_score2 = 0
    total_score=[]
    for c in class_words.keys():
        score4 = calculate_class_score_commonality(sentence, c)
        score3 = calculate_class_score(sentence, c)
        print(c,score4,score3)
        # print(score3)
        total_score=score4+score3
        print(total_score)
        if total_score > high_score2:
                high_class2 = c
                high_score2 = total_score
    fulfillmentMessages = responseId(high_class2,company)
    print(high_class2,high_score2)
    data = {}
    data["total_score"]=[high_class2,high_score2]
    data["high_class"]=[high_class,high_score]
    data["high_class1"]=[high_class1,high_score1]
    data["fulfillmentMessages"]=fulfillmentMessages
    # print("class",class_words)
    return data

    



# getIntent("hi","cgcel")



 
