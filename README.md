# project-HeartDisease
COMP9321 2019 T1 Group Project: Heart Disease

## File Structure  

`data` - raw data

`flask-app` - backend

`client` - Vue front-end


## Develope plan  

`master`-------------------------------->: merge from develope branch stable versions  

`develope`------------------->:merge from features branch  

`feature-flask`-------->: feature frontend/backend  

`feature-ML/DL`------->: feature train the models  

Note：create your own branch and develope on your own branch.

## System architecture  

frontend : bootstrap,Vue,chartjs

backend : flask


## Setting up the environment  

### 1. clone the project  
```
git clone https://github.com/hanxuwu/project-HeartDisease.git
```

### 2. set up the virtualenv  

```
> virtualenv .
```

__for windows:__
```
> .\Scripts\activate
```


__for MacOs:__
```
> source ./bin/activate
```

### 3. install requirements  

```
> pip3 install -r requirements.txt
```
# Back-end

## Setting the environment  

## 1. install flask-cors

```
> pip install flask-cors
```

## 2. create flask-app/app.py  
```
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
```
## 3. open your browser

*http://localhost:5000/ping*


# Front-end

## Setting the environment  

## 1. install nodeenv
```
pip install nodeenv==1.3.3  
```

## 2. activate the nodeenv
```
nodeenv env
windows: .\env\Scripts\activate
npm --version
node --version
npm list -g --depth 0
```
npm version:6.9.0
node verson:v11.12.0
vue-cli@2.9.6


## 3. install vue-cli
```
npm install -g vue-cli
```

## 4. initial the vue  
```
vue init webpack client
```

`first three question using default`
`Vue build`:?Runtime + Compiler  
`Install vue-router?`:?Yes  
`Use ESLint to lint your code?`:?Yes  
`Pick an ESLint preset`:?Airbnb  
`Set up unit tests`:?No  
`Setup e2e tests with Nightwatch`:?No  
`Should we run npm install for you after the project has been created`: Yes, use NPM 

## 5. test if Vue works fire up the server
```
$ cd client
$ npm run dev
```
http://localhost:8080/#/

## 6. Add a new component to the "client/src/components" folder called Ping.vue:

```
<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: 'Ping',
  data() {
    return {
      msg: 'Hello!',
    };
  },
};
</script>
```

## 7. Update client/src/router/index.js to map '/' to the Ping component like:
```
import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Ping',
      component: Ping,
    },
  ],
});
```

## 8. To connect the client-side Vue app with the back-end Flask app, we can use the axios library to send AJAX requests.

```
npm install axios
```
axios@0.18.0

## 9.Update the script section of the component, in Ping.vue, like so:
```
<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
```

## 10.Fire up the Flask app in a new terminal window. You should see pong! in the browser at http://localhost:8080. Essentially, after we get back a response from the back-end, we set msg to the value of data from the response object.

## 11.install the bootstrap  
```
npm install bootstrap
```
bootstrap@4.3.1

## 12.Import the Bootstrap styles to client/src/main.js:

```
import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import App from './App';
import router from './router';

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
```

## 13. Update the style section in client/src/App.vue:
```
<style>
#app {
  margin-top: 60px
}
</style>
```

## 14. run app.py and npm run dev

## 15. add the home page vue  

### a. write the home component in components/Home.vue   
### b. setting the router in router/index.js  


## 16. add components/utilComponents/*  

## 17. register in main.js  

## 18. install chart.js  

```
npm install vue-chartjs chart.js --save
```
chart.js@2.8.0
vue-chartjs@3.4.2

## 19. open  *http://localhost:8080/home#/* view the chart

## 20. install  bootstrap vue
```
npm i vue bootstrap-vue bootstrap
```
bootstrap-vue@2.0.0-rc.16
vue@2.6.10

## 21. register BootstrapVue plugin in your app entry point:
```
// app.js
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)
And import Bootstrap and BootstrapVue css files:

// app.js
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

```

## 22. Move the Navibar to App.vue:

