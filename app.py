from flask import Flask, jsonify,render_template
from flask_cors import CORS
from data.preprocessing import preprocessing
import json
from flask import request
from use_model import *


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__,static_folder="./dist/static", template_folder="./dist")
app.config.from_object(__name__)

@app.route("/")
def home():
    '''
        当在浏览器访问网址时，通过 render_template 方法渲染 dist 文件夹中的 index.html。
        页面之间的跳转交给前端路由负责，后端不用再写大量的路由
    '''
    return render_template('index.html')


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
result="none"
@app.route('/datasets/submit', methods=['GET','POST'])
def submit():  
  global INFO
  global result
  response_object = {'status': 'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    print(post_data)
    age=int(post_data.get('age'))
    sex=int(post_data.get('gender'))
    chest=int(post_data.get('selected_pain'))
    pressure=float(post_data.get('bloodpressure'))
    cholestoral=int(post_data.get('cholestoral'))
    heart_rate=float(post_data.get('heart_rate'))
    oldpeak=float(post_data.get('oldpeak'))
    floursopy=int(post_data.get('selected_ca'))
    #result=predict_final(63,1,1,145,150,2.3,3,0)
    result=predict_final(age,sex,chest,pressure,cholestoral,heart_rate,oldpeak,floursopy)
    print(result)
    INFO=[]
    # result="none"
    INFO.append(post_data)
    # INFO.append({'thalresult':result})
    # response_object['result'] = result
    print()
  else:
    response_object['info'] = INFO
    response_object['result'] = result
    # result="none"
  return jsonify(response_object)
if __name__ == '__main__':
    app.run()