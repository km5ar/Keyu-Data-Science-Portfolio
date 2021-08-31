##
## File: exam-solns.py (STAT 3250)
## Topic: Exam 3 Solutions
## Name: KEYU CHEN - km5ar

##  Exam 3 consists of three sections. 
#  All code should be submitted as a single Python file. 
# Section 3 is on creating plots.  
# The plots will be submitted in a separate PDF document.

import json
import numpy as np
import pandas as pd
import re
import glob
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import datetime

###############################################################################
####
####  Section A
####
###############################################################################

##  For this portion of Exam 3 you will be working with Twitter data related
##  to the season opening of Game of Thrones on April 14.  
# You will use a set of 10,790 tweets for this purpose.  
# The data is in the file 'GoTtweets.txt'.  
##  The code below can be used to import the data into a list, with each
##  list element a dict of the tweet object.


# Read in the tweets and append them to 'tweetlist'
tweetlist = [] 
for line in open('GoTtweets.txt', 'r'): # Open the file of tweets
    tweetlist.append(json.loads(line))  # Add to 'tweetlist' after converting
tweetlist

## A1. The tweets were downloaded in several groups at about the same time.
## Are there any that appear in the file more than once?  
# List the tweet ID for any repeated tweets, 
# along with the number of times each is repeated.

## Note: For the remaining questions in this section, 
# do not worry about the duplicate tweets.  
# Just answer the questions based on the existing data set.

# 1) duplicates 
# 2) list tweet ID for repeated tweets
# 3) along with number of times each is repeated
list = []    # hold the ID numbers
for x in range(len(tweetlist)):  # for loop
    list.append(tweetlist[x]['id'])  # append all the 'id' number into 'list'
    
pd.Series(list).value_counts()[pd.Series(list).value_counts()>1]  # turn 'list' then value_counts on it, print out the number of times which are larger than 1.
'''
A.1

1117608744639025152    2   # the answer, the tweet ID that appear in the file more than once.
1117608741099069440    2
1117619562588057600    2
1117619559043948544    2
dtype: int64
'''


## A2. Some tweeters like to tweet a lot.  
# Find the screen name for all tweeters with at least 5 tweets in the data.
#   Give the screen name
##  and the number of tweets.  

# 1) screen name for all tweeters with at least 5 tweets 
# 2) give the screen name and the number of tweets

list2 = []  # hold the 'screen_name'

for x in range(len(tweetlist)):  # for loop
    list2.append(tweetlist[x]['user']['screen_name']) # append 'screen_name' into 'list2'
pd.Series(list2).value_counts()[pd.Series(list2).value_counts()>=5]  # change 'list2' to series, then value_counts it, print out the 'screen name' for all tweeters with at least 5 tweets in the data

'''
A2.

Eleo_Ellis         6    # the answer, the screen name for all tweeters with at least 5 tweets in the data.
taehyungiebtsdm    6
Czo18              5
_sherycee          5
caioomartinez      5
dtype: int64
'''

## A3. Determine the number of tweets that include the hashtag '#GoT', then
##     repeat for '#GameofThrones'.
##     Note: Hashtags are not case sensitive, so any of '#GOT', '#got', 'GOt' 
##     etc are all considered matches.  Each tweet object has a list of
##     hashtag objects -- use those for this problem, not the text of the
##     tweet.

GOT = 0              # counter
GameOfThrones = 0   #counter
for tweet in tweetlist:  # for loop
    hashtags = tweet['entities']['hashtags']  # subset 'hashtages'
    for i in hashtags:  # for loop
        if (i['text'].lower() == 'got'):  # if statement
            GOT +=1        # add 1 if hashtag contains 'got'
GOT   # print out the number of tweets that include the hashtag '#GoT'

for tweet in tweetlist:   # for loop
    hashtags = tweet['entities']['hashtags']  # subset 'hashtages'
    for i in hashtags:    # for loop
        if (i['text'].lower() == 'gameofthrones'):  # if statment
            GameOfThrones += 1    # add 1 if hashtag contains 'gameofthrones'
GameOfThrones  # the number of tweets that include the hashtag '#GameofThrones'


'''
A3.

1032       # the number of tweets that include the hashtag '#GoT'

8366        # the number of tweets that include the hashtag '#GameofThrones'
'''

