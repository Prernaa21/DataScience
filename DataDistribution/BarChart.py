#Age vs Weight
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.bar(data['Age'],data['Weight'],color='g')
plt.title('Bar chart of Age vs Weight')
plt.xlabel('Age')
plt.ylabel('Weight')
plt.show()

#HP vs Price
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.bar(data['HP'],data['Price'],color='g')
plt.title('Bar chart of HP vs Price')
plt.xlabel('HP')
plt.ylabel('Price')
plt.show()

#Doors vs KM
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.bar(data['Doors'],data['KM'],color='g')
plt.title('Bar chart of Doors vs KM')
plt.xlabel('Doors')
plt.ylabel('KM')
plt.show()

#Automatic vs CC
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.bar(data['Automatic'],data['CC'],color='g')
plt.title('Bar chart of Automatic vs CC')
plt.xlabel('Automatic')
plt.ylabel('CC')
plt.show()
