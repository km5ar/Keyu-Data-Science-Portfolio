##
## File: exam02.py (STAT 3250)
## Topic: Exam 2
## name: keyu chen - km5ar

##  As discussed in class, Exam 2 will be fairly close in form to assignments:
##  there is no "in-class" or timed portion, and you are welcome to talk with
##  other students about solution strategies.  Two major differences from 
##  assignments:
##
##  (1) Course assistants only will provide help with code debugging but will
##      not provide a lot of help with code strategy.
##  (2) Grading will be stricter than with assignments.  In particular, the
##      code efficiency and elegance will be considered in grading to a 
##      greater degree than on assignments.  Also taken into account will be
##      using coding approaches covered in class, rather than something 
##      found online or in another course.
##
##  Grading of Exam 2: 5 questions will be selected for scoring from 0-5,
##  and 5 points will be added for overall completeness, for a total of 30.

##  Note: There is no blanket prohibition on the use of loops, but loops can
##  be inefficient and inelegant so excessive use when non-loop options exist
##  is likely to result in score reductions.  (The same goes for reading in 
##  data.  You should not do that more than once.)

##  The exam is due by Thursday March 28 at 11:30pm.  Exams marked late by
##  Collab will receive a 2 point deduction.  No exams may be submitted after
##  Friday, March 29 at 11:30am.

##  This exam requires the data file 'airline-stats.txt'.  This file contains
##  over 50,000 records of aggregated flight information, organized by airline, 
##  airport, and month.  The first record is shown below.

# =============================================================================
# airport
#     code: ATL 
#     name: Atlanta GA: Hartsfield-Jackson Atlanta International
# flights 
#     cancelled: 5 
#     on time: 561 
#     total: 752 
#     delayed: 186 
#     diverted: 0
# number of delays 
#     late aircraft: 18 
#     weather: 28 
#     security: 2 
#     national aviation system: 105 
#     carrier: 34
# minutes delayed 
#     late aircraft: 1269 
#     weather: 1722 
#     carrier: 1367 
#     security: 139 
#     total: 8314 
#     national aviation system: 3817
# dates
#     label: 2003/6 
#     year: 2003 
#     month: 6
# carrier
#     code: AA 
#     name: American Airlines Inc.
# =============================================================================

import numpy as np # load numpy as np
import pandas as pd # load pandas as pd
airline = open('airline-stats.txt').read().splitlines()    # read in the data

airlineSeries = pd.Series(airline)   # turn the data into Series
airlineTotal = airlineSeries[airlineSeries.str.contains('total')]  # subset the data which contains 'total'
totalM = airlineTotal[1::2].str.split().str[1].reset_index(drop=True).astype(float)  # minutes delayed total
totalT = airlineTotal[0::2].str.split().str[1].reset_index(drop=True).astype(float)  # flight total

## 1.  Give the total number of hours delayed for all flights in all records.

np.sum(totalM)/60   # the answer, sum up the all the total under mintes delayed, then divided by 60

'''
1.

9991285.583333334     # the answer, total number of hours delayed for all flights in all records.
'''

## 2.  Which airlines appear in at least 1000 records?  Give a table of airline
##     names and number of records for each, in order of record count (largest
##     to smallest).

name = airlineSeries[airlineSeries.str.contains('name')]  # subset the data which contains 'name'
name1 = name[1::2].str.split(':').str[-1].reset_index(drop=True)  # subset the airline name, split(':') and only keep the name, then reset the index of the row 
name1Count = name1.value_counts()   # do a value counts on the airline name
name1Count[name1Count>1000]   # the answer, airlines appear in at least 1000 records

