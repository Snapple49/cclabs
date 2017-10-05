import os
import json

def countWord(word):
    return countWordsInTweets(word)

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
            if tweet.get('in_reply_to_status_id') == None: #not a retweet?
                text = tweet.get('text')
                wordsInFile += len([x for x in text.split() if x == word]) #solution from https://stackoverflow.com/questions/34324498/python-find-words-in-string
    file.close()
    return wordsInFile