## A4. Among the screen names with 4 or more tweets, find the
##     'followers_count' for each and then give a table of the top-5 
##     (plus ties) in terms of number of followers. Include the screen 
##     name and number of followers.

## A4. Among the screen names with 4 or more tweets, find the
## 'followers_count' for each and then give a table of the top-5
## (plus ties) in terms of number of followers. Include the screen
## name and number of followers. (If the number of followers changes
## for a given screen name, then report the average number of followers
## among all of the tweeter's tweets.)

tweeters = []  # hold for 'screen_name'
followers = []  # hold for 'followers_count'
for i in range(len(tweetlist)):  # for loop
    tweeters.append(tweetlist[i]['user']['screen_name'])  # append 'screen_name'
    followers.append(tweetlist[i]['user']['followers_count'])  # append 'followers_count'
dfA4 = pd.DataFrame({'sName':tweeters, 'Followers':followers})   # create a new DataFrame
dfA4Larger4 = dfA4['sName'].value_counts()[dfA4['sName'].value_counts()>= 4]  # value counts on dfA4['sName'], subset the value count which larger or equal to four
dfA4[dfA4['sName'].isin(dfA4Larger4.index)].groupby('sName').mean().sort_values(by='Followers', ascending = False).head(5)  # top 5 screen names with most followers

'''
A4.

Handle            Followers         # top-5 in terms of number of followers
bbystark          9313.00
Gamoraavengxr     3842.00
Eleo_Ellis        2948.00
HellblazerArts    2506.00
Dahoralu          1901.25
'''

## A5. Find the mean number of hashtags included in the tweets. 

hashtagsPertweet = []  # hold the hashtags per tweet
for tweet in tweetlist:  # for loop
    hashtagsCount = len(tweet['entities']['hashtags'])  # how many hashtags  
    hashtagsPertweet.append(hashtagsCount)     # add the number of hashtags into 'hashtagsPertweet'
np.mean(hashtagsPertweet)  # the answer, the mean number of hashtags included in the tweets. 

'''
A5.

1.0022242817423541  #  the answer,the mean number of hashtags included in the tweets.

'''

## A6. Give a table of hashtag counts: How many tweets with 0, 1, 2, ...
##     hashtags?
       
hashtag = []   #  hold 'hashtags' 
for x in range(len(tweetlist)):  # for loop
    hashtag.append(tweetlist[x]['entities']['hashtags'])  # append all the 'hashtags' from tweetlist into 'hashtage'

countA6 = []  # hold the len(hashtage[x])
for x in range(len(hashtag)):  # for loop
    countA6.append(len(hashtag[x])) # append (len(hashtage[x])) into CountA6
    
valueCounts = pd.Series(countA6).value_counts().sort_values(ascending = False).reset_index()  # turn 'countA6' into series, value_counts on it, sort the value from largest to smallest, then reset the index()
valueCounts.columns = ['hashtags','count'] # change the column name
valueCounts.sort_values(by = 'hashtags',ascending = True)  # sort the values by the column 'hashtags' from small to large.

'''
A6.

    hashtags  count   # the answer, the talbe of hashtag counts
1          0   1575
0          1   8111
2          2    768
3          3    242
4          4     55
5          5     24
6          6     10
7          7      2
8          8      1
9          9      1
10        10      1
'''

## A7. Determine the number of tweets that include 'Daenerys' (any combination
##     of upper and lower case) in the text of the tweet.  Then do the same 
##     for 'dragon'.

# change all the upper case to lower case
# number of tweets include 'Daenerys' and 'dragon'

lower = []   # hold all the low case data
for x in range(len(tweetlist)):     # for loop
    lower.append(tweetlist[x]['text'].lower())   # turn all 'text' into lower case, then append it into 'lower'

CountA7Daenerys = 0    # hold the count of Daenerys
for x in range(len(lower)):  # for loop
    if 'daenerys' in lower[x]:  # if 'daenerys' is in the lower
        CountA7Daenerys +=1    # add 1 to 'CountA7Daenerys'
CountA7Daenerys       # print out the count of 'CountA7Daenerys'

CountA7dragon = 0     # hold the count of dragon
for x in range(len(lower)):   # for loop
    if 'dragon' in lower[x]:   # if 'dragon' is in 'lower'
        CountA7dragon +=1   # add 1 to 'CountA7dragon'