## 23. Setting the stats path in Navi.vue and index.js
```
<b-nav-item href="#/stats">Stats</b-nav-item>
```

## 24. modify the Stats.vue add the table and write scripts to get data

## 25. Add a list of books to server/app.py:
```
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
]
```

## 26. Add the route handler:  
```
@app.route('/datasets', methods=['GET'])
def all_datasets():
    return jsonify({
        'status': 'success',
        'datasets': Datasets
    })
```

## 27. check the http://localhost:5000/datasets  got the json data
```
{
  "datasets": [
    {
      "age": "63", 
      "angina": "0", 
      "cardiographic": "probable or definite", 
      "chest": "typical", 
      "cholestoral": "233", 
      "flourosopy": "0", 
      "heart_rate": "150", 
      "oldpeak": "2.3", 
      "pressure": "145", 
      "sex": "male", 
      "slope": "3", 
      "sugar": "yes", 
      "target": "no", 
      "thal": "fixed defect"
    }, 
  ], 
  "status": "success"
}
```

## 28. preprocess the data and to json form

## 29. add background color in app.vue and set different background in stats.vue  

## 30. add another pie-chart  

## 31. Test the chartjs and VueChartjs  

## 32. Test npm stats  
Reference:

*http://npm-stats.org/#/*

*https://github.com/apertureless/npm-stats*

*https://hackernoon.com/lets-build-a-web-app-with-vue-chart-js-and-an-api-544eb81c4b44*  

*https://api.npmjs.org/downloads/range/2017-01-01:2017-04-19/vue*  

## 33. Add Vue-scatter  

## 34. add sample Resting Blood Pressure data   

## 35. add  faxios.js to seperate the axios data from the chatData1  

   TODO:  havent't figure out yet!!!

## 36. make the header of the stats table fixed

   TODO:  havent't figure out yet!!!
   
## 37. make the Navibar fixed 

  add the `fixed="top"` attribute to *Naviibar.vue*  to make the navi bar always on the top

  problem : the navibar hide the stats title

  solution: add some <hr>  


## 38. Write the predict page
  

  button `variant="info"` change the button color  

  button '`click="onSubmit" `  call the js function  

  remember change the name of `name="radio-options"` when multiples

  ```
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

  ```

  ```
  methods: {
    addBook(payload) {
      const path = "http://localhost:5000/datasets/submit";
      axios
        .post(path, payload)
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        gender: this.selected,
        age: this.age,
        selected_pain: this.selected_pain,
        bloodpressure: this.bloodpressure,
        cholestoral: this.cholestoral,
        selected_bloodsugar: this.selected_bloodsugar,
        heart_rate: this.heart_rate,
        selected_slope: this.selected_slope,
        selected_angina: this.selected_angina,
        oldpeak: this.oldpeak,
        selected_ca: this.selected_ca,
        selected_electrocardiographic: this.selected_electrocardiographic
      };
      this.addBook(payload);
    }
  },
  ```


  Reference:  
  
  https://bootstrap-vue.js.org/docs/components/form-radio#grouped-radios

  https://getbootstrap.com/docs/4.1/components/buttons/#methods

  http://www.cvdcheck.org.au/calculator/






# FAQ:

## 1. * Install prebuilt node (11.12.0) ..... done.You do not have sufficient privilege to perform this operation  

In windows,run as administrator,then run the commend.

## 2. Why do we need Flask-CORS?  

In order to make cross-origin requests - e.g., requests that originate from a different protocol, IP address, domain name, or port - you need to enable Cross Origin Resource Sharing (CORS). Flask-CORS handles this for us.

## 3. Expected linebreaks to be 'LF' but found 'CRLF' linebreak-style  

If you are using vscode and you are on Windows i would recommend you to click the option at the bottom-right of the window and set it to LF from CRLF. Because we should not turn off the configuration just for sake of removing errors on Windows ,Then save the file again

## 4. Vue-cli setting backgroudcolor for specific page  
add wrapper  
```
.wrapper{
  background-color: #ffffff;
}
```



## Reference:
*https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/*

