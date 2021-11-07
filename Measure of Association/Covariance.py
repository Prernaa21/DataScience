import os
import pandas as pd
import numpy as np

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)
cov=np.cov(data.MonthlyCharges.dropna())
print(cov)
