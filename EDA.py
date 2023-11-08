import pandas as pd                         
import numpy as np                          
import seaborn as sns                       
import matplotlib.pyplot as plt             
%matplotlib inline     
sns.set(color_codes=True)
df = pd.read_csv("diabetes.csv")
df.head(5)  