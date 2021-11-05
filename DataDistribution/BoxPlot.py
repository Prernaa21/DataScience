#Price vs Automatic
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:/Users/Prerna/Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv")
data.boxplot("Price","Automatic",grid='false',figsize = (5,5), color='blue',fontsize=10 )
plt.show()

#FuelType vs Price
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv")
sns.boxplot(x= data['FuelType'], y=data["Price"])
plt.show()

#Age
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv")
data.boxplot("Age",grid='false',figsize = (5,5),fontsize=10 )
plt.show()

#KM
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv")
data.boxplot("KM",grid='false',figsize = (5,5),fontsize=10 )
plt.show()


#HP
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv")
data.boxplot("HP",grid='false',figsize = (5,5),fontsize=10 )
plt.show()

#MetColor
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv")
data.boxplot("MetColor",grid='false',figsize = (5,5),fontsize=10 )
plt.show()

#CC
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv")
data.boxplot("CC",grid='false',figsize = (5,5),fontsize=10 )
plt.show()

#Weight
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv")
data.boxplot("Weight",grid='false',figsize = (5,5),fontsize=10 )
plt.show()

#Doors
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv")
data.boxplot("Doors",grid='false',figsize = (5,5),fontsize=10 )
plt.show()


