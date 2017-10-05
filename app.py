import os
from flask import Flask, render_template, request, make_response, jsonify
import json

import tweetcounter
import tasks

app = Flask(__name__)

@app.route("/") 
def landingPage():
    return render_template('index.html')

@app.route("/tweetAPI/0.1/pronouncount", methods = ['GET'])
def pronouncount():
    return wordcount("han,hon,hen,den,det,denne,denna")

@app.route("/tweetAPI/0.1/wordcount", methods = ['POST'])
def wordcount(formdata = None):
    if formdata is None:
        formdata = request.form['words']
    words = formdata.split(',')
    print words
    jsonresult = {}
    results = []
    for word in words:
        results.append(tasks.countWordInTweets.delay(word))

    for res in results:
        jsonresult.update(res.wait()) 
        
    resp = make_response(jsonify(jsonresult))
    return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
