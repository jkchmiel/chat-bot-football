import sys
from flask import Flask
from flask import make_response
from flask import request
import json
from response import Response

app = Flask(__name__)


@app.route('/')
def homepage():
    return "<h1> DialogFlow chat-bot webhook build under: </h1><p>Python: {ver}</p>".format(ver=sys.version)


@app.route('/webhook', methods=['POST'])
def webhook():

    req = request.get_json(silent=True, force=True)
    print('Request:\n{0}'.format(json.dumps(req, indent=4)))

    response = Response.prepare_response(req)
    print('Response:\n{0}'.format(response))

    r = make_response(response)
    r.headers['Content-Type'] = 'application/json'
    return r


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
