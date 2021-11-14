# Birthdayparadox
# 28 days, Feb
# 30 days, apr, jun, sept, nov
# 31 days, jan, mar, may, jul, aug, oct, dec

import random
import time

def main(): 
    while True: 
        print('How many birthdays shall I generate? (Max 100)')
        choices = input('> ')
        if (0 < int(choices) <=100) and choices.isdecimal():
            randomDates = getrandomDates(choices, masterDates)
            dupes = getDupes(randomDates)
            if len(dupes) == 0:
                print('There are no duplicate birthdays in this simulation')
            else:
                time.sleep(1)
                print('In this simulation, multiple people have a birthday(s) on ' + ', '.join(dupes))
                # .join places list in a string without brackets
                time.sleep(1)
            time.sleep(1)
            print('Generating ' + str(choices) + ' random birthdays 100,000 times...')
            input('Press enter to continue...')
            dupesFound = largeSim(choices, masterDates)
            simP = getPercent(dupesFound)
            print('100,000 simulations run.')
            time.sleep(1)
            print('Out of 100,000 simulations of ' + str(choices) + ' people, there was a\nmatching birthday in that group ' + str(dupesFound) + ' times. this means\nthat ' + str(choices) + ' people have a ' + str(simP) + ''' chance of having a matching\nbirthday in their group. that's probably more than you would think!'''
              )
            break
    

#Generates all the months + date in the year
def generateDates():
    masterDates = []
    for i in range(0, 31):
        masterDates.append('Jan ' + str(i+1))
    for i in range(0, 28):
        masterDates.append('Feb ' + str(i+1))
    for i in range(0, 31):
        masterDates.append('Mar ' + str(i+1))
    for i in range(0, 30):
        masterDates.append('Apr ' + str(i+1))
    for i in range(0, 31):
        masterDates.append('May ' + str(i+1))
    for i in range(0, 30):
        masterDates.append('Jun ' + str(i+1))
    for i in range(0, 31):
        masterDates.append('Jul ' + str(i+1))
    for i in range(0,31):
        masterDates.append('Aug ' + str(i+1))
    for i in range(0, 30):
        masterDates.append('Sep ' + str(i+1))
    for i in range(0, 31):
        masterDates.append('Oct ' + str(i+1))
    for i in range(0, 30):
        masterDates.append('Nov ' + str(i+1))
    for i in range(0, 31):
        masterDates.append('Dec ' + str(i+1))
    return masterDates

masterDates = generateDates()

#Grabs random dates based on inputted choice (how many dates to pull)
def getrandomDates(choices, masterDates):
    choices = int(choices)
    randomDates = random.choices(masterDates, k= choices)
    return randomDates

#Find multiple birthdays

def getDupes(randomDates):
    seen = {}
    dupes = []

    for x in randomDates:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    return dupes

#Run getrandomDates and getDupes 100,000 times, if it has a dupe it's added to dupesFound, if not the for loop continues

def largeSim(choices, masterDates):
    dupesFound = 0
    for i in range(1, 100000):
        randomDates = getrandomDates(choices, masterDates)
        dupes = getDupes(randomDates)
        if len(dupes) == 0:
            continue
        else:
            dupesFound += 1
    return dupesFound

#Gets the percentage of dupes found in 100,000 simulations

def getPercent(dupesFound):
    simP = int(dupesFound)/100000
    simP = simP * 100
    simP = str(simP)
    simP = str(simP[0:5]) + '%'
    return simP
        
if __name__ == '__main__':
    main()
