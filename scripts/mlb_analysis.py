"""MLB Analysis"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing data
standings2021 = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_standings_2021.csv")
standings2020 = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_standings_2020.csv")
payroll2021 = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_payroll_2021.csv")
payroll2020 = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_payroll_2020.csv")



#creating lists
standings2021.values.tolist()
standings2020.values.tolist()
payroll2021.values.tolist()
payroll2020.values.tolist()

#creating dataframes
standings2021df = pd.DataFrame(standings2021)
standings2020df = pd.DataFrame(standings2020)
payroll2021df = pd.DataFrame(payroll2021)
payroll2020df = pd.DataFrame(payroll2020)

#merge dataframes?
df2021 = pd.merge(standings2021df, payroll2021df, on='Team', how='outer')
display(df2021)

#visualizations
x = payroll2021['Win Percentage']
y = payroll2021['2021 Total Payroll']
plt.scatter(x,y)