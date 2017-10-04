import os
from flask import Flask, render_template, request
import tweetcounter

import tasks

app = Flask(__name__)

@app.route("/")
def hello():
    wordstring = request.args.get('words', '')
    words = wordstring.split(',')
    results = []
    for word in words:
        results.append(tasks.countWordInTweets.delay(word))
        
    for res in results:
        res.wait()
    
    
    return render_template('index.html', celery=results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
