
from sklearn import datasets 

import numpy as np 

import matplotlib.pyplot as plt 
import pandas as pd 


iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits.data) 
digits.target
