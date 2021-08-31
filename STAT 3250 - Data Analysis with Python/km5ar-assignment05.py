##
## File: assignment05.py (STAT 3250)
## Topic: Assignment 5
## name: KEYU CHEN - km5ar

import numpy as np # load numpy as np
import pandas as pd   
db = pd.read_csv('diabetic_data.csv') 

##  This assignment requires the data file 'diabetic_data.csv'.  This file
##  contains records for over 100,000 hospitalizations for people who have
##  diabetes.  The file 'diabetic_info.csv' contains information on the
##  codes used for a few of the entries.  Missing values are indicated by
##  a '?'.  You should be able to read in this file using the usual 
##  pandas methods.

##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  

## 1.  Determine the average number of medications ('num_medications') for 
##     males and for females.

group1 = db['num_medications'].groupby(db['gender'])   # group 'num_mediacations' to 'gender'
meanGroup1 = group1.mean() # mean of the male, female and unknown/invalid
meanGroup1.iloc[0:2]  # the answer, the average number of medications ('num_medications') for males and for females.
'''
1

gender                   # the answer, the average number of medications ('num_medications') for males and for females.
Female    16.187888
Male      15.828775
Name: num_medications, dtype: float64
'''

## 2.  Determine the average length of hospital stay ('time_in_hospital')
##     for each race classification.  (Omit those unknown '?' but include 
##     those classified as 'Other'.)

group2 = db['time_in_hospital'].groupby(db['race']) # group 'time_in_hospital' with 'race'
meanGroup2 = group2.mean()    # find the mean of group2
meanGroup2 = meanGroup2[1:len(meanGroup2)]  # the answer, omit unkown
print(meanGroup2)   # print out the answer

'''
2

race
AfricanAmerican    4.507860
Asian              3.995320
Caucasian          4.385721
Hispanic           4.059892
Other              4.273572
Name: time_in_hospital, dtype: float64
'''

## 3.  Among males, find a 95% confidence interval for the proportion that 
##     had at 2 or more procedures ('num_procedures').  Then do the same 
##     for females.

# lcl = phat - 1.96*(phat*(1-phat)/n)**0.5#lower interval for males
# ucl = phat + 1.96*(phat*(1-phat)/n)**0.5#upper interval for males

group3 = db[['gender','num_procedures']]    # keep only 'gender' and 'num_procedures'
maleGroup3 = group3.loc[group3['gender'] == 'Male']   # from data set 'group3', keep only 'gender' = 'Male'
maleTotal = len(maleGroup3)   # the total number of male
maleGroup3at2 = maleGroup3.loc[maleGroup3['num_procedures'] >= 2]  # from maleGroup3, keep only when 'num_procedures' equal or larger than 2
maleGroup3at2Total = len(maleGroup3at2)  # the total number of male which had at 2 or more procedures
phat = maleGroup3at2Total/maleTotal   # percentage of male who had at 2 or more procedures
lcl = phat - 1.96*np.sqrt(phat*(1-phat)/maleTotal)  # lower conf. limit for male
ucl =  phat + 1.96*np.sqrt(phat*(1-phat)/maleTotal) # upper conf. limit for male
print((lcl,ucl))   # 95% confidence interval for male

# female
# lcl = phat - 1.96*(phat*(1-phat)/n)**0.5#lower interval for female
# ucl = phat + 1.96*(phat*(1-phat)/n)**0.5#upper interval for female
group3b = db[['gender','num_procedures']] # subset data, only keep 'gender' and 'num_procedures'
femaleGroup3f = group3b.loc[group3b['gender'] == 'Female']   # only keep 'gender' which == 'Female'
femaleTotal = len(femaleGroup3f)   # total number of female
femaleGroup3at2 = femaleGroup3f.loc[femaleGroup3f['num_procedures'] >= 2]  # keep data of female which had at 2 or more procedures
femaleGroup3at2Total = len(femaleGroup3at2)  # total number of female which had at 2 or more procedures
phat1 = femaleGroup3at2Total/femaleTotal    # percentage of female who had at 2 or more procedures
lcl1 = phat1 - 1.96*np.sqrt(phat1*(1-phat1)/femaleTotal)   # lower conf. limit for female
ucl1 =  phat1 + 1.96*np.sqrt(phat1*(1-phat1)/femaleTotal)   # # upper conf. limit for female
print((lcl1,ucl1))  # 95% confidence interval for female

'''
3

(0.3551161035669802, 0.36378730733515563)   # male

(0.31516986803938, 0.32298177340245665)   # female
'''

## 4.  Among the patients in this data set, what percentage had more than
##     one recorded hospital visit?  (Each distinct record can be assumed 
##     to be for a distinct hospital visit.)

