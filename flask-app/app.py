from flask import Flask, jsonify
from flask_cors import CORS
from data.preprocessing import preprocessing
import json
from flask import request


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)
# CORS(app, resources={r"/*": {"origins": "*"}})

# data
Datasets =json.loads(preprocessing())
Datasets_blood=[
    {
      'x': 1,
      'y': 2,
    },
    {
      'x': 10,
      'y': 11,
    },
    {
      'x': 100,
      'y': 101,
    }]


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

@app.route('/datasets/blood', methods=['GET'])
def blood():
    return jsonify({
        'status': 'success',
        'datasets': Datasets_blood
    })


INFO=[]
@app.route('/datasets/submit', methods=['GET','POST'])
def submit():  
  global INFO
  response_object = {'status': 'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    print(post_data)
    # print(post_data.get('selected'))
    # BOOKS.append({
    #     'gender': post_data.get('gender'),
    # })
    INFO=[]
    INFO.append(post_data)
    print()
  else:
    response_object['info'] = INFO
  return jsonify(response_object)
if __name__ == '__main__':
    app.run()