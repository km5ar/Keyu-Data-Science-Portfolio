##
## File: km5ar-assignment01.py (STAT 3250)
## Topic: Assignment 1
## Name: Keyu Chen - km5ar

## 1.  For the questions in this part, use the following
##     lists as needed:
list01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
list02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1,0,5]
list03 = [2,-5,6,7,-2,-3,0,3,0,2,8,7,9,2,0,-2,5,5,6]
biglist = list01 + list02 + list03

## (a) Find the product of the last four elements of list02.

l1 = list02[-1] # to get last one element
l2 = list02[-2] # second from last
l3 = list02[-3] # third from last
l4 = list02[-4] # Fourth last

lastfour = l1*l2*l3*l4 # the product of the last four elements
print(lastfour) # print the answer out


"""
## 1 (a)

0        # The output of the product of the last four
"""

## (b) Extract the sublist of list01 that goes from
##     the 3rd to the 11th elements (inclusive).

list01[2:11] # extract 3rd to 11th elements(inclusive)

"""
## 1(a)

[4, 9, 10, -3, 5, 5, 3, -8, 0]      # the sublist of list01 that goes from the 3rd to the 11th elements(inclusive)
"""



## (c) Concatenate list01 and list03 (in that order), sort
##     the combined list, then extract the sublist that 
##     goes from the 5th to the 15th elements (inclusive).

list13 = list01 + list03   # Concatenate list01 and list03 and rename it as "list13" 
print(list13)         # print out the "list13"
list13.sort()         # sort the combined list "list13"
list13[4:15]          # sublist that goes from the 5th to the 15th


"""
## 1(c)
[2, 5, 4, 9, 10, -3, 5, 5, 3, -8, 0, 2, 3, 8, 8, -2, -4, 0, 6, 2, -5, 6, 7, -2, -3, 0, 3, 0, 2, 8, 7, 9, 2, 0, -2, 5, 5, 6] # the output of concatenate list01 and list 03(in that order)

[-3, -2, -2, -2, 0, 0, 0, 0, 0, 2, 2]  # the sublist from 5th to 15th
"""


## (d) Generate "biglist", then extract the sublist of every 4th 
##     element starting with the 3rd element

print(biglist)             #print out the biglist
print(biglist[2::4])       #print out the sublist of every 4th lelment starting with the 3rd element

"""
## 1(d)
[2, 5, 4, 9, 10, -3, 5, 5, 3, -8, 0, 2, 3, 8, 8, -2, -4, 0, 6, -7, -3, 8, -5, -5, -2, 4, 6, 7, 5, 9, 10, 2, 13, -12, -4, 1, 0, 5, 2, -5, 6, 7, -2, -3, 0, 3, 0, 2, 8, 7, 9, 2, 0, -2, 5, 5, 6] # the output of "biglist"

[4, 5, 0, 8, 6, -5, 6, 10, -4, 2, -2, 0, 9, 5]  # sublist of every 4th element starting with the 3rd element
"""


## 2.  Use for loops to do each of the following with the lists
##     defined above.
 
## (a) Add up the squares of the entries of biglist.

s = 0  # This will hold the sum of the squares of the entries
for p in biglist:       # Initiates the loop; 
    p1 = p**2           # the squares of the eatch entries of biglist
    s = s + p1    # Adds the current prime value to the sum
print(s)            # print out the sum of the squares of the entries of biglist

"""
## 2(a)

1825      # The output of the sum of the squares of the entries of the biglist
"""

## (b) Create "newlist01", which has 19 entries, each the 
##     sum of the corresponding entry from list01 added 
##     to the corresponding entry from list02.  That is,
##     
##         newlist01[i] = list01[i] + list02[i] 
##
##     for each 0 <= i <= 18.

newlist01 = 19*[0]                         # Creates a list with 19 0's.
for i in range(19):                        # Compute each entry
    newlist01[i] = list01[i] + list02[i]   # sum of corresponding entry and put it in newlist01
print(newlist01)                       # print newlist01 out

"""
## 2(b)

[-5, 2, 12, 4, 5, -5, 9, 11, 10, -3, 9, 12, 5, 21, -4, -6, -3, 0, 11]   # the output of the "newlist01"
"""


## (c) Compute the mean of the entries of biglist.
##     (Hint: len(biglist) gives the number
##     of entries in biglist.  This is potentially useful.)

