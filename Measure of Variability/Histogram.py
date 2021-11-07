import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)
sns.histplot(data['MonthlyCharges'], color='red')
plt.title('Histogram')
plt.xlabel('Monthly Charges')
plt.ylabel('Frequency')
plt.show()