'''
2. 

 Delta Air Lines Inc.            4370                  # the answer, airlines appear in at least 1000 records
 American Airlines Inc.          4296
 United Air Lines Inc.           4219
 US Airways Inc.                 3918
 ExpressJet Airlines Inc.        3174
 Southwest Airlines Co.          2900
 JetBlue Airways                 2857
 Frontier Airlines Inc.          2821
 Continental Air Lines Inc.      2815
 AirTran Airways Corporation     2801
 Alaska Airlines Inc.            2678
 SkyWest Airlines Inc.           2621
 American Eagle Airlines Inc.    2379
 Northwest Airlines Inc.         2288
 Mesa Airlines Inc.              1682
 Comair Inc.                     1671
 Atlantic Southeast Airlines     1460
 Hawaiian Airlines Inc.          1073
dtype: int64
'''
    
## 3.  For some reason, the entry under 'flights/delayed' is not always the same
##     as the total of the entries under 'number of delays'.  (The reason for
##     this is not clear.)  Determine the percentage of records for which 
##     these two values are different.

group3 = ['delayed', 'late aircraft', 'weather', 'security', 'national aviation system', 'carrier:']

df3 = pd.DataFrame()  # create a new dataframe 'df3'
for i in range(len(group3)):      # for loop, which will run 6 times
    x = airlineSeries[airlineSeries.str.contains(group3[i])]   # subset the data which contains group3[i]
    x = x[0::2]             # keep other entry, start with 0
    x = x.str.split(':').str[-1]   # keep the number only
    x_df = pd.DataFrame(x).reset_index(drop = True)  # turn it into data frame, reset the index
    df3 = pd.concat([df3,x_df],axis=1)  # concat it into df3, by columns

df3.columns = ['delayed', 'late aircraft', 'weather', 'security', 'national aviation system', 'carrier']  # rename the column
df3 = df3.astype(float)  # turn the 'df3' to float

df3['totalDelays'] = (df3['late aircraft'] + df3['weather'] + df3['security'] + df3['national aviation system'] + df3['carrier']) # created a new column 'totalDelays', which equal the sum of late aircraft, weather, security, national aviation system and carrier
(sum(df3['delayed'] != df3['totalDelays'])/len(df3))*100  #  the percentage of records for which these two values are different

'''
3.

29.283690963286617    # the percentage of records for which these two values are different
'''

## 4.  Determine the number of records for which the number of delays due to
##     late aircraft exceeds the number of delays due to weather.

lateaircraft = airlineSeries[airlineSeries.str.contains('late aircraft')]    # subset the data contains 'late aircraft'
lateaircraft1 = lateaircraft[0::2].str.split(':').str[-1].astype(float).reset_index(drop=True)  # take out late airfraft(number of delays), split by ':' then keep the number only, and turn it into float and reset the index    
weather = airlineSeries[airlineSeries.str.contains('weather')]  # subset the data contains 'weather'
weather1 = weather[0::2].str.split(':').str[-1].astype(float).reset_index(drop=True)  # subset weather(number of delays),  split by ':' then keep the number only, and turn it into float and reset the index 

sum(lateaircraft1> weather1) # the answer, first compare 'lateaircraft1' with 'weather1', then sum up the number of records for which the number of delays due to late aircraft exceeds the number of delays due to weather.

'''
4.

46890   # the number of delays due to late aircraft exceeds the number of delays due to weather.
'''

## 5.  Find the top-10 airports in terms of the total number of minutes delayed.
##     Give a table of the airport names and the total minutes delayed, in 
##     order from largest to smallest.

name5 = name[0::2].str.split(':').str[-1].reset_index(drop=True)  # airport name only, reset the index
df5 = pd.concat([name5,totalM],axis=1) # create a data frame by concat column 'name5' and 'totalM' together, axis =1 means concat by column not by row
df5.columns = ['airport','total']  # rename the columns

group5 = df5['total'].groupby(df5['airport'])  # create a group5 by group 'total' with 'airport'
group5a = group5.sum().sort_values(ascending=False).head(10)  # sum the group5, the sort the value from the largest to smallest, then get the top 10.
group5a  # print out the answer, top 10 airports in terms of the total number of minutes delayed

