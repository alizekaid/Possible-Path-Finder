def getNeighbours(city,cities):   #This function returns the connected cities of the given city in the given dictionary.
    if city in cities.keys():
        return cities[city]
    return []       
          
starts = []
cities = {}
with open("./city.txt") as f:       #Opens the stated file as f. 
    c = f.read()                    #Reads the contents of the stated file.
    for rLine in c.split("\n"):     #Splits and loops the lines.
        line = rLine.split(":")     
        cities[line[0]] = line[1].split(" ")

with open("./commandsP2.txt") as f:     #This line opens the stated file as f.
    starts = f.readline().split(",")    #Reads the first line of the given file and splits the str's by comma.

result = {}                             
for starting in starts:                 #Works for looping the starting cities that converted to Python list.
    result[starting] = []
    for n in getNeighbours(starting, cities):   #Finds the starting cities in the given dictionary and finds the neighbours of this city. And then loops for each neighbour-cities until the finds out the neighbours of the neighbour.
        result[starting].append(n)
        for m in getNeighbours(n, cities):
            result[starting].append(m)
            for x in getNeighbours(m, cities):
                result[starting].append(x)
    result[starting] = list(set(result[starting]))   #Creates unique list from non-unique list. 
    if result[starting] == []:  #If the given city that started from has no connection with other cities.
        print(f"City '{starting}' has no reachable neighbour")
    else:
        print(f"{starting}:", result[starting])

