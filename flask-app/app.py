from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# data
Datasets = [
    {
        'age': '63',
        'sex': 'male',
        'chest': 'typical',
        'pressure':'145',
        'cholestoral':'233',
        'sugar':'yes',
        'cardiographic':'probable or definite',
        'heart_rate':'150',
        'angina':'0',
        'oldpeak':'2.3',
        'slope':'3',
        'flourosopy':'0',
        'thal':'fixed defect',
        'target':'no'
    },
    {
        'age': '67',
        'sex': 'female',
        'chest': 'asymptomatic',
        'pressure':'160',
        'cholestoral':'286',
        'sugar':'no',
        'cardiographic':'probable or definite',
        'heart_rate':'108',
        'angina':'1',
        'oldpeak':'1.5',
        'slope':'2',
        'flourosopy':'3',
        'thal':'normal',
        'target':'yes'
    }
]

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