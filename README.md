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






# FAQ:

## 1. * Install prebuilt node (11.12.0) ..... done.You do not have sufficient privilege to perform this operation  

In windows,run as administrator,then run the commend.

## 2. Why do we need Flask-CORS?  

In order to make cross-origin requests - e.g., requests that originate from a different protocol, IP address, domain name, or port - you need to enable Cross Origin Resource Sharing (CORS). Flask-CORS handles this for us.

## 3. Expected linebreaks to be 'LF' but found 'CRLF' linebreak-style  

If you are using vscode and you are on Windows i would recommend you to click the option at the bottom-right of the window and set it to LF from CRLF. Because we should not turn off the configuration just for sake of removing errors on Windows ,Then save the file again



## Reference:
*https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/*

