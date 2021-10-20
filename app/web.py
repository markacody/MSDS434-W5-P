# https://github.com/noahgift/pai-aws

import os
import base64
import sys
from io import BytesIO

from flask import Flask
from flask import send_from_directory
from flask import request
from flask_api import status
from flasgger import Swagger
from flask import redirect
from flask import jsonify

from sensible.loginit import logger
#from mlib import csvops
#from mlib import utils

# Create a log
log = logger(__name__)
# Create the app
app = Flask(__name__)
# Create the documentation
Swagger(app)


@app.route('/')
def home():
    """/ route redirects to API Docs: /apidocs"""
    return redirect('/apidocs')


@app.route('/favicon.ico')
def favicon():
    """Give the browser a favicon"""
    return send_from_directory(os.path.join(app.root, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/api/funcs', methods=['GET'])
def list_appliable_funcs():
    """Return a list of appliable functions
        GET /api/funcs
        ---
        responses:
            200:
                description: Returns list of appliable functions.
    """
    appliable_list = utils.appliable_functions()
    return jsonify({"funcs": appliable_list})

# Add base64 converter function
# Add aggregator functions


if __name__ == '__main__':
    log.info("Start Flask")
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
    log.info('Shutdown Flask')
