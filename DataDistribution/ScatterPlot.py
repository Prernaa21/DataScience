#Age vs Price
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.scatter(data['Age'],data['Price'])
plt.title('Scatter plot of Age vs Price')
plt.show()


#KM vs HP
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.scatter(data['KM'],data['HP'])
plt.title('Scatter plot of KM vs HP')
plt.xlabel('KM')
plt.ylabel('HP')
plt.show()


#CC vs Weight
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.scatter(data['CC'],data['Weight'])
plt.title('Scatter plot of CC vs Weight')
plt.xlabel('CC')
plt.ylabel('Weight')
plt.show()


#FuelType vs HP
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
sns.scatterplot(data['FuelType'],data['HP'])
plt.title('Scatter plot of FuelType vs HP')
plt.xlabel('FuelType')
plt.ylabel('HP')
plt.show()

#MetColor vs Doors
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.scatter(data['MetColor'],data['Doors'])
plt.title('Scatter plot of MetColor vs Doors')
plt.xlabel('MetColor ')
plt.ylabel('Doors')
plt.show()


