import pandas as pd                         
import numpy as np                          
import seaborn as sns                       
sns.set(color_codes=True)
df = pd.read_csv("diabetes.csv")
print(df.head(5))
sns.boxplot(x=df['Age'])
