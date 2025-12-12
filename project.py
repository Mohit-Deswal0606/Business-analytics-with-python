import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data= pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Tech_Companies.csv")

# print(data.head())
# print(data.tail())
# print(data.columns)
# print(data.describe())
# print(data.isnull().sum())
# print(sns.relplot(x="Revenue_Million", y="Employees", hue="Founded", data=data))
# plt.show()
# sns.pairplot(data)
# plt.show()
# sns.relplot(x='GrowthRate',y='MarketShare',kind='line',data=data)
# plt.show()
sns.catplot(x='Employees',y='RnD_Million',data=data)
plt.show()