import os
import json
import re

def countWord(word):
    dict = {word:countWordsInTweets(word)}
    return dict

def countWordsInTweets(word):
    wordsInTweets = 0
    for filename in os.listdir('./data'):
        wordsInTweets += countWordsInFile(filename, word)
    return wordsInTweets

def countWordsInFile(filename, word):
    wordsInFile = 0
    file = open('./data/' + filename)
    for line in file:
        if line.startswith('{'):
            tweet = json.loads(line)
            if tweet.get('retweeted_status') == None: #not a retweet?
                text = tweet.get('text')
                wordsInFile += len([x for x in preprocessString(text).split() if x == word])
    return wordsInFile

def preprocessString(str):
    str = re.sub('[^a-zA-Z]+', ' ', str.lower())
    str = ' ' + str + ' '
    return str
