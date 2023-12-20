import pandas as pd

csv_list = list(pd.read_csv("location_ids/files.txt").values.flatten())

for csv in csv_list:
    df = pd.read_csv(f"https://www.ncei.noaa.gov/data/local-climatological-data/access/2023/{csv}", chunksize=1, nrows=1)
    print(df)
    break
