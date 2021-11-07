import os
import pandas as pd
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)
x=data.MonthlyCharges.dropna()
y=data.TotalCharges.dropna()

correlation=x.corr(y, method='pearson')
print(correlation)

