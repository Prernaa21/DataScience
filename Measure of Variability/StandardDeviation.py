import os
import pandas as pd

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)
stdev=data.MonthlyCharges.std()
print(stdev)
