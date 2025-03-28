#csv training

import pandas


data = pandas.read_csv("central_park.csv")

gray = data[data["Primary Fur Color"] == "Gray"]
black = data[data["Primary Fur Color"] == "Black"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
taple = { "fur color" : ["gray" , "black" , "cinnamon"],
           "count" : [len(gray) , len(black) , len(cinnamon)]
}
print(taple)
output = pandas.DataFrame(taple)
print(output)
output.to_csv("squirrel_count.csv")