CountA7dragon   # print out the count of 'CountA7dragon'


'''
A7.

735    # number of tweets include 'Daenerys'

385    # number of tweets include 'dragon'
'''


## A8.  Determine the 5 most frequent hashtags, and the number of tweets that
##      each appears in.  As usual, give a table.

# 1) 5 most frequeent hashtags
# 2) number of tweets each appears in

hashtageA8 = []  # hold the 'hashtags' section
for x in range(len(tweetlist)):   # for loop
    hashtageA8.append(tweetlist[x]['entities']['hashtags'])  # append 'hashtags' into hashtageA8

hashtageA8b = []  # hold the 'text'
for x in range(len(hashtageA8)): # for loop
    h = hashtageA8[x]  # hashtageA8 equal to h
    for j in range(len(h)): # for loop
        hashtageA8b.append(h[j]['text'].lower()) # turn 'text' into lower case, then append it into 'hashtageA8b'

a8 = pd.Series(hashtageA8b).value_counts().sort_values(ascending = False) # turn 'hashtageA8b' into Series, then value_counts on it, sort the value from largest to smallest
a8.head(5) # print out the 5 most frequent hashtages, and the number of tweets that each appears in.

'''
A8.

gameofthrones           8366   # the 5 most frequent hashtages, and the number of tweets that each appears in.
got                     1032
forthethrone             219
gameofthronesseason8     124
demthrones               110
dtype: int64
'''

## A9.  Determine the 5 most frequent 'user_mentions', and the number of tweets 
##      that each appears in.  Give a table.

mentionsA9a = [] # hold the 'user_mentions'
for x in range(len(tweetlist)):   # for loops
    mentionsA9a.append(tweetlist[x]['entities']['user_mentions']) # append 'user_mentions' into mentionsA9a
mentionsA9b = []  # hold the 'screen_name'
for x in range(len(mentionsA9a)):  # for loops
    m = mentionsA9a[x] # mentionsA9a[x] equal 
    for j in range(len(m)): # for loops
        mentionsA9b.append(m[j]['screen_name']) # append the 'screen_name'
pd.Series(mentionsA9b).value_counts().sort_values(ascending = False).head(5)  # turn 'mentionsA9b' into series, value_counts on it, sort it from largest to smarest, then keep the top 5

'''
A9.

GameOfThrones    502  # the 5 most frenquent 'user_mentions' and the number of tweets that each appears in.
YgorFremo         82
GoTthings_        79
Complex           75
TPAIN             60
dtype: int64
'''



################################################################################
####
####  Section B
####
################################################################################


##  We will use the 'Stocks' data sets from Assignment 8 in this section.
##  You can see some information about the data in the assignment description.

##  The time interval covered varies from stock to stock. 
# There are some missing records, so the data is incomplete. 
# Note that some dates are not present because the exchange is closed on weekends and holidays. 
# Those are not missing records. 
# Dates outside the range reported for a given stock are also not missing records, 
# these are just considered to be unavailable. 
# Answer the questions below based on the data available in the files.

# 1) use 'Stocks' data sets from Assign 8
# 2) some missing records, so the data is incomplete. 
# 3) some dates are not present because the exchange is closed on weekends and holidays. Those are not missing records.
# 5) Dates outside the range reported for a given stock are also not missing records, just considered to be unavailable.
# 6) Answer the questions below based on the data available in the files.

filelist = glob.glob('*.csv') # 'glob.glob' is the directory search
# put all the file in one folder named "Stocks", then change directory to 'Stocks', '*.csv' selects files ending in '.csv', which is all the stock file
filelist
df = pd.DataFrame() #formed dataframe that will contain all data
for f in filelist:
    df2 = pd.read_csv(f) #imported each file and added a new column with their name
    df2['Name'] = f  
    df = pd.concat([df,df2]) #added the new files to the big dataframe
df['Date'] = pd.to_datetime(df['Date']) # turn 'Date' into datetime
df['Name'] = df['Name'].str.split('.').str[0]     # keep the name only
df['Year'] = df['Date'].dt.year  # year
df['Month'] = df['Date'].dt.month # month
df['Day'] = df['Date'].dt.day # day
df = df.reset_index(drop=True) # reset the index


