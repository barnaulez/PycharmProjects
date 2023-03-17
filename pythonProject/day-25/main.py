import pandas

#data = pandas.read_csv("weather_data.csv")
#print(data)
#temp_list = data["temp"].to_list()
#average = sum(temp_list) / len(temp_list)
#print(f"AVG: {average}")
#print(data[data.temp == data.temp.max()])
#monday = data[data.day == "Monday"]
#monday_temp = int(monday.temp)
#monday_fahr = (monday_temp * 9 / 5) + 32
#print(f"Celsium: {monday_temp}, Fahrenheit: {monday_fahr}")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

