"""
HouseholdSize.py - This program uses a bubble sort to arrange household sizes
                    in descending order and then prints the mean and median
                    household size.
Input:  Interactive.
Output:  Mean and median household size.
"""

# Initialize variables.
householdSizes = []  # Array used to store household sizes.
numSizes = 0
total = 0.0
mean = 0.0
median = 0.0

# Input household size
householdSizeString = input("Enter household size or 999 to quit: ")
householdSize = int(householdSizeString)
# This is the work done in the fillArray() function
while (householdSize != 999):
    total += householdSize
    # Place value in array.
    householdSizes.append(householdSize)
    # Calculate total of household sizes

    numSizes += 1  # We have one more house
    householdSizeString = input("Enter household size or 999 to quit: ")
    householdSize = int(householdSizeString)

# Find the mean
mean = total / numSizes

# This is the work done in the sortArray() function
for i in range(numSizes):
    for i in range(numSizes-1):
        if householdSizes[i] > householdSizes[i+1]:
            temp = householdSizes[i]
            householdSizes[i] = householdSizes[i+1]
            householdSizes[i+1] = temp

# This is the work done in the displayArray() function
for item in householdSizes:
    print(item)
# Find the median
if numSizes%2 == 0:
    index1 = int(numSizes/2) -1
    index2 = int(numSizes/2)
    median = int((householdSizes[index1]+householdSizes[index2])/2)
if numSizes%2 != 0:
    median = householdSizes[int(numSizes/2)]
print("the mean is: ", mean)
print("The median is: ", median)
