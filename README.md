# project-HeartDisease
COMP9321 2019 T1 Group Project: Heart Disease

Group name:404 NOT FOUND

Hanxu Wu (z5148463)  
Hao Wu (z5132458)  
Jinci Zhang (z5136172)  
Mingda Liu (z5019749)  

## File Structure  

`data` - raw data

`flask-app` - backend

`client` - Vue front-end

`heatmag.png`: shows the correlation for each attribute.

`logstic.py`:  contains 4 models without applying data redunction. Model trained are stored  in .sav files

`plots.py` : contains functions to generate graphs to demo my models selections. Will add more graphs later

`read_data.py` : use this file to read the training data

`use_model.py` : are prepared for future usage. A function to read from saged models(.sav) and read from 

front end input to and use the model to predict heart diseases.

## Develope plan  

`master`-------------------------------->: merge from develope branch stable versions  

`dev`------------------->:merge from features branch  

`feature-visualize`-------->: feature frontend/backend  

`feature-ML/DL`------->: feature train the models  

`feature-plot`------->: prepare the visualize data 

`feature-selection`------->: select feature

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

```
python app.py
```

# Front-end


## test if Vue works fire up the server  

```
$ cd client

npm install

npm run dev
```

then open :  

http://localhost:8080/#/


### Final version submission

1.Drag the test data to the Data/heart folder.

To re-generate my final model. First remove final_model.sav 

2.then run final_model.py which will generate my final model again and stored as final_model.sav.

3. Run read_model.py, which will read from the saved model and print the result.