import pandas as pd
import pytz

## Load the POA csv and process it into a pandas dataframe
df_POA = pd.read_csv("POA_irradiance_10Feb23.csv", na_values = r'\N', index_col = 0)
df_POA.dropna(inplace = True)
df_POA.index = pd.to_datetime(df_POA.index)
df_POA.index = df_POA.index.tz_localize(tz = "Etc/GMT-2")
df_POA.head()

## Load the Weather Data csv and process it into a pandas dataframe

df_WT = pd.read_csv("WTdata_corrected_20230508.csv", index_col = 0)
df_WT.index = pd.to_datetime(df_WT.index) 
df_WT.index = df_WT.index.tz_localize(tz = "GMT")
df_WT.index = df_WT.index.tz_convert(tz = "Etc/GMT-2") ## Localize in UTC time and then converted as EET
df_WT.head()

## Rescale data as min mean
df_POA_min = df_POA.resample("1min").mean()
df_POA_H = df_POA_min.resample("H").mean()
df_WT_min = df_WT.resample("min").mean()
df_WT_H = df_WT.resample("H").mean()

## Merge both Weather data and POA together
df_merge = pd.concat([df_POA_min, df_WT_min], axis = 1)
df_merge.dropna(inplace = True) 
df_merge.head()


## Open HP_electrical_cons.csv example

df_HPmeasurement = pd.read_csv("HP_electrical_cons.csv", skiprows = [0,2], sep = ";", decimal = ",")
# drop Nan row value from the Heatpump consumption file and rename the Value column
df_HPmeasurement.dropna(axis = 0, inplace = True, how = "any")
df_HPmeasurement.rename(columns = {"Value": "HP elec cons[kW]"}, inplace = True)
## Pass finnish dateformat into international dateformat to have a datetime index
df_HPmeasurement["Timestamp"] = pd.to_datetime(df_HPmeasurement["Timestamp"], format = "%d.%m.%Y %H:%M", errors = "coerce").fillna(pd.to_datetime(df_HPmeasurement["Timestamp"], format = "%Y-%m-%d %H:%M:%S", errors = "coerce"))
df_HPmeasurement.set_index("Timestamp", inplace = True)
df_HPmeasurement.index = df_HPmeasurement.index.tz_localize(None)
df_HPmeasurement = df_HPmeasurement.resample("H").mean()