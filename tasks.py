from celery import Celery

app = Celery('app-server')
app.config_from_object('celeryconfig')

@app.task
def hello(name):
    return "Hello "+name
