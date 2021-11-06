#Frequency Distribution
import os
import pandas as pd

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
d1=data['Price'].value_counts()
print(d1)

#Relative Frequency
import os
import pandas as pd
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
d1=data['Price'].value_counts()
d2=data['Price']
print(d1 / len(d2))

#Cumulative Frequency
import os
import pandas as pd
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
d1=data['Price'].value_counts()
c1=d1['Cumulative Frequency'] = d1.cumsum()
print(c1)
