flights = []

# Opening the file
file = open("airline_delays.csv")
content = file.read()
file.close()

rows = content.split("\n")

# Skipping the first line
firstRow = True
for row in rows:
    if firstRow:
        firstRow = False
        continue

    values = row.split(",")
    
# Appending values(dictionaries) into flights(list) 
    if values[0] != "" and values[2] != "" and values[4] != "":
        flights.append({"airport": values[0], "delay": float(values[2]), "distance": float(values[4])}) 

airports = {}
for rec in flights:
    name = rec["airport"]
    arrDelays = rec["delay"]
    
    if name in airports:
        airports[name].append(arrDelays)
    else:
        airports[name] = [arrDelays]

# STEP 1

# Getting an input from the user
airport = input("Origin Airport: ")
numFlights = airports[airport]

# Counting delayes for the airport
delayCount = 0
for delay in numFlights:
    if delay > 0:
        delayCount += 1
        
# Counting on time flights for the airport        
onTime = len(numFlights) - delayCount 

print("\nSTEP 1")   
print(f"Total number of flights originated from {airport} airport was {len(numFlights)}." )  
print(f"Flights from {airport} were on time {onTime} times.") 
print(f"Flights from {airport} were delayed {delayCount} times.")   

# Counting the rating for the airport
rating = (len(numFlights) - delayCount) / len(numFlights)
print (f"The perfomance of flights from {airport} is {rating}.")


# STEP 2
print("\nSTEP 2")
best = ""
bestRating = 0
worst = ""
worstRating = 1

for airport in airports:
    numFlights = airports[airport]
    delayCount = 0
    for delay in numFlights:
        if delay > 0:
            delayCount += 1
    rating = (len(numFlights) - delayCount) / len(numFlights) 
    
    print(f"The perfomance of flights from {airport} is {rating}.")

    if rating > bestRating:
        best = airport
        bestRating = rating
        
    if rating < worstRating:
        worst = airport
        worstRating = rating
               
print(f"Best airport {best} with perfomance {bestRating}.")       
print(f"Worst airport {worst} with perfomance {worstRating}.")
      

# STEP 3
print("\nSTEP 3")
data = []

for i in range(7):
    start = i * 400 + 1
    end = i * 400 + 400
    
    totalCount = 0
    oneTimeCount = 0
    for flight in flights:
        if flight["distance"] < start or flight["distance"] > end:
            continue
        
        if flight["delay"] == 0:
            oneTimeCount += 1
        totalCount += 1
       
    rating = oneTimeCount / totalCount
    data.append(rating)
    
import matplotlib.pyplot as plt
plt.plot(data)
plt.show()  

            
            