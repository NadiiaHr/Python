# STEP 0
import csv

# Open file
f = open("vaccination.csv")
reader = csv.reader(f)

# Skipping header
next(reader)

# Creating class
class Member: 
    def __init__(self, name, gender, age, state, date):
         self.name = name
         self.gender = gender
         self.age = age
         self.state = state
         self.date = date
            
data = []        
persons = {}  
newList = []

for row in reader:
    name = row[1] + " " + row[2]
    
# Checking if name doesn't exists already
# If there is no name, creating instance of class Member 
    if not name in persons:
        m = Member(name, row[0], int(row[4]), row[3], [int(row[5])])
        persons[name] = m
# If name exists, adding record of date to that name and changing type of it to an intger
    else:
        persons[name].date.append(int(row[5]))
                
f.close()

# Creating and appending each record  to the data
for person in persons:
    data.append(person[name])

# Adding to the newList each formatted element of Data list
"""for i in data:
    i = list(i)
    i.pop(0)
    newList.extend(i)"""

#STEP 1       
print("\nSTEP 1")
print("=======================")
# Counting total vaccinated members 
print(f"There are {len(data)} members with vacinataion records.") 
females = list(filter(lambda x: x.gender == "female", data))
males = list(filter(lambda x: x.gender == "male", data))
print(f"There are {len(females)} females and {len(males)} males.")
print(f"Average age is {sum(list(map(lambda x: x.age, data)))/ len(data)}")

#STEP 2
print("\nSTEP 2")
print("=======================")

count = 0
for i in newList:
    if len(i.date) >= 3:
        count += 1
        print(f"{i.name} with {len(i.date)} doses")
        
print(f"\nThere are {count} members with more than two doses.")  
      
#STEP 3
print("\nSTEP 3")
print("=======================")

info = []
for i in newList:
    if len(i.date) == 2:
        info.append(i.date)      

dif = []            
for i in info:
    calc = abs(i[0] - i[1])
    dif.append(calc)

avrDays = sum(dif)/ len(dif)
print(f"Average days between the first 2 doses are {avrDays} days.")

#STEP 4
print("\nSTEP 4")
print("=======================")
states = set(map(lambda x: x.state, newList))
print(f"\nVaccination records from {len(states)} states.")

# Create function that counts all doses by state
def NumOfDoses(state, doses):
    states = filter(lambda x: x.state == state, doses)
    doses = list(map(lambda x: x.date, states))
    dose = 0
    for d in doses:
        cnt = len(d)
        dose += cnt
    return dose
    
states = set(map(lambda x: x.state, newList))
states = list(map(lambda x: {"state": x, "doses": NumOfDoses(x, newList)}, states))

# Sorting states by doses from high to low and limiting to 5
states = sorted(states, key=lambda x: x["doses"], reverse=True)[:5]

print("Top 5 states")

# Display 5 top states
for i in states:
    print(f"{i['state']} {i['doses']} doses")


#STEP 5
print("\nSTEP 5")
print("=======================")
# Graph with a correlation between number of doses and age 

y = []
x = []
 
# Ppl 20-29 y.o.
y.append(len(list(filter(lambda x: x.age >= 20 and x.age <= 29, newList))))
x.append("20-29")

# Ppl 30-39 y.o.
y.append(len(list(filter(lambda x: x.age >= 30 and x.age <= 39, newList))))
x.append("30-39")

# Ppl 40-49 y.o.
y.append(len(list(filter(lambda x: x.age >= 40 and x.age <= 49, newList))))
x.append("40-49")

# Ppl 50-59 y.o.
y.append(len(list(filter(lambda x: x.age >= 50 and x.age <= 59, newList))))
x.append("50-59")

# Ppl 60-69 y.o.
y.append(len(list(filter(lambda x: x.age >= 60 and x.age <= 69, newList))))
x.append("60-69")

# Ppl 70-79 y.o.
y.append(len(list(filter(lambda x: x.age >= 70 and x.age <= 79, newList))))
x.append("70-79")

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
