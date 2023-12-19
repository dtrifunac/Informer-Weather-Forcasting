import requests
import pandas as pd
import numpy as np
station_code = "72051800449"

dfs = []

for i in range(2013, 2020, 1):
    print(i)
    yeardf = pd.read_csv(f"https://www.ncei.noaa.gov/data/local-climatological-data/access/{str(i)}/{station_code}.csv")
    columns = ["DATE", "HourlyVisibility", "HourlyDryBulbTemperature", "HourlyWetBulbTemperature", "HourlyDewPointTemperature", "HourlyRelativeHumidity", "HourlyWindSpeed", "HourlyWindDirection", "HourlyStationPressure", "HourlyAltimeterSetting"]
    for c in columns:
        yeardf[c] = yeardf[c].replace('', np.nan).replace("*", np.nan)
        # if yeardf[c].dropna().empty:
        #     print(c)
        #     raise BaseException("Empty column")
    yeardf['DATE'] = pd.to_datetime(yeardf['DATE'])
    yeardf['date'] = yeardf['DATE'].dt.strftime('%m/%d/%Y %H:%M')
    yeardf['date'] = pd.to_datetime(yeardf['date'])
    columns[0] = "date"
    yeardf = yeardf[columns]
    yeardf = yeardf.dropna()
    dfs.append(yeardf)

alldata = pd.concat(dfs)



cols = ["HourlyVisibility", "HourlyDryBulbTemperature", "HourlyWetBulbTemperature", "HourlyDewPointTemperature", "HourlyRelativeHumidity", "HourlyWindSpeed", "HourlyWindDirection", "HourlyStationPressure", "HourlyAltimeterSetting"]
alldata[cols] = alldata[cols].apply(pd.to_numeric, errors='coerce')
alldata = alldata.dropna()
print(alldata.dtypes)
alldata.to_csv("weather_data.csv")


