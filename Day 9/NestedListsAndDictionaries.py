#=================================================
#Name: Nested Lists and Dicts
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-15
#=================================================

#Nesting a list and a dict inside of a dict
nestedDict = {
    "France": {"CitiesVisited": ["Paris", "Lille", "Dijon"], "TotalVisits": 12},
    "Germany": {"CitiesVisited": ["Berlin", "Hamburg", "Stuttgart"], "TotalVisits": 5},
}

#Nesting a list in a list
nestedList = ["A", "B", "C", ["D", "E", "F"]]

#Nesting a dict inside a list
travelLog = [
    {
        "Country": "France", 
        "CitiesVisited": ["Paris", "Lille", "Dijon"], 
        "TotalVisits": 12
    },
    {
        "Country": "Germany", 
        "CitiesVisited": ["Berlin", "Hamburg", "Stuttgart"], 
        "TotalVisits": 12
    },
]