patientCount = db['patient_nbr'].value_counts()   # value count 'patient_nbr'
patientCount1 = len(patientCount[patientCount>1]) # number of patient had more than one recorded hispital visit
print(patientCount1/len(patientCount)*100)     # number of patient had more than one recorded hospital visit devided by total number of patient, the percentage had more than one recorded hospital vist

'''
4

23.452837048015883    # the percentage had more than one recorded hospital vist
'''

## 5.  List the top-10 most common diagnoses, based on the codes listed in
##     the columns 'diag_1', 'diag_2', and 'diag_3'.

diag1 = db['diag_1'].value_counts()   # value count 'diag_1'
diag2 = db['diag_2'].value_counts()   # value count 'diag_2'
diag3 = db['diag_3'].value_counts()   # value count 'diag_3'
m5 = diag1 + diag2 + diag3             # add the value count of diag1, diag2, and diag3 together
m6 = m5.sort_values(ascending=False)   # sort it from largest to smallest
m6.head(10)                            # top 10 most common diagnoses

'''
5

428    18101             # the top 10 most common diagnoses
250    17861
276    13816
414    12895
401    12371
427    11757
599     6824
496     5990
403     5693
486     5455
dtype: float64
'''


## 6.  The 'age' in each record is given as a 10-year range of ages.  Assume
##     that the age for a person is the middle of the range.  (For instance,
##     those with 'age' [40,50) are assumed to be 45.)  Determine the average
##     age for each classification in 'insulin'.

ageList = np.unique(db['age'])

def ageFunction(x): # Returns the median age
    if x == '[0-10)':   # check if condition meet
        return(5)       # if meet, return 5
    elif x == '[10-20)': # check if condition meet
        return(15)      # if meet, return 15
    elif x == '[20-30)': # check if condition meet
        return(25)      # if meet, return 25
    elif x == '[30-40)': # check if condition meet
        return(35)      # if meet, return 35
    elif x == '[40-50)': # check if condition meet
        return(45)      # if meet, return 45
    elif x == '[50-60)': # check if condition meet
        return(55)      # if meet, return 55
    elif x == '[60-70)': # check if condition meet
        return(65)      # if meet, return 65
    elif x == '[70-80)': # check if condition meet
        return(75)      # if meet, return 75
    elif x == '[80-90)': # check if condition meet
        return(85)      # if meet, return 85
    elif x == '[90-100)': # check if condition meet
        return (95)     # if meet, return 95
db['ageAverage'] = db['age'].apply(ageFunction) #apply function to column 'age' then make it as new column 'ageAverage'
group5 = db['ageAverage'].groupby(db['insulin']) # 'ageAverage' groupby 'insulin' classification
group5.mean()    # mean of group 5 

'''
6.

insulin
Down      63.300049
No        67.460165
Steady    65.571169
Up        63.673560
Name: ageAverage, dtype: float64
'''
## 7.  Among those whose weight range is given, assume that the actual
##     weight is at the midpoint of the given interval.  Determine the
##     average weight for those whose 'num_lab_procedures' exceeds 50,
##     then do the same for those that are fewer than 30.

np.unique(db['weight'])  # find out the range of the weight in this dataset
#array(['>200', '?', '[0-25)', '[100-125)', '[125-150)', '[150-175)',
#       '[175-200)', '[25-50)', '[50-75)', '[75-100)'], dtype=object)

def weightFunction(x): # Returns the mean weight
    if x == '[0-25)':   # if the condition meet 
        return(12.5)    # return 12.5
    elif x == '[25-50)': # # if the condition meet 
        return(37.5) # return 37.5
    elif x == '[50-75)': # # if the condition meet 
        return(62.5) # return 62.5
    elif x == '[75-100)': # if the condition meet 
        return(87.5)  # return 87.5
    elif x == '[100-125)': # if the condition meet 
        return(112.5)  # return 112.5
    elif x == '[125-150)': # if the condition meet 
        return(137.5)   # return 137.5
    elif x == '[150-175)': # if the condition meet 
        return(162.5)   # return 16.25
    elif x == '[175-200)': # if the condition meet 
        return(187.5)   # return 187.5
    elif x == '>200': # if the condition meet 
        return(200)  # return 200
db = db[db.weight != '?'] # ignore the data which == to '?'
db['averageWeight'] = db['weight'].apply(weightFunction) #applies function and creates new column
over50Procedures = db[db['num_lab_procedures'] > 50] #subset, keep 'num_lab_procedures' over 50 procedures
less30Procedures = db[db['num_lab_procedures'] < 30] #subset, keep 'num_lab_procedures' fewer than 30 procedures
over50Procedures['averageWeight'].mean() # mean weight of those with over 50 procedures 
less30Procedures['averageWeight'].mean() #mean weight of those with fewer than 30 procedures


