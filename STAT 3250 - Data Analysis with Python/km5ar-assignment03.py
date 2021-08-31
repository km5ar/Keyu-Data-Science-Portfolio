##
## File: km5ar-assignment03.py (STAT 3250)
## Topic: Assignment 3
## Name: keyu chen - km5ar
##

##  The questions in this assignment refer to the data in the
##  file 'absent.csv'.  The data contains 740 records from an
##  employer, with 21 columns of data for each record.  (There
##  are a few missing values indicated by zeros where zeros 
##  are clearly not appropriate.)  The file 'absent.pdf' has
##  a summary of the meanings for the variables.

##  Questions 1 and 2 can be completed without loops.  You should
##  try to do them this way, grading will take this into account.

## 1.  All questions refer to the data set 'absent.csv'.

## 1(a) Find the mean absent time among all records.

import numpy as np    # import numpy
import pandas as pd   # import pands
records = pd.read_csv('absent.csv')   # improt the data set 'absent.csv' and name it "records"
np.mean(records)['Absenteeism time in hours']   # mean absent time among all records

"""
1a.

6.924324324324324   # the answer, the mean absent time among all records
"""
## 1(b) Determine the number of records corresponding to
##      being absent on a Thursday.

abThursday = records.loc[records['Day of the week'] == 5,:]   # get the information of people who being absent on a Thursday
len(abThursday) # find the lenth of the records, which is the number of records corresponding to being absent on a Thursday

"""
1b.

125   # the answer, the number of records corresponding to being absent on a Thursday
"""
## 1(c) Find the number of different employees represented in 
##      this data.

diffemployees = np.unique(records['ID'])   # find the unique number in data set "records"'s column 'ID'
len(diffemployees) # then find the lenth of the list

"""
1c.

36  # answer, the number of different employees represented in this data set.
"""
## 1(d) Find the transportation expense for the employee with
##      ID = 34.

# column 'Transportation expense' with ID = 34

idTransportation = records[['ID','Transportation expense']]      # the data set with ID and Transportation expense
transportation34 = idTransportation.loc[idTransportation['ID'] == 34,:]  # transporation expense with ID '34'
print(transportation34)  #print out the transportation expense for the emplyee with ID = 34


"""
1d.

118    # the answer, the transportation expense for ID = '34'
"""
## 1(e) Find the mean number of hours absent for the records
##      for employee ID = 11.

idAbsent = records[['ID','Absenteeism time in hours']]  # the data set with 'ID' and 'Absenteeism time in hours'
absent11 = idAbsent.loc[idAbsent['ID']== 11,:]   # data with ID = 11
np.mean(absent11['Absenteeism time in hours'])   # the mean number of hours absent for the records for employee ID = 11



"""
1e.

11.25   # the answer, the mean number of hours absent for the records for employee ID = 11
"""
## 1(f) Find the mean number of hours absent for the records of those who 
##      have no pets, then do the same for those who have more than one pet.

## mean number of hours absent for the records of those who have no pets
petAbsent = records[['Pet','Absenteeism time in hours']]   # data set with 'Pet' and 'Absenteeism in hours'
noPetAbsent = petAbsent.loc[petAbsent['Pet']== 0,:]    # data with people who have no pets
np.mean(noPetAbsent['Absenteeism time in hours'])     # the mean number of hours absetn for the records of those who have no pets

## mean number of hours absent for the records of those who have more than one pet
MoreThan1PetAbsent = petAbsent.loc[petAbsent['Pet'] > 1,:] # data with people who have more than one pet
np.mean(MoreThan1PetAbsent['Absenteeism time in hours'])   # mean number of hours absent for the records of those who have more than one pet

"""
1f.

6.828260869565217    # the answer, the mean number of hours for the records of those who have no pets

5.21830985915493     # the answer, the mean number of hours for the records of those who have more than one pet
"""
## 1(g) Find the percentage of smokers among the records for absences that
##      exceeded 8 hours, then do the same for absences of no more then 4 hours.

smokersAbsences = records[['Social smoker','Absenteeism time in hours']]   #data set of 'Social smoker' and 'Absenteeism time in hours'
print(smokersAbsences)

