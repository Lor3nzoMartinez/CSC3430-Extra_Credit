import random

# Link to Youtube Video: https://youtu.be/3KLrYxXKwq4
# Initialize Constants for the program.
AMOUNT_OF_HOUSES = 50
AMOUNT_OF_MILES = 100

# Initialize array of houses that will be randomly generated
houses = []
# Initialize array of cell tower intervals that will hold the the area
# of coverage of a given cell tower. [startCoverage, endCoverage]
cellTowerIntervals = []

# I will start by looping through AMOUNT_OF_HOUSES times and adding houses to my
# array randomly between mile 1 and AMOUNT_OF_MILES + 1
for x in range(AMOUNT_OF_HOUSES):
    houses.append(random.randrange(1, AMOUNT_OF_MILES + 1))

# After I will sort the house with the built in sort function that python uses.
houses.sort()

# Initialize the intervals to zero out side of the loop so that can access
# the update version.
startInterval = 0
endInterval = 0

# Next I will loop through the array of houses
for x in range(len(houses)):
    # If my end interval is less then the current houses position
    # then I will create a cell tower 4 miles away from the current house
    # position ensuring that it is covered and then updating the
    # end interval.
    if endInterval < houses[x]:
        startInterval = houses[x]
        endInterval = startInterval + 8
        cellTowerIntervals.append([startInterval, endInterval])

# This is some simple output info to show what has been done.
print("Houses:\n", houses, "\n")
print("Cell Tower Intervals:\n", cellTowerIntervals, "\n")
print("Amount of Cell Towers:\n", len(cellTowerIntervals), "\n")
