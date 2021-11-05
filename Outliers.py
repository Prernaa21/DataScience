#Price
import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
set=data['Price']
mean = np.mean(set)
sd = np.std(set)
thres = 2
outliers=[]
for i in set:
    z = (i-mean)/sd
    if abs(z) > 2:
        outliers.append(i)
print(outliers)        


#Age
import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
set=data['Age']
mean = np.mean(set)
sd = np.std(set)
thres = 2
outliers=[]
for i in set:
    z = (i-mean)/sd
    if abs(z) > 2:
        outliers.append(i)
print(outliers)        

#KM
import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
set=data['KM']
mean = np.mean(set)
sd = np.std(set)
thres = 2
outliers=[]
for i in set:
    z = (i-mean)/sd
    if abs(z) > 2:
        outliers.append(i)
print(outliers)        

#HP
import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
set=data['HP']
mean = np.mean(set)
sd = np.std(set)
thres = 2
outliers=[]
for i in set:
    z = (i-mean)/sd
    if abs(z) > 2:
        outliers.append(i)
print(outliers)        

#CC
import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
set=data['CC']
mean = np.mean(set)
sd = np.std(set)
thres = 2
outliers=[]
for i in set:
    z = (i-mean)/sd
    if abs(z) > 2:
        outliers.append(i)
print(outliers)        

#Weight
import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
set=data['Weight']
mean = np.mean(set)
sd = np.std(set)
thres = 2
outliers=[]
for i in set:
    z = (i-mean)/sd
    if abs(z) > 2:
        outliers.append(i)
print(outliers)        

#Doors
import os
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
set=data['Doors']
mean = np.mean(set)
sd = np.std(set)
thres = 2
outliers=[]
for i in set:
    z = (i-mean)/sd
    if abs(z) > 2:
        outliers.append(i)


