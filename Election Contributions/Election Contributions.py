
# Open the file
f = open("contributions.csv")
import csv
reader = csv.reader(f)

# Skip header column
next(reader) 

# Create class
class Contribution: 
    def __init__(self, candidate, name, gender, age, donation):
        self.Candidate = candidate
        self.Name = name
        self.Gender = gender
        self.Age = age
        self.Donation = donation

# Create a list    
data = []

#Skipping if the first row is empty
for row in reader:
    if row[0] == "":
        continue

    if row[3] != 'male':
        row[3] = 'female'
        
# Create an instance of class Contribute                    
    c = Contribution(row[0], row[1] + " " + row[2], row[3], int(row[4]), float(row[5]))
    data.append(c)

f.close()


# Create function Info()
def Info(lst):
    return(f"\tThere are {len(lst)} donations.")
    amount = sum(list(map(lambda x: x.Donation, lst)))
    return(f"\tTotal amount is ${amount}") 
    return(f"\tAverage contribution was ${amount/len(lst)}")

#STEP1
candidates = list(set(map(lambda x: x.Candidate, data)))
print("\nSTEP 1:")
print(f"In this election, {len(candidates)} candidates are running:")
for i in range(len(candidates)):
    print(f"\tCandidate {i+ 1} : {candidates[i]}")       

#STEP2
print("\nSTEP 2:")
# Showing information using Info() func about donations for each candidate
for i in candidates:
    print(f"For candidate {i}:")
    Info(list(filter(lambda x: x.Candidate == i, data))) # is lst

#STEP3
print("\nSTEP 3:")
print("Donations from underage donors:")
# Showing information using Info() func about donation where age under 21
Info(list(filter(lambda x: x.Age < 21, data)))
        
#STEP4
print("\nSTEP 4:")
print("Following donors exceeded amount limit per election:")
donors = set(map(lambda x: x.Name, data))
for donor in donors:
    #List of all donations by donor
    don = list(filter(lambda x: x.Name == donor, data)) 
    #Sum of all donations by donor
    amount = sum(list(map(lambda x: x.Donation, don)))
    if amount > 1600:
        print(f"\t{donor} contributed ${amount}")

#STEP5
print("\nSTEP 5:")
for i in candidates:
    # Showing information for each candidate using Info() func with only female gender
    print(f"Females for candidate {i}:")
    Info(list(filter(lambda x: x.Candidate == i and x.Gender == "female", data)))
    
    # Showing information for each candidate using Info() func with only male gender
    print(f"Males for candidate {i}:")
    Info(list(filter(lambda x: x.Candidate == i and x.Gender == "male", data)))
