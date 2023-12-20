import requests
import pandas as pd
import numpy as np
import sys
# station_code = "72051800449"
station_code = sys.argv[1]

dfs = []

start_year = 2013
end_year = 2020


for i in range(start_year, end_year, 1):
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
alldata.to_csv(f"CustomData/weather_data_{station_code}_{start_year}-{end_year}.csv", index=False)


