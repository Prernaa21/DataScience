
#HP
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.hist(data['HP'],color='orange')
plt.title('HP Histogram')
plt.xlabel('HP')
plt.ylabel('Frequency')
plt.show()

#Price
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.hist(data['Price'],color='orange')
plt.title('Price Histogram')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

#Age
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.hist(data['Age'],color='orange')
plt.title('Age Histogram')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#CC
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.hist(data['CC'],color='orange')
plt.title('CC Histogram')
plt.xlabel('CC')
plt.ylabel('Frequency')
plt.show()

#Weight
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
plt.hist(data['Weight'],color='orange')
plt.title('Weight Histogram')
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.show()
