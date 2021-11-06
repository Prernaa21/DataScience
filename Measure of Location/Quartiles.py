import os
import pandas as pd

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)
Q1=data.MonthlyCharges.quantile(0.25)
Q2=data.MonthlyCharges.quantile(0.50)
Q3=data.MonthlyCharges.quantile(0.75)
print(Q1,Q2,Q3)

