"""MLB Analysis"""

import pandas as pd
import numpy as np
import matplotlib as plt


#importing data
2021_standings = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_standings_2021")
2020_standings = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_standings_2020")
2021_payroll = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_payroll_2021")
2020_payroll = pd.read_csv("/Users/geoffrey/Desktop/mlbdata_payroll_2020")

#creating lists
2021_standings.values.tolist()
2021_standings.values.tolist()
2021_payroll.values.tolist()
2020_payroll.values.tolist()

#creating dataframes
2021_standings_df = pd.DataFrame(2021_standings)
2020_standings_df = pd.DataFrame(2020_standings)
2021_payroll_df = pd.DataFrame(2021_payroll)
2020_payroll_df = pd.DataFrame(2020_payroll)

