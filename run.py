from flask import Flask, render_template, send_from_directory
from flask import request
import feedparser


app = Flask(__name__, static_url_path='')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory("static", path)

@app.route('/')
def index():
    return render_template('webhtml.html')
@app.route('/render', methods =['POST'])
def products():
    data = request.form
    #import pdb;pdb.set_trace()
    link = data["email"]
    NewsFeed = feedparser.parse(link)
    print(NewsFeed.entries[0])
    return render_template('renderdata.html', data=NewsFeed)


if __name__ == '__main__':
    app.run(debug=True, port=2000)