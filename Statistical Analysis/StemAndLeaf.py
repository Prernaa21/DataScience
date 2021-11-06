#a)	Price
import os
import pandas as pd
import stemgraphic

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
stemgraphic.stem_graphic(data['Price'])

#import os
import pandas as pd
import stemgraphic

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
stemgraphic.stem_graphic(data['Age'])

#import os
import pandas as pd
import stemgraphic

os.chdir(r"C:\Users\Prerna\Downloads")
print(os.getcwd())
data = pd.read_csv("Toyota.csv", index_col=0)
stemgraphic.stem_graphic(data['KM'])
