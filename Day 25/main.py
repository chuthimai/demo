import pandas as pd

# data = pd.read_csv("weather_data.csv")
# temp_list = data.temp.to_list()
# max = data["temp"].max()
#
# print(data[data.temp == max])

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data["Primary Fur Color"].unique()
colors = colors.tolist()
count = []

for i in colors:
    count.append(0)
for color in data["Primary Fur Color"]:
    if color in colors:
        count[colors.index(color)] += 1

new_data = {"Fur Color": colors[1::], "Count": count[1::]}
export = pd.DataFrame(new_data)
export.to_csv("New_data.csv")
