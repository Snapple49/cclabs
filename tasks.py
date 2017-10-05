from celery import Celery

from tweetcounter import countWord

app = Celery('app-server')
app.config_from_object('celeryconfig')

@app.task
def hello(name):
    return "Hello "+name

@app.task
def countWordInTweets(word):
    return countWord(word)
