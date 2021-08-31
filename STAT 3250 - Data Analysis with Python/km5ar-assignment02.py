##
## File: km5ar-assignment02.py (STAT 3250)
## Topic: Assignment 2
## Nmae: KEYU CHEN - km5ar

## 1.
##
## 1(a) Generate an array x of 10000 random values from 
##      a uniform distribution on the interval [0,50],
##      then use a for loop to determine the percentage     
##      of values that are in the interval [8,27].

## Note: 1(a) asks for a percentage, not a count and not
##       a proportion.

import numpy as np   # improt numpy
x = np.random.uniform(low=0,high=50,size = 10000)  # run it 10000 times
ct = 0          # hold the count
for i in x:     # for loop
    e = np.random.uniform(low=0, high=50)   # mean value of drawn 20 samples from 0-24
    if 27 > e > 8:   # if statement
        ct += 1      # if the condition is meet, ct adds 1
print(ct/10000)      # percentage of values that are in the interval [8,27]

"""
## 1(a)

0.3797  # percentage of values that are in the interval [8,27]
"""

## 1(b) Repeat 1(a) 1000 times, then compute the average
##      of the 1000 percentages found.

import numpy as np 
x = np.random.uniform(low=0,high=50,size = 10000)  # create a array called "x"
ct = 0          # hold the count 
for i in x:     # for loop
    e = np.random.uniform(low=0, high=50)   # mean value of drawn 20 samples from 0-24
    if 27 > e > 8:   # if statement
        ct += 1      # if the condition is meet, ct adds 1
print(ct/10000)  # the average after repeat 1(a)

"""
## 1(b)

0.3787 # percentage of values that are in the interval [8,27] after repeat 1(a) 1000 times
"""


## 1(c) For the array x in 1(a), use a while loop to determine 
##      the number of random entries required to find the
##      first that is less than 3.

i = 0       # this will holds the count
r1 = np.random.uniform(low=0, high=50,size=10000)   # take 10000 random variables from uniform distribution of (0-50)
while r1[i] >= 3:   # set the condition, keep runing untile find the first that is less than 3
    i += 1              #  add i for one if the r1[i] is larger than 3
print(i)            # print out the answer, the number of random enties requried to find the first that is less than 3.


"""
## 1(c)

19   # the number of random entries to find the first that is less than 3
"""

## 1(d) Repeat 1(c) 1000 times, then compute the average for the
##      number of random entries required.

array3 = np.zeros(1000) # create a array to holds 1000 simulation
for i in range(1000):   # for loop 1000 times
    ct = 1    # create the ct, and set it for 1
    s = np.random.choice(x,size=1)   # random choice 1 number
    while s >= 3:        # while loop
        ct = ct+1       # ct + 1 if the number is larger than 3
        s = np.random.choice(x, size =1)   # random choice 1 number
    array3[i] = ct   # add the number of random entries requried to find 3 into the array
np.mean(array3)   # the answer, the mean of the arrays

"""
## 1(d)

16.612  # after repeat 100 times, the number of random entries requried
"""

## 1(e) For the array x in 1(a), use a while loop to determine 
##      the number of random entries required to find the
##      third entry that exceeds 36.

# while loop

x = np.random.uniform(low = 0, high = 50, size = 10000)
c = 0*[0]   # new list for number larger than 36
l = 0*[0]   # new list for number less than 36
i = 0
while len(c) < 3:   # condition: when the number less than 36 are smaller than 3
    if x[i] <= 36:     # if the number is less or equal to 36
        l.append(x[i])  # add it into the "l" array
    else:              # if it larger than 36
        c.append(x[i]) # add it into the "i" array
    i += 1  # every time add 1 to i
print(len(l)+3)  # the answer, the number is less or qual to 36 plus 3 = the number of random entries required to find the third entrey that exceeds 36

"""
## 1(e)

15 # the number of random entries requried to find the third entry that exceeds 36
"""

## 1(f) Repeat 1(e) 5000 times, then compute the average for the
##      number of random entries required.


biglist = [] # new array for 5000 times data
for i in range(5000):
    c = 0*[0]   # new list for number larger than 36
    l = 0*[0]   # new list for number less than 36
    i = 0       # count used in the while loop 
    x = np.random.uniform(low = 0, high = 50, size = 100000)
    while len(c) < 3:   # condition: when the number less than 36 are smaller than 3
        if x[i] <= 36:  
            l.append(x[i])   # add number into the list "l"
        else:
            c.append(x[i])   # add number into the list "c"
        i += 1 # keep the 
    biglist.append(len(l)+3) # add it into the "biglist"
np.mean(biglist)   # get the mean of repeat 5000times for 1(e)

"""
## 1(f)

10.889 # the mean of repeat 5000 times for 1(e)
"""


## 2.   For this problem you will draw samples from a normal
##      population with mean 40 and standard deviation 12.
##      Run the code below to generate your population, which
##      will consist of 1,000,000 elements.

import numpy as np 
p1 = np.random.normal(40,12,size=1000000)

