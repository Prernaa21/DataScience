import os
import pandas as pd
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
x=data.Age.dropna()
y=data.Price.dropna()

correlation=x.corr(y, method='spearman')
print(correlation)

