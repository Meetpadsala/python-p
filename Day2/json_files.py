import json


#Write JSON
# data = {
#     "Name": "Meet",
#     "Age": 20
# }


# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)


with open("data.json", "r") as file:
    data = json.load(file)
    print(data["Name"])




