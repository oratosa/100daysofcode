import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# data_list = data["temp"].to_list()
# avg_temperature = sum(data_list) / len(data_list)

# print(avg_temperature)
# max_temperature = data["temp"].max()
# print(max_temperature)
# print(data[data["temp"] == max_temperature])

df_groupby = df.groupby(by=df["Primary Fur Color"], as_index=False).count()
df_output = df_groupby[["Primary Fur Color", "X"]].rename(
    columns={"Primary Fur Color": "Fur Color", "X": "Count"}
)

df_output.to_csv("squirrel_count.csv")