## B1.  Use the collective data to 
# determine when the market was open from January 1, 2008 to December 31, 2015. 
# (Do not use external data for this question.) 
# Report the number of days the market was open for each year in 2008-2015. 
# Include the year and the number of days in table form.

# 1） from January 1, 2008 to December 31, 2015. 
# 2) Report the number of days the market was open for each year in 2008-2015.
# 3) Include the year and the number of days in table form.

stocksB1 = df[(df['Date'] <= '2015-12-31') & (df['Date'] >= '2008-01-01')].loc[:,'Date':'Volume'] # subset the day from January 1, 2008 to Dec 31, 2015
stocksB1['Year'] = stocksB1['Date'].dt.year  # create a new column 'Year', equal to  stocksB1['Date'].dt.year

listB1 = []  # new list hold the number of days
years = np.unique(stocksB1['Year'])  # unique years 
for i in range(len(years)):  # for loops
    x = stocksB1[stocksB1['Year'] == years[i]] # 
    x1 = len(x['Date'].unique())  # the number of days per year
    listB1.append(x1)  # add the number of days per year into listB1
B1 = pd.concat([pd.DataFrame(years), pd.DataFrame(listB1)], axis = 1)  # concate years and listB1 by column    
B1.columns = ['Year', 'number of days']     # change the name of the column
B1      # print out the answer

'''
B1.

   Year  number of days     # the answer, the number of days the market was open for each year in 2008-2015.
0  2008             253
1  2009             252
2  2010             252
3  2011             252
4  2012             250
5  2013             252
6  2014             252
7  2015             252
'''

## B2.  Determine the total number of missing records for all stocks for the 
##      period 2008-2015.

# 1) total number of missing records for all stocks
# 2) period 2008-2015

datesOpen = df['Date'].drop_duplicates()   # find the unique date
stocksList = df['Name'].unique()   # find the unique stock name, there is 291 stocks
dfMissing = pd.DataFrame(columns = ['Date', 'Stock'])  # rename the column

for i in stocksList:  # for loops
    dfB2a = df.loc[(df['Date'].dt.year >= 2008) & (df['Date'].dt.year <= 2015)]  # subset the data from 2008 to 2015
    dfB2a = dfB2a.loc[dfB2a['Name'] == i]  # subset the data with ['Name'] = i
    start = dfB2a['Date'].min()  # find the min of the idf['Date']
    end = dfB2a['Date'].max()    # find the max of the idf['Date']
    dateopenPer = datesOpen.loc[(datesOpen >= start) & (datesOpen <= end)]   # subset the start date to end date 
    missingDates = np.setdiff1d(dateopenPer, dfB2a['Date'])   # check the missing date
    missingDF = pd.DataFrame({'Date':missingDates, 'Stock': i})   # create a new data frame, with column 'Date' equal to missingDates, 'Stock' equal to i
    dfMissing = pd.concat([dfMissing, missingDF], ignore_index=True) # concate the column, ignore the index
dfMissing['Date'] = pd.to_datetime(dfMissing['Date'])  # change the 'Date' to datatime
B2 = len(dfMissing)  # the len of the data
B2  # print out the answer

'''
B2.

7163  # the number of missing records for all stocks for the period 2008 - 2015 is 7163.
'''

## B3.  For the period 2008-2015, find the 10 stocks (plus ties) that had the 
##      most missing records, and the 10 stocks (plus ties) with the fewest 
##      missing records. (For the latter, don’t include stocks that have no 
##      records for 2008-2015.) Report the stocks and the number of missing 
##      records for each.

dfB2 = df[(df['Year']>=2008) & (df['Year'] != 2016)]   # subset the data from period 2008 to 2015
NameB2 = df['Name'].unique()  # unique 'Name'

missing = []  # hold numebr of the missing record
Name = []   # hold the stock name
for i in NameB2:
    subset = dfB2[dfB2['Name']== i]  # subset the 
    first = subset['Date'].min()  # minimum of subset['Date']
    last = subset['Date'].max()   # max of subset['Date']
    stocksSub = dfB2[(dfB2['Date']>= first) & (dfB2['Date']<= last)]  # subset the data from first dat to last day
    days_stocks = stocksSub['Date'].unique()  # unique stocksSub['Date']
    days_ticker = subset['Date'].unique()  # unique subset['Date']
    missingNumber = len(days_stocks) - len(days_ticker)  # missing number of records
    missing.append(missingNumber)  # append the missingNumber in 'missing'
    Name.append(i)  # append the name into the stock

