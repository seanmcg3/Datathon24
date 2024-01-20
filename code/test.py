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

def filter_by_year(csv, start_date, end_date):
    filtered_df = csv[(csv['game_date'] >= int(start_date)) & (csv['game_date'] <= int(end_date))]
    return filtered_df

year2000 = filter_by_year(data, 20000000, 20010000)
year2001 = filter_by_year(data, 20010000, 20020000)
year2002 = filter_by_year(data, 20020000, 20030000)
year2003 = filter_by_year(data, 20030000, 20040000)
year2004 = filter_by_year(data, 20040000, 20050000)
year2005 = filter_by_year(data, 20050000, 20060000)
year2006 = filter_by_year(data, 20060000, 20070000)
year2007 = filter_by_year(data, 20070000, 20080000)
year2008 = filter_by_year(data, 20080000, 20090000)
year2009 = filter_by_year(data, 20090000, 20100000)
year2010 = filter_by_year(data, 20100000, 20110000)
year2011 = filter_by_year(data, 20110000, 20120000)
year2012 = filter_by_year(data, 20120000, 20130000)
year2013 = filter_by_year(data, 20130000, 20140000)
year2014 = filter_by_year(data, 20140000, 20150000)
year2015 = filter_by_year(data, 20150000, 20160000)
year2016 = filter_by_year(data, 20160000, 20170000)
year2017 = filter_by_year(data, 20170000, 20180000)
year2018 = filter_by_year(data, 20180000, 20190000)
year2019 = filter_by_year(data, 20190000, 20200000)
year2020 = filter_by_year(data, 20200000, 20210000)
year2021 = filter_by_year(data, 20210000, 20220000)
year2022 = filter_by_year(data, 20220000, 20230000)
year2023 = filter_by_year(data, 20230000, 20240000)
