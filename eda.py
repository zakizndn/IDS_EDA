import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("diabetes.csv")

# Display the first 5 rows of the dataframe
st.write("#### Sample of the Data")
st.write(df.head(5))

# Display the boxplot using Streamlit
st.write("#### Box Plot: Age")
box_plot = sns.boxplot(x=df['Age'])
st.pyplot()