## 2(a) The formula for a 95% confidence interval for the 
##      population mean is given by
##     
##      [xbar - 1.96*sigma/sqrt(n), xbar + 1.96*sigma/sqrt(n)]
##      xbar = sample mean
##      sigma = population standard deviation
##      n = sample size
##
##      where xbar is the sample mean, sigma is the population
##      standard deviation, and n is the sample size.
##
##      Select 10,000 random samples of size 10 from p1.  For
##      each sample, find the corresponding confidence 
##      interval, and then determine the percentage of
##      confidence intervals that contain the population mean.
##      (This is an estimate of the confidence level.)

## 5.20

# sigma = 12
# xbar is the sample size

pop = np.mean(np.random.normal(40,12,size=1000000))  # select 10000 random samples of size 10 from p1
n = 10  # the sample size
ct = 0  # hold the count
sigma = 12   # the true mean of our population
for i in range(10000):
    x = np.random.choice(p1,size=10) #get 10 random sample from random normal distribution
    xbar = np.mean(x)  #sample mean
    lower = xbar - 1.96*sigma/np.sqrt(n) # lower conf. limit
    upper = xbar + 1.96*sigma/np.sqrt(n) # upper conf. limit
    if lower < pop < upper:      # if the confidence intervals contain the population mean
        ct += 1                  # if condition meet, ct adds one
print(ct) # print the count
print(ct/10000) # the percentage of confidence intervals that contain the population mean

"""
## 2(a)

95.06% # the percentage of confidence intervals that contain the population mean
"""



## 2(b) Frequently in applications the population standard
##      deviation is not known. In such cases, the sample
##      standard deviation is used instead.  Repeat part 2(a)
##      replacing the population standard deviation with the
##      standard deviation from each sample, so that the
##      formula is
##
##      [xbar - 1.96*stdev/sqrt(n), xbar + 1.96*stdev/sqrt(n)]
##
##      Tip: Recall the command for the standard deviation is 
##           np.std(data, ddof=1)

#will the sample stand dev be inside of the for loop or outside?

pop = np.mean(np.random.normal(40,12,size=1000000))  # population mean
n = 10  # the sample size
ct = 0  # hold the count
for i in range(10000):
    x = np.random.choice(p1,size=10)   # take 10 samples from a random normal distribution
    xstd = np.std(x) # standard deviation of the random sample
    xbar = np.mean(x) # sample mean
    lower = xbar - 1.96*xstd/np.sqrt(n) # lower conf. limit
    upper = xbar + 1.96*xstd/np.sqrt(n) # upper conf. limit
    if lower < pop < upper: # if the confidence intervals contain the population mean
        ct += 1 # if the condition is meet, ct adds one
print(ct)    # print the ct
print(ct/10000) # the percentage of confidence intervals that contain the population mean(used stdev)

"""
## 2(b)

90.69% # the percentage of confidence intervals that contain the population mean(used stdev)
"""



## 2(c) Your answer in part 2(b) should be a bit off, in that
##      the estimated confidence level isn't quite 95%.  The 
##      problem is that a t-distribution is appropriate when
##      using the sample standard deviation.  Repeat part 2(b),
##      this time using t* in place of 1.96 in the formula,
##      where: t* = 2.262 for n = 10.


n = 10  # the sample size
ct = 0  # hold the count
for i in range(10000):
    x = np.random.choice(p1,size=10) # take 10 samples from a random normal distribution
    xstd = np.std(x) # standard deviation of the random sample
    xbar = np.mean(x) # sample mean
    lower = xbar - 2.262*xstd/np.sqrt(n) # lower conf, limit
    upper = xbar + 2.262*xstd/np.sqrt(n) # upper conf, limit
    if lower < pop < upper: #if the confidence intervals contain the population mean
        ct += 1 # if the condition is meet, ct adds one
print(ct)    # print the count 
print(ct/10000) # the answer, the percentage of confidence intervals that contain the population mean(t*=2.262) 


"""
## 2(c)

94.53%   # the answer, the percentage of confidence intervals that contain the population mean(used t* 2.262)
"""


## 3.   Suppose that random numbers are selected one at a time
##      with replacement from among the set 0, 1, 2, ..., 8, 9.
##      Use 10,000 simulations to estimate the average number 
##      of values required to select three identical values in 
##      a row.
# generate one value at a time
# how much does it take for you to get 3 identical value in a row
# as long as you got 3 identical values in a row you stop and record
# that number
   
list = [0,1,2,3,4,5,6,7,8,9]    # create the set 0,1,2...9
array = []  #hold the count 
for i in range(10000):
    newlist=[] #create a new list inside of the for loop
    ct = 0  # hold the count
    c1 = np.random.choice(list,size =1) #first number
    c2 = np.random.choice(list,size =1) # second number
    c3 = np.random.choice(list,size =1) # 3rd number
    newlist.append(c1) # add first number into the "newlist"
    newlist.append(c2) # add second number into the "newlist"
    newlist.append(c3) # add 3rd number into the "newlist"
    while (newlist[-3] != newlist[-2]) or (newlist[-2] != newlist [-1]): # always compared last 3 number
        ct += 1 # ct add one if three number are not the same number
        c4 = np.random.choice(list,size = 1) # choice next number
        newlist.append(c4) # add the new number into the "newlist"
    array.append(ct+3) # add 3 to ct, then add (ct+3) into the "array"