'''
7

85.05018489170628   # mean weight of those with over 50 procedures 
88.73546511627907   # mean weight of those with fewer than 30 procedures
'''
## 8.  Three medications for type 2 diabetes are 'glipizide', 'glimepiride',
##     and 'glyburide'.  There are columns in the data for each of these.
##     Determine the number of records for which at least two of these
##     are listed as 'Steady'.

#pd.Series(['glipizide','glimepiride','glyburide']).isin(y)
#glipizide1 = db[['glipizide','patient_nbr']]

np.unique([db['glipizide']])    # to see how many different different condition there is in 'glipizide'
np.unique([db['glimepiride']])  # to see how many different different condition there is in 'glimepiride'
np.unique([db['glyburide']])    # # to see how many different different condition there is in 'glyburide'

def threeMedications(x):   # define the function
    if x == 'Steady':      # if x == 'Steady'
        return(1)              # if condition meet, return 1
    else:                   # bc there is 'Down', 'No', 'Up'] so we can use else to include those three
        return(0)           # if the x is not 'Steady', return 0
db['glipizide111'] = db['glipizide'].apply(threeMedications)  # add a new column for db which equal to apply function 'threeMedications' to the column'glipizide' 
db['glimepiride111'] = db['glimepiride'].apply(threeMedications) # add new column for db which equal to apply function 'threeMedications' to the column 'glimepride'
db['glyburide111'] = db['glyburide'].apply(threeMedications)  # add new column for db which equal to apply function 'threeMedications' to the column 'glyburide'
db['sumggg'] = db['glipizide111'] + db['glimepiride111'] + db['glyburide111']   # add 3 list together
atleasttwo = db.loc[db['sumggg'] >= 2]   # fun records which at least two of those are listed as 'Steady'
len(atleasttwo)   #  count how many of records at least two of those are listed as 'Stead'

'''
8.

284    # the answer, the number of records for which at least two of these are listed as 'Steady'
'''

## 9.  What percentage of reasons for admission ('admission_source_id')
##     correspond to some form of transfer from another care source?

# transfer from another care source, 4,5,6,10,18,22,25,26
def transfer(x):
    if x == 4 or x== 5 or x== 6 or x== 10 or x== 18 or x== 22 or x== 25 or x== 26: # if the patient is transfer from another care source
        return(1)           # if the condition meet, return 1
    else:                    # if the patient is not transfer from another care source
        return(0)         # return 0
db['transfer'] = db['admission_source_id'].apply(transfer) # created a new column 'transfer', equal to (apply the function transfer to 'admission_source_id')
transfer = db['transfer']    # subset the db['transfer']
totalTransfer = transfer.sum()    # sum the transfer
source_id = db['admission_source_id']   # subset the db['admission_source_id']
totalAdmission = source_id.count()   #  count the number of 'source_id'
100*totalTransfer/totalAdmission   # the answer total number of transfer devided by total admission number 

'''
9

6.218186820745633                # the answer, the percentage of reasons for admission correspond to some form of transfer from antoher care source. 
'''

## 10. The column 'discharge_disposition_id' gives codes for discharges.
##     Determine which codes (and the corresponding outcomes from the ID
##     file) resulted in no readmissions ('NO' under 'readmitted').  Then
##     find the top-5 outcomes that resulted in readmissions, in terms of
##     the percentage of times readmission was required.

noReadmitted = db[db['readmitted']== 'NO']   # keep the data which 'readmitted' == 'NO'
noReadmittedCount = noReadmitted['discharge_disposition_id'].value_counts()  # value_counts for noReadmitted
dispositionCount = db['discharge_disposition_id'].value_counts()   # value_counts for db['discharge_disposition_id']
disposition10 = dispositionCount - noReadmittedCount    # get the non-readmissions
disposition10[disposition10==0]   # non-readmissions

dispositionCountSort = dispositionCount.sort_index()    # sort it by dinxe
disposition10Percent = (disposition10/dispositionCountSort)*100   # percentage 
disposition10PercentSort = disposition10Percent.sort_values(ascending=False)   # sort the percentage
disposition10PercentSort.head()   # top 5

'''
10
                           # codes which resulted in no readmissions
11    0                           # Expired
19    0                           # Expired at home. Medicaid only, hospice.
20    0                           # Expired in a medical facility. Medicaid only, hospice.
Name: discharge_disposition_id, dtype: int64


15    73.015873                      # top 5 outcomes that resulted in readmissions, by percentage
10    66.666667
12    66.666667
28    61.151079
16    54.545455
Name: discharge_disposition_id, dtype: float64
'''