'''
5.

airport                                    totalMinutes        # top-10 airports in terms of the total number of minutes delayed.                     
 Chicago O'Hare International                66079561.0
 Hartsfield-Jackson Atlanta International    61818488.0
 Dallas/Fort Worth International             39246534.0
 Newark Liberty International                33306693.0
 San Francisco International                 28980270.0
 Denver International                        27020884.0
 Los Angeles International                   26897269.0
 George Bush Intercontinental/Houston        24121262.0
 LaGuardia                                   22335295.0
 John F. Kennedy International               19985703.0
Name: totalMinutes, dtype: float64
'''

## 6.  Find the top-10 airports in terms of percentage of on time flights.
##     Give a table of the airport names and percentages, in order from 
##     largest to smallest.

ontime = airlineSeries[airlineSeries.str.contains('on time')]   # subset the data contains 'on time'
ontime1 = ontime.str.split(':').str[-1].astype(float).reset_index(drop=True) # keep the number only, by split ':' and str[-1], then change it into float and reset the index
total = airlineSeries[airlineSeries.str.contains('total')]  # subset the data contains 'total'
total1 = total[0::2].str.split(':').str[-1].astype(float).reset_index(drop=True)   # subset the total(flights), keep the number only by split (':') then str[-1], then turn the number into float and reset the index

df6 = pd.concat([name5,ontime1,total1],axis= 1) # create a df6 by concate the column 'name5','ontime1' and 'total1'
df6.columns = ['name','ontime','total']  # rename the columns 

group6 = df6[['ontime','total']].groupby(df6['name'])  # group 'ontime' and 'total' with 'name'
group6a = group6.sum()   # sum the group6
group6a['percentage'] = group6a['ontime']/group6a['total']  # create a new column 'percentage',
group6b = group6a.sort_values(by = 'percentage',ascending=False)*100  # sort value by column 'percentage', from largest to smartest 
group6c = group6b.head(10)  # keep the top 10
group6c['percentage']  # only keep the name and percentage column

'''
6.

name                                                    percentage   # top-10 airports in terms of percentage of on time flights.
 Salt Lake City International                            84.249328
 Phoenix Sky Harbor International                        82.423895
 Portland International                                  80.759415
 Minneapolis-St Paul International                       80.342827
 Chicago Midway International                            80.317165
 Charlotte Douglas International                         80.310017
 Baltimore/Washington International Thurgood Marshall    80.268309
 Denver International                                    80.236443
 Detroit Metro Wayne County                              80.182134
 George Bush Intercontinental/Houston                    80.117228
Name: percentage, dtype: float64
'''

## 7.  Find the top-10 airlines in terms of percentage of on time flights.
##     Give a table of the airline names and percentages, in order from 
##     largest to smallest.

df7 = pd.concat([ontime1,total1,name1],axis= 1)    # created a new df7 by concat the columns 'ontime1','total1' and 'name1'
df7.columns = ['ontime','total','name']   # rename the columns 
group7 = df7[['ontime','total']].groupby(df7['name'])  # group 'ontime' and 'total' with 'name'
group7Sum = group7.sum()  # sum the group7
group7Sum['percentage'] = group7Sum['ontime']/group7Sum['total']*100  # create a new column 'percentage' in group7Sum by ('ontime' devided by 'total') times 100
group7percentage = group7Sum.sort_values(by = 'percentage', ascending=False)  # sort values by the 'percentage', from largest to smallest
answer = group7percentage.head(10)  # top-10 airlines in terms of percentage of on time flights.
answer['percentage']   # answer, only shows airline names and percentages of the top 10 