missingRecord = pd.DataFrame({'Name': Name, 'Number of Missing Records': missing})  # new data frame, which column 'Name' equal name, 'Number of Missing Records' equal missing 
lowest10 = missingRecord.sort_values(by = 'Number of Missing Records')[0:10] # sort the data by column 'Number of Missing Records' and keep the top 10
lowest10 # the answer, the 10 stocks with the fewest missign records.
highest10 = missingRecord.sort_values(by = 'Number of Missing Records', ascending=False)[0:12] # sort the record by columne 'Number of Missing Records', sort from largest to smallest, keep the top 12 due to ties
highest10  # the answer, the 12 stocks with the most missing records.

'''
B3.

    Name   Number of Missing Records   # the answer, the 12 stocks with the most missing records.
276   NBL                         44
247  HBAN                         37
148    RF                         37
269   BBT                         36
53   PDCO                         36
287   WAT                         36
226    LB                         36
125   SEE                         35
94    GAS                         34
101  VRSN                         34
213   RCL                         34
23    HOT                         34

     Name   Number of Missing Records   # the answer, the 10 stocks with the fewest missign records.
83     GM                          0
117   ZTS                          0
282   ADT                          0
138  TRIP                          0
4    NLSN                          0
151   XYL                          0
233   LYB                          0
153    FB                          0
258  NWSA                          0
39   NAVI                          0
'''


## B4.  Identify the top-10 dates (plus ties) in 2008-2015 that are missing 
##      from the most stocks.  Provide a table with dates and counts.

# 1) top 10 dates in 2008 - 2015 taht are missing from the most stocks
# 2) table with dates and counts

dfB4 = dfMissing.groupby(dfMissing['Date'])   # group dfMissing with column 'Date'
dfB4.count().sort_values(by='Stock', ascending=False).head(23)   # count the group 'dfB4', sort values by column 'Stock', sort from the largest to smallest, print out top 23

'''

B4.

Date        Stock        # the top 10 dates (plus ties) in 2008-2015 that are missing from the most stocks
2012-04-23     11
2011-03-08     10
2013-09-23     10
2013-01-30     10
2008-04-01      9
2013-11-05      9
2009-04-06      9
2008-06-10      9
2009-04-27      9
2010-07-21      9
2009-03-16      9
2012-04-24      9
2011-08-01      9
2013-04-30      9
2013-07-22      9
2009-08-13      9
2009-12-24      9
2008-04-03      9
2013-08-29      9
2012-06-25      9
2012-08-10      9
2009-06-11      9
2009-08-05      9
'''

##################################################################################

##  Questions B5 and B6: For each stock, impute (fill in) the missing records 
##  using linear interpolation. For instance, suppose d1 < d2 < d3 are dates,  
##  and P1 and P3 are known Open prices on dates d1 and d3, respectively, with
##  P2 missing.  Then we estimate P2 (the Open price on date d2) with
##
##        P2 = ((d3 - d2)*P1 + (d2 - d1)*P3)/(d3 - d1)
##
##  The same formula is used for the other missing values of High, Low, Close, 
##  and Volume.  Once you have added the missing records into your data, then
##  use the new data (including the imputed records) to calculate the Python 
##  Index for each date in 2008-2015 (see Assignment 8 for the formula). 
##  Remember that weekends and holidays are not missing records, so don't 
##  impute those.  Once you're done with that, then you can answer B5 and B6.


## B5.  Find the Open, High, Low, and Close for the imputed Python Index for 
##      each day the market was open in January 2013. Give a table the includes 
##      the Date, Open, High, Low, and Close, with one date per row.

def impute(d1, d2, d3, P1, P3):  # create a function
    dif1 = d3 - d2   # create a new variable which equal d3 - d2
    dif2 = d2 - d1   # create a new variable which equal d2 - d1
    dif3 = d3 - d1   # create a new variable which equal d3 - d1
    P2 = ((dif1/dif3)*P1 + (dif2/dif3)*P3) # fomula
    return P2      # return P2

