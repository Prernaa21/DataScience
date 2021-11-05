#Doors vs CC
import os
import pandas as pd
from matplotlib.pyplot import pie, axis, show

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
sums = data.groupby(data["Doors"])["CC"].sum()
axis('equal')
pie(sums, labels=sums.index)
show()

#FuelType vs Price
import os
import pandas as pd
from matplotlib.pyplot import pie, axis, show

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
sums = data.groupby(data["FuelType"])["Price"].sum()
axis('equal')
pie(sums, labels=sums.index)
show()

#MetColor vs KM
import os
import pandas as pd
from matplotlib.pyplot import pie, axis, show

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
sums = data.groupby(data["MetColor"])["KM"].sum()
axis('equal')
pie(sums, labels=sums.index)
show()

#Automatic vs HP
import os
import pandas as pd
from matplotlib.pyplot import pie, axis, show

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)                   
sums = data.groupby(data["Automatic"])["HP"].sum()
axis('equal')
pie(sums, labels=sums.index)
show()

#



