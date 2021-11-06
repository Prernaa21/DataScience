#Age vs FuelType
import os
import pandas as pd

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
s=pd.crosstab(data.Age, data.FuelType, rownames=('a'), colnames=('b'), dropna=False)
print(s)

#Price vs MetColor
import os
import pandas as pd

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyotaa.csv", index_col=0)
s=pd.crosstab(data.Price, data.MetColor, rownames=('a'), colnames=('b'), dropna=False)
print(s)

#KM vs HP
import os
import pandas as pd

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyotaa.csv", index_col=0)
s=pd.crosstab(data.KM, data.HP, rownames=('a'), colnames=('b'), dropna=False)
print(s)

#Automatic vs CC
import os
import pandas as pd

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyotaa.csv", index_col=0)
s=pd.crosstab(data.Automatic, data.CC, rownames=('a'), colnames=('b'), dropna=False)
print(s)

