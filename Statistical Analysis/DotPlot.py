#Price
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.plot(data['Price'], 'ro')
plt.title('Dot Plot')

#Age
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.plot(data['Age'], 'ro')
plt.title('Dot Plot')


#KM
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.plot(data['KM'], 'ro')
plt.title('Dot Plot')