np.mean(array) # find the mean of the array

"""
## 3

111.4871  # the answer, the average number of values requried to select three identical values in a row after 10000 simulation
"""

## 4.   Jay is taking a 20 question true/false quiz online.  The
##      quiz is configured to tell him whether he gets a question
##      correct before proceeding to the next question.  The  
##      responses influence Jay's confidence level and hence his 
##      exam performance.  In this problem we will use simulation
##      to estimate Jay's average score based on a simple model.
##      We make the following assumptions:
##    
##      * At the start of the quiz there is a 80% chance that 
##        Jay will answer the first question correctly.
##      * For all questions after the first one, if Jay got 
##        the previous question correct, then there is a
##        88% chance that he will get the next question
##        correct.  (And a 12% chance he gets it wrong.)
##      * For all questions after the first one, if Jay got
##        the previous question wrong, then there is a
##        70% chance that he will get the next question
##        correct.  (And a 30% chance he gets it wrong.)
##      * Each question is worth 5 points.
##
##      Use 10,000 simulated quizzes to estimate the average 
##      score.

arrayquiz = np.zeros(10000)   # created a array to hold all the 10,000 simulated quizzes
for w in range (10000):      # for loop for 10,000 simulation
    quizwith20question = 20*[0]   # created a array to hold 20 questions
    quizwith20question[0] = np.random.choice([0,5],size = 1, p = [0.2,0.8]) # first question
    for i in range(19):  # test 2nd-20th questions
        if quizwith20question[i] == 5: # test 2nd-20th questions, if the question get correct
            quizwith20question[i+1] = np.random.choice([0,5], size=1, p=[0.12,0.88]) # the probablilty of get correct is 88%
        else: # test 2nd-20th questions, if the questions get wrong
            quizwith20question[i+1] = np.random.choice([0,5], size=1, p=[0.3,0.7]) # the probablilty of get correct is 70%
    sum(quizwith20question) # sum of grade after take 20 questions
    arrayquiz[w] = sum(quizwith20question) # put the sum of the grade into the array
np.mean(arrayquiz) #mean grade of the 10000 quizes 

"""
## 4

85.0695 # after 10,000 simulated quizzes, the average score is 85.0695
"""

## 5.   The questions in this problem should be done without the 
##      use of loops.  They can be done with NumPy functions.
##      The different parts use the array defined below.

import numpy as np # Load NumPy
arr1 = np.array([[2,5,7,0,2,5,-6,8,1,-9],[-1,3,4,2,0,1,3,2,1,-1],
                [3,0,-2,-2,5,4,5,9,0,7],[1,3,2,0,4,5,1,9,8,6],
                [1,1,0,1,5,3,2,9,0,-9],[0,1,7,7,7,-4,0,2,5,-9]])
print(arr1)
    
## 5(a) Extract a submatrix arr1_slice1 from arr1 that consists of
##      the second and third rows of arr1.


arr1_slice1 = arr1[1:3,]   # extract a subtrix "arr1_slice1" which consists of 2rd and 3rd rows of arr1
print(arr1_slice1)      # print out the "arr1_slice1"
    
"""
## 5(a)

[[-1  3  4  2  0  1  3  2  1 -1]     # 2rd rows of arr1
 [ 3  0 -2 -2  5  4  5  9  0  7]]    # 3rd rows of arr1
"""


## 5(b) Find a one-dimensional array that contains the entries of
##      arr1 that are less than -2.

print(arr1[arr1 < -2])  # print out the answer of one-dimensional array that contains the entries of arr1 that are less than -2
"""
## 5(b)

[-6 -9 -9 -4 -9] # the answer, one-dimensional array that contains the entries of arr1 that are less than -2
"""

## 5(c) Determine the number of entries of arr1 that are greater
##      than 4.

print(np.sum((arr1>4))) # print out the number of values that are greater than 4


"""
## 5(c)

18   # answer, the number of values that are greater than 4
"""

## 5(d) Find the mean of the entries of arr1 that are less than
##      or equal to -2.

print(np.mean(arr1[arr1<=-2])) # print out the number of 

"""
## 5(d)

-5.857142857142857 # answer, the mean of the entries of arr1 that are less than or equal to -2
"""


## 5(e) Find the sum of the squares of the odd entries of arr1.

print(np.sum((arr1[arr1 %2 ==1])**2)) # print the sum of the squares of the odd entries of arr1

"""
## 5(e)

962  # answer, the sum of the squares of the odd entries of arr1.
"""

## 5(f) Determine the proportion of positive entries of arr1 
##      that are greater than 5.
print(np.sum(arr1>5)/np.sum(arr1>0)) # use numbers greater than 5 divided by positive numbers

"""
## 5(f)

0.2619047619047619    # the proportion of positive entries of arr1 that are greater than 5
"""