# for 8 hours
socialsmoker8Absent = smokersAbsences.loc[smokersAbsences['Absenteeism time in hours'] >8]   # only keep 'Absenteeism time in hours' that exceeded 8 hours
smoker8Absent2 = socialsmoker8Absent.loc[socialsmoker8Absent['Social smoker'] == 1]  # smoker among the 'Absenteeism time in hours' that exceeded 8 hours
100*len(smoker8Absent2)/len(socialsmoker8Absent)      # the percentage of smokers among the records for absence that exceeded 8 hours

# for 4 hours 
socialsmoker4Absent = smokersAbsences.loc[smokersAbsences['Absenteeism time in hours'] <= 4]   # only keep 'Absenteeism time in hours' no more than 4 hours
smoker4Absent2 = socialsmoker4Absent.loc[socialsmoker4Absent['Social smoker'] == 1]   #smoker that absences no more than 4 hours
100*len(smoker4Absent2)/len(socialsmoker4Absent)   # smoker that absences no more than 4 hours devided by total number of people who no more than 4 hours

"""
1g.

6.349206349206349    # the percentage of smokers among the records for absence that exceeded 8 hours is 6.349206349206349%

6.290672451193059    # the percentage of smokers among the records for abseces that no more than 4 hours is 6.290672451193059%
"""
## 1(h) Repeat 1(g), this time for social drinkers in place of smokers.


drinkersAbsences = records[['Social drinker','Absenteeism time in hours']]   #data set of 'Social smoker' and 'Absenteeism time in hours'

# for 8 hours
socialdrinker8Absent = drinkersAbsences.loc[drinkersAbsences['Absenteeism time in hours'] > 8]  # data with 'Absenteeism time in hours' more than 8 hours
drinker8Absent2 = socialdrinker8Absent.loc[socialdrinker8Absent['Social drinker'] == 1]   # with in 'socialdrinker8Absent', extract the 'Social drinker' which = 1
100*len(drinker8Absent2)/len(socialdrinker8Absent)    # the percentage of drinkers among the records for absence that exceeded 8 hours
 
# for 4 hours
socialdrinker4Absent = drinkersAbsences.loc[drinkersAbsences['Absenteeism time in hours'] <= 4]
drinker4Absent2 = socialdrinker4Absent.loc[socialdrinker4Absent['Social drinker'] == 1]
100*len(drinker4Absent2)/len(socialdrinker4Absent)    # the percentage of drinkers among the records for absence that no more than 4 hours

"""
1h.

73.01587301587301  # the percentage of drinkers among the records for absence that exceeded 8 hours is 73.01587301587301%

53.36225596529284   # the percentage of drinkers among the records for absence that no more than 4 hours is 53.36225596529284%

"""

## 2.  All questions refer to the data set 'absent.csv'.

## 2(a) Find the top-5 employee IDs in terms of total hours absent.  List
##      the IDs and corresponding total hours absent.

a= records['Absenteeism time in hours'].groupby(records['ID']) 
#group the hours absent by the employee ID
top = a.sum().sort_values(ascending= False)
#sort this group after counting the total hours absent
top2 = top[0:5]
#subsset the top 5 
print(top2) #prints employees hours missed with ID number


"""
2a.

ID
3     482
14    476
11    450
28    347
34    344
Name: Absenteeism time in hours, dtype: int64
"""
## 2(b) Find the average hours absent per record for each day of the week.
##      Print out the day number and average.

groupAverageAbsent = records['Absenteeism time in hours'].groupby(records['Day of the week']) # group the data in column 'Absenteeism time in hours' based entries in 'Day of the week'
groupAverageAbsent.mean()   # the average hours absent per record for each day of the week


"""
2b.

Day of the week 
2    9.248447   # the average hours absent per record for Monday
3    7.980519   # the average hours absent per record for Tuesday
4    7.147436   # the average hours absent per record for Wendesday
5    4.424000   # the average hours absent per record for Thursday
6    5.125000   # the average hours absent per record for Friday
Name: Absenteeism time in hours, dtype: float64
"""
## 2(c) Repeat 2(b) replacing day of the week with month.

groupAverageAbsent2 = records['Absenteeism time in hours'].groupby(records['Month of absence'])  # group the data in column 'Absenteeism time in hours' based entries in "Month of absence"
groupAverageAbsent2.mean() # the mean hours absent per record for 'Month of of absence' 

