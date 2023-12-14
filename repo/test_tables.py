'''
using df.read_csv from tables from wiki page

@quayles
'''
import pandas

all_df = []

state_df = pandas.read_csv('state_parks.csv', usecols=["Park Name", "Region", "County or Counties", "Status", "Remarks"])
all_df.append(state_df)
rec_df = pandas.read_csv('rec_parks.csv', usecols=["State Recreation Area", "Region", "Counties", "Status", "Remarks"])
all_df.append(rec_df)
nat_df = pandas.read_csv('nat_parks.csv', usecols=["State Natural Area", "Region", "Counties", "Public Access", "Remarks"])
all_df.append(nat_df)
lakes_df = pandas.read_csv('lakes.csv', usecols=["State Lake", "Adjoining State Park", "Counties", "Remarks"])
all_df.append(lakes_df)
rivers_df = pandas.read_csv('rivers.csv', usecols=["State River", "Region", "Remarks"])
all_df.append(rivers_df)
trails_df = pandas.read_csv('trails.csv', usecols=["State Trail", "Region", "Remarks"])
all_df.append(trails_df)

# create lists to hold state parks in coast, coastal plain, piedmont, or mountains
coast_state_parks = [val for val, condition in zip(state_df["Park Name"], state_df["Region"]=="Coast") if condition]
coastal_state_parks = [val for val, condition in zip(state_df["Park Name"], state_df["Region"]=="Coastal Plain") if condition]
piedmont_state_parks = [val for val, condition in zip(state_df["Park Name"], state_df["Region"]=="Piedmont") if condition]
mountain_state_parks = [val for val, condition in zip(state_df["Park Name"], state_df["Region"]=="Mountains") if condition]



user_val = 0

print("PARKS MENU")
print("1. State Parks in Coastal Region")
print("2. State Parks in Coastal Plains Region")
print("3. State Parks in Piedmont Region")
print("4. State Parks in Mountains Region")
print("5. Exit")
user_val = int(input("Please select a region\n> "))

while user_val != 5:
    if user_val == 1:
        for park in coast_state_parks:
            print(park)
    elif user_val == 2:
        for park in coastal_state_parks:
            print(park)
    elif user_val == 3:
        for park in piedmont_state_parks:
            print(park)
    elif user_val == 4:
        for park in mountain_state_parks:
            print(park)
    else:
        print(f"Sorry, {user_val} is not an option. Please try again.")
    
    print("PARKS MENU")
    print("1. State Parks in Coastal Region")
    print("2. State Parks in Coastal Plains Region")
    print("3. State Parks in Piedmont Region")
    print("4. State Parks in Mountains Region")
    print("5. Exit")
    user_val = int(input("Please select a region\n> "))