capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in Dictionary

# travel_log = {
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"],
# }

# print Lille

# print(travel_log["France"][1])

nested_lists = ["A","B",["C","D"]]
# print(nested_lists)

#travel_log =
travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited":   ["Paris","Lille","Dijon"]
    },
    "Germany":{
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
print(travel_log["Germany"]["cities_visited"][2])