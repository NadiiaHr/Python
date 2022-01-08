import pandas as pd

# load the csv file
df = pd.read_csv("nyc_parking_tickets.csv")

# STEP 1
print("Step 1: Reading file...")
# Display the number of records
print(len(df), "records were read from file.")

# STEP 2
print("\nStep 2: Cleaning up...")
#Creating new dataframe wich cleaned data
dfCleaned = df[( (df["Registration_State"] != "99") & (df["Plate_Type"] != "999")
    & (df["Vehicle_Make"] != "") & (df["Vehicle_Year"] != 0)
    & (df["Issuer_Code"] != 0) & (df["Vehicle_Year"] < 2018))];

print(len(dfCleaned), "records left after cleaning.")

# STEP 3
print("\nStep 3: # of tickets by vehicle year...")
#unique years
distYears = sorted(dfCleaned["Vehicle_Year"].unique())
num_tickets = []
#Counting tickets for each vechicle year
for year in distYears:
    num_tickets.append(dfCleaned[dfCleaned["Vehicle_Year"] == year]["Issuer_Code"].count())

#Displaying graph with Vehicle Year and number of tickets
import matplotlib.pyplot as plt  
plt.plot(distYears, num_tickets)
plt.show() 
    
# STEP 4
print("\nStep 4: Top 5 vehicle-makes with most tickets...")
vehTypeTic = (dfCleaned.groupby("Vehicle_Make")["Plate_ID"].count()).nlargest(5)
print(vehTypeTic)


# STEP 5
print("\nStep 5: The street where commercial vehicles got the most tickets:")
#Commercial vehicles
comVeh = dfCleaned[dfCleaned.Plate_Type == "COM"]
StrMostTickets = (comVeh.groupby("Street_Name")["Plate_ID"].count()).nlargest(1)
print(StrMostTickets)

# STEP 6.1
print("\nStep 6.1: The state with newest vehicles:")
stateVeh = dfCleaned[["Registration_State", "Vehicle_Year"]]
statenewVeh = stateVeh.groupby(["Registration_State"]).mean().sort_values("Vehicle_Year", ascending=False).head(1)
print(statenewVeh)

# STEP 6.2
print("\nStep 6.2: The state with oldest vehicles:")
stateoldVeh = stateVeh.groupby(["Registration_State"]).mean().sort_values("Vehicle_Year", ascending=True).head(1)
print(stateoldVeh)