'''
7.

name                          percentage    # the answer, top-10 airlines in terms of percentage of on time flights.
 Endeavor Air Inc.             84.050792
 Alaska Airlines Inc.          81.888334
 Virgin America                81.492009
 Aloha Airlines Inc.           80.934150
 Delta Air Lines Inc.          80.411719
 SkyWest Airlines Inc.         80.102370
 Southwest Airlines Co.        80.061932
 America West Airlines Inc.    79.373011
 Hawaiian Airlines Inc.        79.308415
 US Airways Inc.               78.974549
Name: percentage, dtype: float64
'''

## 8.  Determine the average length (in minutes) of a weather-related delay.

weather2 = weather[1::2].str.split(':').str[-1].astype(float).reset_index(drop=True)  # subset the weather(minutes delayed), keep number only by split(':') and str[-1], then change it to float and reset the index
np.sum(weather2)/np.sum(weather1)  # the average length (in minutes) of a weather-related delay, by sum the weather(minutes delayed) devided by the sum of (weather)number of delays

'''
8.

80.25100063808806    # the answer, the average length (in minutes) of a weather-related delay.
'''

## 9.  For each month, determine which airport had the highest percentage
##     of delays.  Give a table listing the month number, the airport name,
##     and the percentage.

month = airlineSeries[airlineSeries.str.contains('month')]  # subset the data which ocntains 'month' 
month1 = month.str.split(':').str[-1].reset_index(drop=True).astype(int)  # keep the month only, turn it into interger
delayed = airlineSeries[airlineSeries.str.contains('delayed:')]  # subset the data which contains 'delayed:'
delayed1 = delayed.str.split(':').str[-1].reset_index(drop=True).astype(float) # keep the number only, reset the index, and turn it into float
df9 = pd.concat([month1,name5,delayed1,totalT],axis= 1) # concat column 'month1', 'name5', 'delayed1' and 'totalT'
df9.columns = ['month','name','delayed','total']  # rename all the column

group9 = df9[['delayed','total']].groupby([df9['month'],df9['name']])  # create a new group, group 'delayed' and 'total' with 'month' and 'name'
group9Sum = group9.sum()  # sum the group9 
group9Sum['percentage'] = group9Sum['delayed']/group9Sum['total']*100   # created a new column 'percentage' in group9Sum, 
group9Sum = group9Sum['percentage'].groupby(level=0, group_keys=False)  # groupby the first level of the index
print(group9Sum.nlargest(1)) #extracts largest value of % per month

'''
9.

month  name                            percentage  # the answer, for each month, the highest percentage of delays    
1       Chicago O'Hare International    27.392193
2       Newark Liberty International    27.909382
3       Newark Liberty International    31.613341
4       Newark Liberty International    30.250067
5       Newark Liberty International    30.339172
6       Newark Liberty International    32.249598
7       Newark Liberty International    31.445250
8       Newark Liberty International    27.601543
9       Newark Liberty International    23.935120
10      Newark Liberty International    26.140379
11      Newark Liberty International    26.961231
12      Newark Liberty International    33.508850
Name: percentage, dtype: float64
'''

## 10. For each year, determine the percentage of flights delayed by weather.

year = airlineSeries[airlineSeries.str.contains('year')]   # subset the data which contains 'year'
year1 = year.str.split(':').str[-1].reset_index(drop=True).astype(int)  # keep the number only, by split(':') and str[-1], then reset the index and turn it into interger
df10 = pd.concat([year1,total1,weather1],axis= 1)  # concat the column 'year1' 'total1' and 'weather1' together, by column
df10.columns = ['year','total','weather']   # rename the column

group10 = df10[['weather','total']].groupby(df10['year'])   # group 'weather' and 'total' with 'year'
group10Sum = group10.sum()  # sum the group10
group10Sum['percentage'] = group10Sum['weather']/group10Sum['total']*100   # created a new column 'percentage' in group10Sum, which equal ('weather'/'total')*100
group10Sum['percentage']  # keep only year and percentage

