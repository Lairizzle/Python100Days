#=================================================
#Name: Dict in a list Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-15
#=================================================

#Challenge, add new country to existing list using a function

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

#print(travelLog[1]["CitiesVisited"][0])

def addNewCountry(country, visits, cities):
    travelLog.append({"Country": country, "CitiesVisited": cities, "TotalVisits": visits})
    print(travelLog)

addNewCountry("Russia", 2, ["Moscow", "Saint Petersburg"])

