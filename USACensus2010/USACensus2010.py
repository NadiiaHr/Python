# Step 0
# Create class County
class County:
    name = ""
    state = ""
    commute = 0
    home = 0
    income = 0
    pop = 0
    edu = 0   

    # Method to find similar states
    def similarTo(self, y):
        return sim(self.pop, y.pop) and sim(self.edu, y.edu) and sim(self.home, y.home) and sim(self.income, y.income) and sim(self.commute, y.commute) 

    # Method to find the same states
    def sameAs(self, y):
        return self.name == y.name and self.state == y.state

    #Method to find abrevation of the state
    def label(self):
        return self.name + " (" + self.state + ")"
    
    #Method to find happiness
    def happiness(self):
        return (self.income * self.home) / self.commute

def sim(x, y):
        return abs(x / y - 1)< 0.02  
    
data = []

# Open the file
f = open("county_facts.csv") 
import csv
rows = csv.reader(f) 

#Skipping column header
next(rows)

for cols in rows:
    if cols[2]== "":
        continue

    c = County()
    c.name = cols[1]
    c.state = cols[2]
    c.pop = float(cols[6])
    c.edu = float(cols[23])
    c.income = float(cols[33])
    c.home = float(cols[27])
    c.commute = float(cols[25])
    
    data.append(c)

f.close()   

# Step 1
# County with the most population
maxCon = max(data, key = lambda x: x.pop)

# County with the least population
minCon = min(data, key = lambda x: x.pop)
print("\nQ1: Counties with least and most population")
print("===========================================")
print(f"{minCon.name} ({minCon.state}): {minCon.pop}")
print(f"{maxCon.name} ({maxCon.state}): {maxCon.pop}")

print(type(data)) 
# Step 2 
print("\nQ2: States with least and most population")
print("=========================================")
def statePop(state, counties):
    stateCounties = filter(lambda x: x.state == state, counties)
    pops = list(map(lambda x: x.pop, stateCounties))
    output = sum(pops)
    return output
     
states = set(map(lambda x: x.state, data))
states = list(map(lambda x: {"State": x, "population": statePop(x, data)}, states))

# State with the least population
print(min(states, key=lambda x: x["population"]))

# State with the most population
print(max(states, key=lambda x: x["population"]))    
   
     
# Step 3 
print("\nQ3: Hapiness vs Higher Education Rate")
print("======================================")
def average(lst):
    lst = list(lst)
    return sum(lst)/ len(lst)

happyRate = map(lambda x: x.happiness(), data)
# Avearge of the Happy Rate
avg = average(happyRate)

# Happy Counties College Edu Rate
happyCount = filter(lambda x: x.happiness() >= avg, data)
avgEduHappy = average(map(lambda x: x.edu, happyCount))
print(f"Happy Counties College Edu Rate: {avgEduHappy}%")

# Unhappy Counties College Edu Rate
otherCount = filter(lambda x: x.happiness() < avg, data)
avgEduOther = average(map(lambda x: x.edu, otherCount))
print(f"Unhappy Counties College Edu Rate: {avgEduOther}%")

# Difference between Happy and Unhappy Counties College Edu Rate
differ = avgEduHappy - avgEduOther
print(f"Difference is {differ}%")
if differ > 20:
    print("Happy counties have significantly more college graduates.")
elif differ > 5:
    print ("Happy counties have slightly more college graduates.")
elif differ > -20:
    print("Happy counties have significantly less college graduates.")
elif differ > -5:
    print ("Happy counties have slightly less college graduates.")
else:
    print("Could not find any significant correlation.")    
    
    
# Step 4 
print("\nQ4: Similar Counties (2%)")
print("=========================")

similAll = set()

for c in data:
    # Remove counties from data
    selfrem = filter(lambda x: not x.sameAs(c), data)

    # Similiar states in terms of pop and edu
    similar = list(filter(lambda x: x.similarTo(c), selfrem))

    for simC in similar:
        if c.pop > simC.pop:
            similAll.add(simC.label() + " and " + c.label() + " are similar.")
        else:
            similAll.add(c.label() + " and " + simC.label() + " are similar.")

# Displaying similiar countries
for i in  similAll:
    print(i)

# Step 5 
print("\nQ5: Population vs Income Rate")
print("=============================")

# Graph with a correlation between population and income 
y = []
x = []

space = (maxCon.pop - minCon.pop) / 3
for i in range(3):
    r1 = minCon.pop + space * i
    r2 = r1 + space
    fData = filter(lambda x: r1 <= x.pop <= r2, data)
    incomes = map(lambda x: x.income, fData)
    x.append(str(r1) + "-" + str(r2))
    y.append(average(incomes))
    
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()    