'''
10,

year    percentage            # the percentage of flights delayed by weather.
2003    0.653742
2004    0.816713
2005    0.757056
2006    0.795570
2007    0.871017
2008    0.725152
2009    0.620590
2010    0.529282
2011    0.494533
2012    0.470042
2013    0.543351
2014    0.598251
2015    0.604453
2016    0.502287
Name: percentage, dtype: float64
'''

## 11. Find the top-10 airports in terms of average length (in minutes) of 
##     security-related flight delays.  Give a table listing the airport name 
##     and average, sorted from largest to smallest.

security = airlineSeries[airlineSeries.str.contains('security')]   # subset the data which contains 'security'
security1 = security[1::2].str.split(':').str[-1].astype(float).reset_index(drop=True)  # keep the number only, then turn it into float and reset the index
security2 = security[0::2].str.split(':').str[-1].astype(float).reset_index(drop=True)   # number of delay(security)

df11 = pd.concat([name5,security1,security2],axis= 1)  # concat 'name5' 'security1' 'security2', by column
df11.columns = ['airport','security','securitynumber']   # rename the column

group11 = df11[['security','securitynumber']].groupby(df11['airport']).sum()  # group 'securirty' and 'securitynumber' by 'airport'
group11a = group11['security']/group11['securitynumber'] # 'security' divided by 'securitynumber' to get the delay per flight by airport
group11a.sort_values(ascending=False).head(10)   # top 10 airport name and average, sorted from largest to smallest


'''
11.

airport                                     security       # the answer, top-10 airports in terms of average length (in minutes) of security-related flight delays.
 Hartsfield-Jackson Atlanta International    49.742964
 Logan International                         46.457082
 Chicago O'Hare International                46.311587
 Miami International                         45.400826
 Ronald Reagan Washington National           42.258621
 San Francisco International                 42.183099
 Newark Liberty International                41.232283
 John F. Kennedy International               40.967069
 LaGuardia                                   40.853896
 Washington Dulles International             40.224490
dtype: float64
'''



## 12. Determine the top-10 airport/airline combinations that had the lowest
##     percentage of delayed flights.  Give a table listing the airport name,
##     the airline name, and the percentage of delayed flights, sorted in
##     order (smallest to largest) of percentage of delays.
df12 = pd.concat([name5,name1,delayed1,total1],axis= 1)  # concat 'name5' 'name1' 'delayed1' and 'total1' by columns
df12.columns = ['airport','airline','delayed','total']   # rename all the columns

group12a = df12[['total','delayed']].groupby((df12['airport'],df12['airline']))   # group 'total' and 'delayed' by 'airport' and 'airline'
group12b = group12a.sum()  # sum the 'group12a'
group12b['percentage'] = group12b['delayed']/group12b['total']*100  # created a new column 'percentage' in group12b, which equal ('delayed'/'total')*100
group12c = group12b.sort_values(by = 'percentage')   # sort value by the column 'percentage'
group12d = group12c.head(10)   # keep the top 10
group12d['percentage']   # only show airport name, airline name and the percentage of delayed flight

'''
12.

airport                                                airline                    percentage   # the top-10 airport/airline combinations that had the lowest percentage of delayed flights.
 McCarran International                                 Comair Inc.                0.000000
 Phoenix Sky Harbor International                       Pinnacle Airlines Inc.     0.000000
 John F. Kennedy International                          Alaska Airlines Inc.       4.347826
 Salt Lake City International                           Alaska Airlines Inc.       8.567829
 Baltimore/Washington International Thurgood Marshall   Alaska Airlines Inc.       8.689024
 Fort Lauderdale-Hollywood International                Endeavor Air Inc.          8.695652
 Fort Lauderdale-Hollywood International                SkyWest Airlines Inc.      9.090909
 Tampa International                                    SkyWest Airlines Inc.     10.000000
 Orlando International                                  Virgin America            10.635226
 Detroit Metro Wayne County                             Endeavor Air Inc.         10.828148
Name: percentage, dtype: float64
'''
