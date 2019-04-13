April 7th, 2018
feature-ML/DL
heatmag.png shows the correlation for each attribute.

logstic.py contains 4 models without applying data redunction. Model trained are stored  in .sav files

plots.py contains functions to generate graphs to demo my models selections. Will add more graphs later

read_data.py use this file to read the training data

use_model.py are prepared for future usage. A function to read from saged models(.sav) and read from 
front end input to and use the model to predict heart diseases.


Aprial 10th 2018,

now we change to predict the thal
for tutor assess my accurancy, run my read_model.py
use_model.py is for front end



Final version submission

1.Drag the test data to the Data/heart folder.

To re-generate my final model. First remove final_model.sav 

2.then run final_model.py which will generate my final model again and stored as final_model.sav.

3. Run read_model.py, which will read from the saved model and print the result.