dfMissing['Open'] = ''  # create a new empty column
dfMissing['High'] = ''  # create a new empty column
dfMissing['Low'] = ''   # create a new empty column
dfMissing['Close'] = '' # create a new empty column
dfMissing['Volume'] = '' # create a new empty column

for i in stocksList:    # for loop
    dfi = df.loc[df['Name'] == i]  # subset the data
    missingi = dfMissing.loc[dfMissing['Stock'] == i]  # missing data for one stock
    for date2 in missingi['Date']:   # for loops
        before = dfi.loc[dfi['Date'] < date2]['Date']  # date before missing date
        date1 = before.iloc[0] 
        after = dfi.loc[dfi['Date'] > date2]['Date']   # date after missing date
        date3 = after.iloc[len(after)-1]
        
        R1 = dfi.loc[dfi['Date'] == date1]     # date before missing date from the stock data
        R3 = dfi.loc[dfi['Date'] == date3]     # date after missing date in stock data
        open1 = float(R1['Open'])  # turn to float
        open3 = float(R3['Open']) # turn to float
        high1 = float(R1['High']) # turn to float
        high3 = float(R3['High']) # turn to float
        low1 = float(R1['Low']) # turn to float
        low3 = float(R3['Low']) # turn to float
        close1 = float(R1['Close']) # turn to float
        close3 = float(R3['Close']) # turn to float
        vol1 = float(R1['Volume']) # turn to float
        vol3 = float(R3['Volume']) # turn to float
        open2 = impute(date1, date2, date3, open1, open3)   # apply function 
        high2 = impute(date1, date2, date3, high1, high3)   # apply function 
        low2 = impute(date1, date2, date3, low1, low3)      # apply function 
        close2 = impute(date1, date2, date3, close1, close3)  # apply function 
        vol2 = impute(date1, date2, date3, vol1, vol3)      # apply function
        
        index = missingi.loc[missingi['Date'] == date2].index[0]  # define date index
        dfMissing.loc[index, 'Open'] = open2  # add imputed valuess
        dfMissing.loc[index, 'High'] = high2  # add imputed valuess
        dfMissing.loc[index , 'Low'] = low2   # add imputed valuess
        dfMissing.loc[index , 'Close'] = close2  # add imputed valuess
        dfMissing.loc[index , 'Volume'] = vol2  # add imputed valuess

dfbig = pd.concat([df, dfMissing], ignore_index=True, sort=False)  # concate the data, ignore index
dfbigA = dfbig.loc[(dfbig['Date'].dt.year >= 2008) & (dfbig['Date'].dt.year <= 2015)]   # subset the data from 2008 to 2015
dfbigA['OpenVolume'] = dfbigA['Open']*dfbigA['Volume']  # get the 'OpenVolume' 
dfbigA['HighVolume'] = dfbigA['High']*dfbigA['Volume']  # get the 'HighVolume'
dfbigA['LowVolume'] = dfbigA['Low']*dfbigA['Volume']  # get the 'LowVolume'
dfbigA['CloseVolume'] = dfbigA['Close']*dfbigA['Volume']  # get the 'CloseVolume'
newGroup = dfbigA.groupby(dfbigA['Date'])   # group

newDF = pd.DataFrame()  # The new dataframe
newDF['Open'] = newGroup['OpenVolume'].sum()/newGroup['Volume'].sum()   # compute the 'Open'
newDF['High'] = newGroup['HighVolume'].sum()/newGroup['Volume'].sum() # compute the 'High'
newDF['Low'] = newGroup['LowVolume'].sum()/newGroup['Volume'].sum()  # compute the 'Low'
newDF['Close'] = newGroup['CloseVolume'].sum()/newGroup['Volume'].sum()  # compute the 'Close'


## B5.  Find the Open, High, Low, and Close for the imputed Python Index for 
##      each day the market was open in January 2013. Give a table the includes 
##      the Date, Open, High, Low, and Close, with one date per row.

newDF['Date'] = newDF.index   # new column, date index
dfB5 = newDF[(newDF['Date'].dt.year == 2013) & (newDF['Date'].dt.month == 1)]  # January 2013 only
dfB5  # print out the answer

