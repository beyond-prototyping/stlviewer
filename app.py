import os
from flask import Flask, request, url_for, render_template
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def stlviewer():
    stl_url = request.values.get('stl')
    if stl_url is None:
        stl_url = url_for('static', filename='example001.stl')
    else:
        stl_url = url_for('loadstl', url=stl_url)
    return render_template('index.html', stl_url=stl_url)


@app.route('/loadstl/<path:url>')
def loadstl(url):
    if not url.endswith('.stl'):
        return 'Invalid URL', 403
    try:
        r = requests.get(url)
    except:
        return 'Invalid URL', 403
    return r.content

if __name__ == "__main__":
    app.run(debug=os.environ.get('DEBUG', False), host='0.0.0.0', port=os.environ.get('PORT', 5000))
