import os
import pandas as pd

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)
Q1=data.MonthlyCharges.quantile(0.25)
Q3=data.MonthlyCharges.quantile(0.75)
IQR=Q3-Q1
print(IQR)

