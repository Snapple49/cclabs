from celery import Celery

from tweetcounter import countWord

app = Celery('app-server')
app.config_from_object('celeryconfig')

#def countWord(word):
#    return 100

@app.task
def hello(name):
    return "Hello "+name

@app.task
def countWordInTweets(word):
    return countWord(word)