'''
B5.

Date             Open       High        Low      Close       Date           #   Find the Open, High, Low, and Close for the imputed Python Index for  each day the market was open in January 2013.                                       
2013-01-02  37.054761  37.505297  36.638862  37.228915 2013-01-02
2013-01-03  37.032179  37.523912  36.657750  37.081912 2013-01-03
2013-01-04  37.404633  37.863218  37.142403  37.636333 2013-01-04
2013-01-07  39.467304  39.985991  39.121514  39.630800 2013-01-07
2013-01-08  39.403554  39.748143  38.922081  39.354890 2013-01-08
2013-01-09  35.024724  35.401727  34.640686  35.003027 2013-01-09
2013-01-10  37.033616  37.421070  36.654474  37.189733 2013-01-10
2013-01-11  38.191304  38.514559  37.833823  38.247111 2013-01-11
2013-01-14  38.484674  38.900076  38.112640  38.526461 2013-01-14
2013-01-15  38.200333  38.754825  37.881484  38.366129 2013-01-15
2013-01-16  39.376960  39.755706  38.911310  39.371881 2013-01-16
2013-01-17  35.979870  36.329769  35.648391  35.974307 2013-01-17
2013-01-18  40.134305  40.504265  39.723440  40.230839 2013-01-18
2013-01-22  40.567323  41.068261  40.241281  40.851074 2013-01-22
2013-01-23  44.641020  45.344795  44.288949  44.994229 2013-01-23
2013-01-24  48.921170  49.827586  48.346726  49.279962 2013-01-24
2013-01-25  55.089956  58.565085  54.817362  57.965279 2013-01-25
2013-01-28  50.963814  51.568084  49.721003  50.138855 2013-01-28
2013-01-29  42.852754  43.719166  42.382627  43.346702 2013-01-29
2013-01-30  45.365733  45.742741  44.516468  44.955761 2013-01-30
2013-01-31  43.908594  44.645015  43.391417  44.108205 2013-01-31
'''

## B6.  Determine the mean Open, High, Low, and Close imputed Python index 
##      for each year in 2008-2015, and report that in a table that includes 
##      the year together with the corresponding Open, High, Low, and Close.

group6 = newDF.groupby(newDF['Date'].dt.year)     # group by year
group6Mean = group6.mean()  # mean of the group6
group6Mean  # print out the mean Open, High, Low, and Close imputed Python index for each year in 2008-2015

'''
# B6.

Date       Open       High        Low      Close       # print out the mean Open, High, Low, and Close imputed Python index for each year in 2008-2015
2008  39.380067  40.282598  38.369949  39.316860
2009  27.203915  27.762914  26.660808  27.236140
2010  35.487994  35.966539  34.998897  35.505608
2011  38.709006  39.251518  38.116169  38.681309
2012  37.258081  37.740394  36.806378  37.295120
2013  47.072033  47.616081  46.539772  47.096413
2014  58.266215  58.897633  57.604711  58.269364
2015  54.358924  54.988411  53.707369  54.354561
'''

##################################################################################
####
####  Section C
####
################################################################################

##  This section requires the creation of a number of graphs. 
# In addition to the code in your Python file, 
# you will also upload a PDF document (not Word!)
##  containing your graphs (be sure they are labeled clearly).  
# The data file you will use is “samplegrades.csv”.

# 1) creation of a number of graphs
# 2) also upload a PDFZ dpcument (containing your graphs) label clearly

pd.set_option('display.max_columns', 10) # Display 10 columns in console
dfc = pd.read_csv("samplegrades.csv")  # read in data

## C1.  Make a scatter plot of the “Math” SAT scores (x-axis) against the 
##      “Read” SAT scores (y-axis). Label the plot “Math vs Read” and label
##      the axes "Math" and "Read".

x = dfc['Math']  # subset 'Math' from dfc
y = dfc['Read']  # subset 'Read' from dfc
plt.scatter(x,y)  # creat scatter with x and y, color as blue
plt.title('Math vs Read')  # add title 
plt.xlabel('Math')  # add x label
plt.ylabel('Read')  # add y label
plt.show() # display the plot

## C2.  Make the same scatter plot as the previous problem, but this time 
##      color-code the points to indicate the “Sect” and choose different 
##      shapes to indicate the value of “Prev”.

