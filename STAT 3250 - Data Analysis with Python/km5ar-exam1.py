##
## File: exam1.py (STAT 3250)
## Topic: Exam 1
## Name: KEYU CHEN - KM5AR
## 

import numpy as np # load numpy as np
import pandas as pd
bankdata = pd.read_csv('bankdata.csv')

array1 = np.array([[13,0,2,-3,2,-4,0,7,-5],
                   [0,5,-2,-1,-4,5,4,9,12],
                   [5,11,-1,-8,0,-3,5,6,7],
                   [-9,2,4,10,0,3,2,-4,-5]])

# 1a
array1b = array1[:,[1,4]]
print(array1b)

# 1b
array1c = array1[[0,2]][:,[1,6]]     # [0,2] 1st and 3rd row    [:,[1,2]] 2rd 3rd
print(array1c)

#1c

array2 = array1[array1 < 2]
array2.mean()


#1d

array1d = np.where(array1 >3, -1, array1)
np.var(array1d,ddof=1)




#2.
# 2a

100*np.sum(bankdata['contact'] == 'telephone')/len(bankdata)

# 2b

group2b = bankdata['duration'].groupby(bankdata['day_of_week'])
group2b.mean()

# 2c

jobmarital = bankdata[['job','marital']]
services = jobmarital.loc[jobmarital['job'] == 'services']
servicesDivorced = services.loc[services['marital'] == 'divorced']
100*len(servicesDivorced)/len(services)

# 2d


pdaysNon999 = bankdata.loc[bankdata['pdays'] != 999]
pdaysNon9991 = pdaysNon999['pdays']
pdaysNon9991.mean()

jobmarital = bankdata[['job','marital']]
pdays = bankdata['pdays']


# 2e

group21 = bankdata.loc[bankdata['housing']]
group21 = group21['job'].groupby(group21['housing'])
group211 = group21.count()
sort1 = group21 = group211.count().sort_values(ascending=False)

# for Social smokers
commonAbsentSocialsmokers = records.loc[records['Social smoker'] == 1]  # data with 'Social smoker'
groupAverageAbsent2 = commonAbsentSocialsmokers['Absenteeism time in hours'].groupby(commonAbsentSocialsmokers['Reason for absence']) # group the data in 'Absenteeism time in hours' based on the entries in column 'Reason for absence'
groupAA2count = groupAverageAbsent2.count()   # count the frecrency of reasons for absence and named it 'groupAA2count'
sort1= groupAverageAbsent2.count().sort_values(ascending=False)  # sort it from most frecrent to least frecrent reason
sort1[1:7]  # 0 doesn't count because it is not a reason for absent.


# 2f


group2e = bankdata['education']

array2f = []
for i in range(len(group2e)):
    if group2e[i] == 'university.degree':
        array2f.append(i)
[np.percentile(array2f,2.5),np.percentile(array2f,97.5)]
        


#3.

np.random.exponential(scale = 10, size = 10)

ct = 0
array = []
for i in range(100000):
    s = np.random.exponential(scale=10,size=10)
    array.append(s)

[np.percentile(array,2.5),np.percentile(array,97.5)]    







