#by Josiah Brooks
#01/09/2017
#Profressor Turner


print("Starting a0 - Python: Print, List, Dictionary & Git")
lncount = 0
with open("cities_crosswalk.csv") as f:
    for line in f:
        lncount += 1
        if lncount < 10:
            print(line[0:10])