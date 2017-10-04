import os
from flask import Flask, render_template, request

import tweetcounter
import json


import tasks

app = Flask(__name__)

@app.route("/tweetalyzerAPI/0.1", methods = ['GET', 'POST'])
def wordcount():
    formdata = request.form['words']
    words = wordstring.split(',')
    results = []
    jsonresult = {}
    for word in words:
        results.append(tasks.countWordInTweets.delay(word))
        jsonresult[word]=0
        
    for word in words:
        for res in results:
            jsonresult[word] = res.wait()
        
    
    return render_template('index.html', json=jsonresult)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