# len(biglist)
# import numpy as np
# np.mean(biglist) 

for i in biglist:
    t = sum(biglist)        # sum of the biglist
    mean = t/len(biglist)   # mean of the biglist
print(mean)                 # print out the mean of the biglist

"""
## 2(c)

2.3684210526315788    # the mean of the entries of biglist
"""


## (d) Determine the number of entries in biglist that
##     are less than 6.

ct = 0
for xval in biglist:    #create the for loop for biglist
    if xval < 6:  # to find entries that are less than 6
        ct += 1  # Adds 1 to ct; same as ct = ct + 1
print(ct)  # print out the number of entries in biglist that are less than 6


"""
## 2(d)

40     # The number of entries in biglist that are less than 6
"""

## (e) Determine the number of entries in biglist that
##     are between -2 and 4 (inclusive).

ct = 0                   # This will hold the count   
for xval in biglist:
    if -2 <= xval and xval <= 4: # if statement to find the number between -2 and 4
        ct += 1  # Adds 1 to ct; same as ct = ct + 1
print(ct)       # print out the number of entries in biglist that are between -2 and 4

"""
## 2(e)

22     # The number of entries in biglist that are between -2 and 4(inclusive)
"""


## (f) Create a new list called "newlist02" that contains 
##     the elements of biglist that are greater than 0.

newlist02 = 0*[0]       # create a new list called "newlist02"
for i in biglist:   
    if i > 0:           # if statement to find the elements which larger then 0
        newlist02.append(i) # add the element which larger than 0 into the "newlist02"
print(newlist02)        # print out the "newlist02"

"""
## 2(f)

[2, 5, 4, 9, 10, 5, 5, 3, 2, 3, 8, 8, 6, 8, 4, 6, 7, 5, 9, 10, 2, 13, 1, 5, 2, 6, 7, 3, 2, 8, 7, 9, 2, 5, 5, 6]
# The output of the "newlist02" that contains the elements of biglist that are greater than 0.
"""


## 3.  In this problem you will be simulating confidence intervals
##     for samples drawn from a uniform distribution on [0,24], 
##     which has a mean of 12.
##     For instance, a sample of size 10 can be drawn with the 
##     commands
import numpy as np # "as np" lets us use "np"; only run once
samp = np.random.uniform(low=0,high=24,size=10)  # demostration purpose

## (a) Use random samples of size 20 and simulation to generate 
##     500,000 confidence intervals of the form
##     
##                           xbar +- 2
## 
##     Use your confidence intervals to estimate the confidence
#      level. (Give the level as a percentage.)
## what porporsion include the number 12 ##
## if I make 500,000 times, what percentage of time 

ct = 0              # This will hold the count        
for i in range(500000):
    xbar = np.mean(np.random.uniform(low=0, high=24,size=20))   # mean value of drawn 20 samples from 0-24
    if xbar+2 > 12 >xbar-2:
        ct += 1
print(ct)
print(ct/500000)

"""
## 3(a)

400969       # the number of simulation that fall into the confidence intervals xbar +-2.
0.801938     # after I make 500,000 simulation, 80.19% of the time it will be fall into the xbar +-2.
"""

## (b) Repeat (a) with confidence intervals xbar +- 3

ct = 0                      # This will hold the count
for i in range(500000):                 #create the for loop
    xbar = np.mean(np.random.uniform(low=0, high=24,size=20))   # mean value of drawn 20 sample from 0 - 24
    if xbar+3 > 12 >xbar-3:             # Test if 12 fall into the interval
        ct += 1          # if 12 fall into the interval, add 1 to ct
print(ct)                # print the number of ct which fall into the interval
print(ct/500000)         # print the percentage of ct which fall into the interval when I make 500,000 times simulation


"""
## 3(b)

474059    #the number of simulation that fall into the confidence intervals xbar +-3
0.948118  #after I make 500,000 simulation, 94.8% of the time it will be fall into the confidence intervals xbar +-3
"""

## (c) Repeat (a) with samples of size 30.
## c should have a higher than a ##


ct = 0             # This will hold the count
for i in range(500000):       # create the for loop
    xbar = np.mean(np.random.uniform(low=0, high=24,size=30))   # mean value of random drawn 30 sample from 0 - 24
    if xbar+2 > 12 >xbar-2:      # Test if 12 fall into the interval
        ct += 1        # if 12 fall into the interval, add 1 to ct
