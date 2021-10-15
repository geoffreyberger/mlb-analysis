"""MLB Analysis"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from io import StringIO


#importing data
standings2021 = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_standings_2021.csv")
payroll2021 = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_payroll_2021.csv")

standings2020 = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_standings_2020.csv")
payroll2020 = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_payroll_2020.csv")



#creating lists
standings2021.values.tolist()
payroll2021.values.tolist()

standings2020.values.tolist()
payroll2020.values.tolist()

#creating dataframes
standings2021df = pd.DataFrame(standings2021)
payroll2021df = pd.DataFrame(payroll2021)

standings2020df = pd.DataFrame(standings2020)
payroll2020df = pd.DataFrame(payroll2020)

#merge dataframes?
df2021 = pd.merge(standings2021df, payroll2021df, on='Team', how='outer')
display(df2021)

#visualizations
x = payroll2021df['Win Percentage']
y = payroll2021df['2021 Total Payroll']
y = y[::-1]
x = x[::-1]

payroll2021df.plot.scatter(x=x,y=y,c='Blue')

#scatter2021
plt.scatter(x,y)
plt.xlabel("Win Percentage")
plt.ylabel("Total Payroll")
plt.title("2021")
plt.show()

#trendline
x1 = payroll2021df.iloc[:,2]
x1str = str(x1)
y1 = payroll2021df.iloc[:,-1]
y1str = str(y1)

textfile = StringIO(x1, y1)

df = [int(x1),int(y1)]


plot = sbn.lmplot(x='Win Percentage', y='Total Payroll', data=df, ci=None)








