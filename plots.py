import csv
import pandas as pd
import os
import numpy as np
from read_data import *
from matplotlib import pyplot as plt
import seaborn as sns


##heat map to show the variable correlation
def heatmap():
	frame=clean_data()
	fig=plt.figure(figsize=(10,10))
	plt.suptitle('heatmap')
	sns.heatmap(frame.corr(),annot=True,vmax=0.3,linewidths=0.5,annot_kws={"size": 10})
	plt.show()
	fig.savefig('heatmap.png')