"""
2c.

Month of absence
0      0.000000   
1      4.440000   # the average hours absent per record for Jan
2      4.083333   # the average hours absent per record for Feb
3      8.793103   # the average hours absent per record for March
4      9.094340   # the average hours absent per record for April
5      6.250000   # the average hours absent per record for May
6      7.611111   # the average hours absent per record for June
7     10.955224   # the average hours absent per record for July
8      5.333333   # the average hours absent per record for Aug
9      5.509434   # the average hours absent per record for Sep
10     4.915493   # the average hours absent per record for Oct
11     7.507937   # the average hours absent per record for Nov
12     8.448980   # the average hours absent per record for Dec
"""
## 2(d) Find the top 3 most common reasons for absence for the social smokers,  
##      then do the same for the non-smokers. (If there is a tie for 3rd place,
##      include all that tied for that position.)

# for Social smokers
commonAbsentSocialsmokers = records.loc[records['Social smoker'] == 1]  # data with 'Social smoker'
groupAverageAbsent2 = commonAbsentSocialsmokers['Absenteeism time in hours'].groupby(commonAbsentSocialsmokers['Reason for absence']) # group the data in 'Absenteeism time in hours' based on the entries in column 'Reason for absence'
groupAA2count = groupAverageAbsent2.count()   # count the frecrency of reasons for absence and named it 'groupAA2count'
sort1= groupAverageAbsent2.count().sort_values(ascending=False)  # sort it from most frecrent to least frecrent reason
sort1[1:7]  # 0 doesn't count because it is not a reason for absent.

# for non- smokers
commonAbsentSocialsmokers2 = records.loc[records['Social smoker'] == 0]   # data with non smoker
groupAverageAbsent3 = commonAbsentSocialsmokers2['Absenteeism time in hours'].groupby(commonAbsentSocialsmokers2['Reason for absence']) # group the data in 'Absenteeism time in hours' based on the entries in column 'Reason for absence'
groupAA3count = groupAverageAbsent3.count() # count the frecrency of reasons for absence and named it 'groupAA3count'
sort2 = groupAverageAbsent3.count().sort_values(ascending=False)  # sort it from most frecrent to least frecrent reason
sort2.head(3) # most common reasons for absence  for the social smokers

"""
2d.

Reason for absence        # the answer for the social smokers
25    7
19    4
18    4
28    4
22    4
23    4
Name: Absenteeism time in hours, dtype: int64


Reason for absence                # top 3 most common reasons for absence for non smoker
23    145
28    108
27     69
Name: Absenteeism time in hours, dtype: int64
"""

## 2(e) Suppose that we consider our data set as a sample from a much
##      larger population.  Find a 95% confidence interval for the 
##      proportion of the records that are from social drinkers.  Use
##      the formula 
##
##  [phat - 1.96*sqrt(phat*(1-phat)/n), phat + 1.96*sqrt(phat*(1-phat)/n)]
##
## where "phat" is the sample proportion and "n" is the sample size.

## phat = sample porportion = percentSocialdrinker
## n is the sample size

socialdrinkerData = records.loc[records['Social drinker'] == 1]  # records that are from social drinkers
phat = len(socialdrinkerData)/len(records)  # the percentage of records that are from social drinkers
n = len(records)    # the number of sample size
lower = phat - 1.96*np.sqrt(phat*(1-phat)/n)    # lower conf. limit
upper = phat + 1.96*np.sqrt(phat*(1-phat)/n)    # upper conf. limit
[lower,upper]    # 95% confidence interval for the proportion of the records that are from social drinkers.

"""
2e.

[0.5318725067607831, 0.603262628374352]   # answer, the 95% confidence interval for the proportion of the records that are from social drinkers.
"""

## 3.  For this problem we return to simulations one more time.  Our
##     topic is "bias" of estimators, more specifically the "percentage
##     relative bias" (PRB) which we take to be
##
##        100*((mean of estimated values) - (exact value))/(exact value)
##
##     For instance, to approximate the bias of the sample mean in 
##     estimating the population mean, we would computer
##
##        100*((mean of sample means) - (population mean))/(population mean)
##
##     For estimators that are "unbiased" we expect that the average
##     value of all the estimates will be close to the value of the
##     quantity being estimated.  In these problems we will approximate
##     the degree of bias (or lack of) by simulating.  In all parts we
##     will be sampling from a population of 10,000,000 values randomly
##     generated from an exponential distribution with scale = 10 using
##     the code below.

pop = np.random.exponential(scale = 10, size = 10000000)