# indicate the “Sect”
# shapes to indicate the value of “Prev”

color = pd.DataFrame({'Sect':['MW200','TR930','TR1230'],'Color':['red', 'purple', 'black']}) # creat a data frame which has column Sect and Color
shape = pd.DataFrame({'Prev':['Y', 'N'],'Shape':["^","v"]})  # create a data frame which has column of 'Prev' and 'Shape'
grades = dfc.merge(color)  # merge color into data frame 'dfc'
grades = grades.merge(shape)  # merge shape into data frame 'grades'

yes = grades[grades.Prev.str.contains('Y')]  # keep the data which grades.Prev contains 'Y'
no = grades[grades.Prev.str.contains('N')]  # keep the data which grades.Prev contians 'N'

x1 = yes['Math']   # subset 'Math' column from 'yes'
y1 = yes['Read']  #  subset 'Read' column from 'yes'
x2 = no['Math']  # subset 'Math' column from 'no'
y2 = no['Read'] # subset 'Read' column from 'no'
plt.title('Math vs Read')  # add title
plt.xlabel('Math')  # add x label
plt.ylabel('Read')  # add y label
plt.scatter(x1,y1,marker = 'v', c = yes['Color'])   # use marker 'v' with yes['Color']
plt.scatter(x2,y2,marker = '^', c = no['Color'])    # use marker '^' with no['Color']
plt.show() # display the plot


## C3.  Make a histogram of the values of “CourseAve”. Label the graph 
##      “Course Averages”.

c3 = dfc['CourseAve']   # subset the 'CourseAve' from 'dfc'
plt.xlabel('Course Average')  # add x label
plt.ylabel('Frequency')  # add y label
plt.hist(c3,edgecolor='black',bins=20)  # create histgram, set edge color as 'black', bins = 20
plt.title('Course Averages') # add title
plt.show()   # display the plot



## C4.  Make a histogram of the values of “Final” with color-coded portions 
##      indicating the whether the scored at least 75 on the Midterm. Give 
##      the graph appropriate labels.


finaldf = dfc['Final'] #final grades
above75 = finaldf[dfc.Midterm >= 75] #subset final grades by midterm >= 75
below75 = finaldf[dfc.Midterm < 75] #subset final grades by midterm < 75

plt.hist([above75, below75], color=['red', 'blue']) #plot with different colors 
plt.title('Final by Midterm Grade') #title 
plt.xlabel('Final: Red (Midterm >= 75), Blue (Midterm < 75)') #x label 
plt.ylabel('Frequency') #y label 
plt.show() # display the plot


## C5.  Make a bar chart of the counts for the different values of Year. 
##      Give the graph appropriate labels.

counts = dfc['Year'].value_counts()  # value_counts on 'Year'
styles = counts.index  # index on index 
plt.bar(styles, counts, color='green', edgecolor='black')
plt.xlabel("Year")  # add x label
plt.ylabel("Counts")  # add y label
plt.title("Count of Years")  # add title
plt.show() # display the plot

## C6.  Make side-by-side box-and-whisker plots for the ‘CourseAve” for each 
##      distinct “Sect”. Give the graph appropriate labels.

C6a = dfc['CourseAve']  # subset 'CourseAve' from dfc
C6b = dfc['Sect']  # subset 'CourseAve' from dfc
dfC6 = pd.concat([C6a,C6b],axis=1) # concate 'C6a' and 'C6b' by column
data1 = dfC6.loc[dfC6['Sect']=='MW200','CourseAve'] # subset the CourseAve of 'MW200'
data2 = dfC6.loc[dfC6['Sect']=='TR930','CourseAve'] # subset the CourseAve of 'TR930'
data3 = dfC6.loc[dfC6['Sect']=='TR1230','CourseAve'] # subset the CourseAve pf 'TR1230'
data = [data1, data2, data3]  # concate the data into one column
plt.boxplot(data, notch=None, sym='b^') # 'b^' = blue triangle
plt.xticks([1, 2, 3], ['MW200', 'TR930', 'TR1230']) # Specifies data group
plt.xlabel("Sect") # x label 
plt.ylabel("CourseAve") # y label
plt.title("CourseAve by Sect")  # assign title
plt.show()  # display the plot
