from celery import Celery

import tweetcounter

app = Celery('app-server')
app.config_from_object('celeryconfig')

@app.task
def hello(name):
    return "Hello "+name

@app.task
def countWordInTweets(word):
    return tweetcounter.countWord(word)