## 3(a) Compute and report the mean for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample mean for each of the samples,
##      compute the mean of the sample means, and then compute the PRB.

# loops are ok for number 3

pop = np.random.exponential(scale = 10, size = 10000000)  # population
allpop = []        # will hold mean for all of "pop"      
for i in range(100000):              
    sampleMean = np.mean(np.random.choice(pop, size = 10))   # sample mean for size of 10
    allpop.append(sampleMean)   # add it into the "allpop"
allpopMean = np.mean(allpop)    # mean of the sample means
print(allpopMean)  # print out 'allpopMean'
popmean = np.mean(pop)  # 9.999095465076808
print(popmean)   # print out 'popmean'
PRB = 100*((allpopMean - popmean))/(popmean)  # calculate the PRB
print(PRB)   # print out PRB

"""
3a.
10.005451156416616   # mean of sample mean
9.993329460708484    # mean of the population

0.0939209920434658   # the answer, PRB
"""
## 3(b) Compute and report the variance for all of "pop" using "np.var(pop)".  
##      Simulate 100,000 samples of size 10, then compute the sample variance 
##      for each sample using "np.var(samp)" (where "samp" = sample).  Compute 
##      the mean of the sample variances, and then compute the PRB.
##      Note: Here we are using the population variance formula on the samples
##      in order to estimate the population variance.  This should produce
##      bias, so expect something nonzero for the PRB.


allpop = []   # this array will hold all 100000 simulation of sample var
for i in range(100000):
    sampleVar = np.var(np.random.choice(pop,size=10))   # simulate samples size 10, and get it's variance
    allpop.append(sampleVar)     # append it into 'allpop'
meanSampleVar = np.mean(allpop)   # mean sample variance
print(meanSampleVar)   # print out 'meanSampleVar'
popVar = np.var(pop)   #  population var 
print(popVar)      # print out 'popVar'
PRB = 100*((meanSampleVar)-(popVar))/(popVar)  # calculate the PRB
print(PRB)    # print out PRB
# PRB = 100*((mean of sample var)-(population var))/(population var) 

"""
3b.
100.05000245343034 # population var
90.25034475673421  # mean of the 'all pop(array holds 100000 simulation of sample var)'

-9.90238507277264 # the answer, PRB
"""
## 3(c) Repeat 3(b), but this time use "np.var(samp, ddof=1)" to compute the
##      sample variances.  (Don't change "np.var(pop)" when computing the
##      population variance.)



allpop = []   # this array will hold all 100000 simulation of sample var(with ddof=1)
for i in range(100000):
    sample10 = np.random.choice(pop,size=10)   # simulate samples size 10
    sVar = np.var(sample10, ddof=1)   # get the vriance of the 'sample10' with ddof = 1
    allpop.append(sVar)    # append it into 'allpop'
meanSampleVar = np.mean(allpop)   # mean sample variance
print(meanSampleVar)     # print out 'meanSampleVar'
popVar = np.var(pop)   #  population var 
print(popVar)      # print out 'popvar'
PRB = 100*((meanSampleVar)-(popVar))/(popVar)   # calculate the PRB
print(PRB)   # print out the PRB

"""
3c.
90.55330117163051  # mean sample variance
99.96952116922739 # population var

-0.03511023130519673    # the answer, the PRB
"""
## 3(d) Compute and report the median for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample median for each of the samples,
##      compute the mean of the sample medians, and then compute the PRB.
##      Note: For nonsymmetric distributions (such as the exponential) the
##      sample median is a biased estimator for the population median.  The
##      bias gets decreases with larger samples, but should be evident with 
##      samples of size 10.


allpop = []   # this array will hold all the sample mean
for i in range(100000):
    sample10 = np.random.choice(pop,size=10)   # simulate sample size 10
    sMean = np.median(sample10)     # get the median of the 'sample 10'
    allpop.append(sMean)    # append it into 'allpop'
meanSampleMedian = np.mean(allpop)   # mean sample variance
print(meanSampleMedian)    # printout 'meanSampleMedian' 
popMedian = np.median(pop)   #  population var 
print(popMedian)        # printout 'popMedian'
PRB = 100*((meanSampleMedian)-(popMedian))/(popMedian)  # calculate the PRB
print(PRB)   # pint out the PRB

"""
3d.
7.464622002743975  # mean sample variance
6.931283066225854  # population var

7.630389505609777   # the answer, PRB 
"""