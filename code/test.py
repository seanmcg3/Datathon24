import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("/Users/davidvv/Desktop/DATATHON24/Datathon24/datasets/datathon_2024_dataset.csv")
print(data.head())
coords = pd.read_csv("/Users/davidvv/Desktop/DATATHON24/Datathon24/datasets/Major_League_Baseball_Stadiums.csv")
print(coords.head())


home_team_data = data["home_team"].value_counts()
league_counts = coords["LEAGUE"].value_counts()
print(data["home_team"])
plt.pie(league_counts)
plt.show()