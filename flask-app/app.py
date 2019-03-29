from flask import Flask, jsonify
from flask_cors import CORS
from data.preprocessing import preprocessing
import json


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# data
Datasets =json.loads(preprocessing())

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/datasets', methods=['GET'])
def all_datasets():
    return jsonify({
        'status': 'success',
        'datasets': Datasets
    })


if __name__ == '__main__':
    app.run()