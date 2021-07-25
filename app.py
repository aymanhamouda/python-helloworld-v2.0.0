
from flask import Flask, app
from flask import json
import logging
from werkzeug.datastructures import MIMEAccept

from werkzeug.wrappers import response
app = Flask(__name__)
@app.route('/status')
def healthcare():
    response=app.response_class(
        response=json.dump({"result":"ok-Healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('status requist successfull')
    return response

@app.route('/metrics')
def metrics():
    response=app.response_class(
        {"status":"success", "code":0, "data":{"userCount":140, "userCountActive":23,}
        },
        status=200,
        mimetype='application/json'   
    )
    app.logger.info('Metrics requist succesfull')
    return response
@app.route('/')
def hellow():
    return "Hello World!"

if __name__== "_main_":
    app.run(host='0.0.0.0')