print(ct)              # print the number of ct which fall into the interval
print(ct/500000)       # print the percentage of ct which fall into the interval, when I make 500,000 times simulation

"""
## 3(c)
442848    #the number of simulation that fall into the confidence intervals.
0.885696  #after I make 500,000 simulation, 88.56% of the time it will be fall into the confidence intervals.
"""


## (d) Repeat (b) with samples of size 30.

ct = 0                 # This will hold the count
for i in range(500000):   # create the for loop
    xbar = np.mean(np.random.uniform(low=0, high=24,size=30))   # mean value of drawn 30 random sample from 0 - 24
    if xbar+3 > 12 >xbar-3:         # Test if 12 fall into the interval
        ct += 1        # if 12 fall into the interval, add 1 to ct
print(ct)              # print the number of ct which fall into the interval
print(ct/500000)       # print the percentage of ct which fall into the interval, when I make 500,000 times simulation

"""
## 3(d)

491324    #the number of simulation that fall into the confidence intervals.
0.982648  #after I make 500,000 simulation, 88.56% of the time it will be fall into the confidence intervals.
"""


## 4.  Here we repeat parts (a)-(d) of #3, but this time using
##     samples from an exponential distribution with mean 12.
##     The code below will produce a sample of size 10 with 
##     mean = 12:


# 4a 

ct = 0                # This will hold the count
for i in range(500000):   # create the for loop
    xbar = np.mean(np.random.exponential(scale=12,size=20))  # mean value of exponential distribution of the size of 20
    if xbar+2 > 12 >xbar-2:      # Test if 12 fall into the interval
        ct += 1       # if 12 fall into the interval, add 1 to ct
print(ct)             # print the number of ct which fall into the interval
print(ct/500000)      # print the percentage of ct which fall into the interval, when I make 500,000 times simulation

"""
## 4a
271621   #the number of simulation that fall into the confidence intervals.
0.543242  #after I make 500,000 simulation, 54.32% of the time it will be fall into the confidence intervals.
"""


# 4b
ct = 0          # This will hold the count      
for i in range(500000):      # create the for loop
    xbar = np.mean(np.random.exponential(scale=12,size=20))    # mean value of exponential distribution of the size of 20
    if xbar+3 > 12 >xbar-3:     # Test if 12 fall into the interval
        ct += 1          # if 12 fall into the interval, add 1 to ct
print(ct)                # print the number of ct which fall into the interval
print(ct/500000)         # print the percentage of ct which fall into the interval, when I make 500,000 times simulation


"""
## 4b
371291   #the number of simulation that fall into the confidence intervals.
0.742582  #after I make 500,000 simulation, 94.78% of the time it will be fall into the confidence intervals.
"""



# 4c

ct = 0      # This will hold the count
for i in range(500000):      # create the for loop
    xbar = np.mean(np.random.exponential(scale=12,size=30))   # mean value of exponential distribution of the size of 30
    if xbar+2 > 12 >xbar-2:   # Test if 12 fall into the interval
        ct += 1        # if 12 fall into the interval, add 1 to ct
print(ct)        # print the number of ct which fall into the interval
print(ct/500000)  # print the percentage of ct which fall into the interval, when I make 500,000 times simulation

"""
## 4c
320490   #the number of simulation that fall into the confidence intervals.
0.64098  #after I make 500,000 simulation, 64.098% of the time it will be fall into the confidence intervals.
"""


# 4d

ct = 0            # This will hold the count
for i in range(500000):            # create the for loop
    xbar = np.mean(np.random.exponential(scale=12,size=30))   # mean value of exponential distribution of the size of 30
    if xbar+3 > 12 >xbar-3:        # Test if 12 fall into the interval
        ct += 1                    # if 12 fall into the interval, add 1 to ct
print(ct)                          # print the number of ct which fall into the interval
print(ct/500000)                   # print the percentage of ct which fall into the interval, when I make 500,000 times simulation

"""
## 4d
416692    #the number of simulation that fall into the confidence intervals.
0.833384  #after I make 500,000 simulation, 83.34% of the time it will be fall into the confidence intervals.
"""
