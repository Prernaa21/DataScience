#Senior Citizen vs Partner
import pandas as pd
from scipy.stats import chi2_contingency
import os

os.chdir(r"C:\Users\Admin\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)

db= pd.crosstab(data.SeniorCitizen, data.Partner)
print(db)
c, pvalue, dof, expected = chi2_contingency(db)
alpha = 0.05
if pvalue < alpha:
    print("Reject H0")
else:
    print("H0 holds True")    
print(c)    
print(pvalue)
print(dof)
print(expected)


#Monthly Charges vs Total Charges
import pandas as pd
from scipy.stats import chi2_contingency
import os

os.chdir(r"C:\Users\Admin\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)

db= pd.crosstab(data.MonthlyCharges, data.TotalCharges)
print(db)
c, pvalue, dof, expected = chi2_contingency(db)
alpha = 0.05
if pvalue < alpha:
    print("Reject H0")
else:
    print("H0 holds True")    
print(c)    
print(pvalue)
print(dof)
print(expected)

#Contract vs PaperlessBilling
import pandas as pd
from scipy.stats import chi2_contingency
import os

os.chdir(r"C:\Users\Admin\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)

db= pd.crosstab(data.Contract, data.PaperlessBilling)
print(db)
c, pvalue, dof, expected = chi2_contingency(db)
alpha = 0.05
if pvalue < alpha:
    print("Reject H0")
else:
    print("H0 holds True")    
print(c)    
print(pvalue)
print(dof)
print(expected)

#Payment Methods vs Dependents
import pandas as pd
from scipy.stats import chi2_contingency
import os

os.chdir(r"C:\Users\Admin\Downloads")
print(os.getcwd())
data = pd.read_csv("churn.csv", index_col=0)

db= pd.crosstab(data.PaymentMethod, data.Dependents)
print(db)
c, pvalue, dof, expected = chi2_contingency(db)
alpha = 0.05
if pvalue < alpha:
    print("Reject H0")
else:
    print("H0 holds True")    
print(c)    
print(pvalue)
print(dof)
print(expected)
