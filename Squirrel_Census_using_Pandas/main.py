import pandas

data = pandas.read_csv("./Squirrel_Census_using_Pandas/Squirrel_data.csv")

Gray_Squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

Black_Squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

Cinnamon_Squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(Gray_Squirrel_count)

Squirrel_dict = {
    "Color of Squirrel": ["Gray", "Black", "Cinnamon"],
    "Squirrel Count": [
        Gray_Squirrel_count,
        Black_Squirrel_count,
        Cinnamon_Squirrel_count,
    ],
}

df = pandas.DataFrame(Squirrel_dict)

df.to_csv("./Squirrel_Census_using_Pandas/Squirrel_data_count.csv")
