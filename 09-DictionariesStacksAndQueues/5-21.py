import json

movies = {
    "twilight": {
        "release_year": 2008,
        "director": "Catherine Hardwicke",
        "budget_$mil": 37,
        "lenght_min": 122
    },
    "If I Stay": {
        "release_year": 2014 ,
        "director": "R. J. Cutler",
        "budget_$mil": 11,
        "lenght_min": 106
    }
}


file_name = "favourite.json"

with open(file_name, 'w') as file:
    json.dump(movies, file, indent=4)
    
print("Data has been written to", file_name)