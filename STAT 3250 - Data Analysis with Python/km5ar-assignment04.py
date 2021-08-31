##
## File: assignment04.py (STAT 3250)
## Topic: Assignment 4
## name: KEYU CHEN - km5ar

import pandas as pd   # import pands
airline = pd.read_csv('airline_tweets.csv')    # import 'airline_tweets.csv' and rename it as 'airline'

##  This assignment requires the data file 'airline_tweets.csv'.  This file
##  contains records of over 14000 tweets and associated information related
##  to a number of airlines.  You should be able to read this file in using
##  the usual pandas methods.

##  Note: Questions 1-9 should be done without the use of loops.  
##        Questions 10-13 can be done with loops.

## 1.  Determine the number of tweets for each airline, indicated by the
##     name in the 'airline' column of the data set.  Give the airline 
##     name and number of tweets in table form.

group1 = airline['text'].groupby(airline['airline'])  # grouped 'text' and 'airline', named the group 'group1'
group1.count()    # calculate the number of tweets for each airline

'''
# 1

airline                         # the answer, the number of tweets for each airline
American          2759
JetBlue           2222
Southwest         2420
US Airways        2913
United            3822
Virgin America     504
Name: text, dtype: int64

'''

## 2.  For each airlines tweets, determine the percentage that are positive,
##     based on the classification in 'airline_sentiment'.  Give a table of
##     airline name and percentage, sorted from largest percentage to smallest.

a4 = airline[['airline_sentiment','airline']]      # create a newdata named 'a4' set with only 'airline_sentiment', 'airline'
a5 = a4.loc[a4['airline_sentiment'] == 'positive'] # create a newdata named 'a5' which is from a4, only keep 'airline_sentiment' == 'positive'
group5 = a5['airline_sentiment'].groupby(a5['airline'])  # group a5['airline_sentiment'] with [a5'airline']
positive = group5.count()   # count the group5 and name it positve
a2 = airline['airline'].value_counts().sort_index()    # total number of tweets
b2 = airline['airline'][airline['airline_sentiment']=='positive'].value_counts().sort_index()   # number of tweets that are positive
print(((b2/a2)*100).sort_values(ascending = False))  # number of tweets that are positive divided by the total number of tweets, sort by largest to smallest

'''
# 2

Virgin America    30.158730       # the answer, the percentage that are positive, from largest percentage to smallest
JetBlue           24.482448       
Southwest         23.553719
United            12.872841
American          12.178325
US Airways         9.234466
Name: airline, dtype: float64
'''

## 3.  List all user names (in the 'name' column) with at least 20 tweets
##     along with the number of tweets for each.  Give the results in table
##     form sorted from most to least.

a3 = airline['name'].value_counts()       # user name with the number of tweets
a3[a3 >= 20]     # user names with at least 20 tweets 

'''
# 3

JetBlueNews        63                   # the answer, user names with at least 20 tweets along with the number of tweets for each, from most to least
kbosspotter        32
_mhertz            29
otisday            28
throthra           27
rossj987           23
weezerandburnie    23
MeeestarCoke       22
GREATNESSEOA       22
scoobydoo9749      21
jasemccarty        20
'''

## 4.  Determine the percentage of tweets from users who have more than one
##     tweet in this data set.

name4 = airline['name'].value_counts() # user name with the numbner of tweets
answer = 100*len(name4[name4>1])/len(name4)    # 100 times (the number of user who have more than one tweet devided by the total number of number of user who tweets)
print(answer)   # print the answer

'''
# 4

38.955979742890534    # the answer, the percentage of tweets from users who have more than one tweet in this data set
'''

## 5.  Among the negative tweets, which five reasons are the most common?
##     Give the percentage of negative tweets with each of the five most 
##     common reasons.  Sort from most to least common.

a5 = airline[['airline_sentiment', 'negativereason']]   #subset 'sentiment', include the 'airline_sentiment' and 'negativereason'
a5Negative = a5.loc[a5['airline_sentiment'] == 'negative'] # subset the data with 'airline_sentiment' == negative
sentimentNegative = ((a5Negative['airline_sentiment'].groupby(a5Negative['negativereason'])).count()).sort_values(ascending=False)  #group 'airline_sentiment' with 'negativereason', count and sort from largest to s
list5 = 100*sentimentNegative/len(a5Negative)  # list of negative tweets with the percentage
print(list5[0:5])   # the answer, top 5 reason among the negative tweets, from most to least common


'''
# 5

negativereason                                        # the answer, top 5 reason among the negative tweets with percentage, from most to least common
Customer Service Issue    31.706254
Late Flight               18.141207
Can't Tell                12.965788
Cancelled Flight           9.228590
Lost Luggage               7.888429
Name: airline_sentiment, dtype: float64
'''

## 6.  How many of the tweets for each airline include the phrase "on fleek"?

airlineFleek = airline[airline['text'].str.contains('on fleek')]     # find out the data contains 'on fleek'
group6 = airlineFleek['text'].groupby(airlineFleek['airline'])     # group the [airlineFleek'text'] with [airlineFleek'airline']
group6.count()    # count for the numebr of tweets for each airline include the phrase 'on fleek'

'''
# 6

airline                       # the answer, tweets by airline include the phrase "on fleek"
JetBlue    146
Name: text, dtype: int64
'''

## 7.  What percentage of tweets included a hashtag?

tweet7 = airline['text'].str.count('#')    # count the number of hashtage in airline'text' and name it 'tweet'
tweet1= tweet7[tweet7 >=1 ]    # subset the tweet which included at least a hashtage
tweet2 = len(tweet1)            # the number of tweet which included at least a hashtage
print(tweet2/len(tweet7)*100)    # print out the answer, the percentage of tweets included a hashtag


'''
# 7

17.001366120218577   # the answer, the percentage of tweets including a hashtag
'''

## 8.  How many tweets include a link to a web site?

airlinelink = airline[airline['text'].str.contains('http')]     # the list of data contains 'http'
len(airlinelink)  # the length of the 'airlinelink' 
a8 = airline['text'].str.count('http')   # keep the data a website
print(len(a8[a8>=1]))   # the number of tweets include a link to a website

'''
# 8

1173   # the answer, the number of tweets include a link to a website
'''

## 9.  How many of the tweets include an '@' for another user besides the
##     intended airline?

tweetAt = airline['text'].str.count('@')     # count the numebr of '@' in text for each row
a9 = len(tweetAt[tweetAt >= 2])           # the number of tweets include equal or more than 2 '@'
print(a9)     # print out the answer, the number of the tweets include an '@' for another user besides the intended airline

'''
# 9

1645  # the answer, the number of the tweets include an '@' for another user besides the intended airline
'''

## 10. Suppose that a score of 1 is assigned to each positive tweet, 0 to
##     each neutral tweet, and -1 to each negative tweet.  Determine the
##     mean score for each airline, and give the results in table form with
##     airlines and mean scores, sorted from highest to lowest.

score = []   # holds for score
airlineSentiment = airline['airline_sentiment']  # subset, only sentiments
for t in airlineSentiment:  # for loops
    if t == 'positive':     # if positive, x =1
        x = 1
    elif t == 'neutral':     # if neutral, x = 0
        x = 0
    else:                    # else, x = -1
        x = -1
    score.append(x)       # add it into the score
airline['score'] = score   # add a new column to hold 'score'
scores = airline['score'].groupby(airline['airline'])  # group score by airline
scores.mean().sort_values(ascending = False)  # find the mean and sort it from highest to lowest

'''
# 10

airline                                   # the answer, the mean score for each airline, sorted from highest to lowest
Virgin America   -0.057540
JetBlue          -0.184968
Southwest        -0.254545
United           -0.560178
American         -0.588619
US Airways       -0.684518
Name: rating, dtype: float64
'''


## 11. Among the tweets that "@" a user besides the indicated airline, 
##     what percentage include an "@" directed at the other airlines 
##     in this file? (Note: Twitterusernames are not case sensitive, 

textMore1 = airline[airline['text'].str.count('@')>1]     # subset the airline['text'] with more than 1 "@"
text11 = airline[airline['text'].str.count('@')>1]  # list which has more than 1 '@' 
text11= airline['text'].str.lower()      # lowercase
ct = 0     # hold the count
for y in text11:   # for loop for 'text11'
    y = pd.Series(y.split())     # series and split the text
    i = pd.Series(['@virginamerica','@united','@southwestair','@jetblue','@usairways','@americanair']).isin(y)  # check if those @airlines isin data set 'y'
    if sum(i) >= 2:   # if the sum of i is equal or larger than 2 
        ct += 1  # add one to ct
print((ct/len(textMore1))*100)   # percentage, 1645 come from Q9

'''
# 11

18.72340425531915  the answer, among the tweets that "@" a user besides the indicated airline, 18.72340425531915% incldue an "@" directed at the other airlines in thise file
'''

## 12. Suppose the same user has two or more tweets in a row, based on how they 
##     appear in the file. For such tweet sequences, determine the percentage
##     for which the most recent tweet (which comes nearest the top of the
##     file) is a positive tweet.

positive = 0  # hold the count for the positive airline sentiment
a12 = 0  # hold the count if airline['name'][i] == airline['name'][i+1] != airline['name'][i-1] condition is met
for i in range(14639):   # for loop
    if airline['name'][i] == airline['name'][i+1] != airline['name'][i-1]: # airline['name'][i] equal one after not equal before
        a12 += 1   # if the condition is met, add total for 1
        if airline['airline_sentiment'][i] == 'positive':  # positive sentiment
            positive += 1   # add to positive
print(positive/a12*100)   # the answer, the percentage

'''
# 12

11.189634864546525   # the answer, percentage for for which the most recent tweet (which comes nearest the top of the file) is a positive tweet is 11.189634864546525%
'''

## 13. Give a count for the top-10 hashtags (and ties) in terms of the number 
##     of times each appears.  Give the hashtags and counts in a table
##     sorted from most frequent to least frequent.  (Note: Twitter hashtags
##     are not case sensitive, so '#HashTag', '#HASHtag' and '#hashtag' are
##     all regarded as the same. Also ignore instances of hashtags that are
##     alone with no other characters.)

hashtags13 = []    # created a new array
for x in airline['text']:   # create a loop
    if x.count('#') > 0:    # if there is a hashtag
        a13 = pd.Series(x.split())  # create a new series
        tags = list(a13[a13.str.contains('#')])  # newlist which only contains '#'
        hashtags13 = hashtags13 + tags  # add tags to hashtags
hashtags13 = pd.Series(hashtags13).str.lower()   # convert list to series, and lowercased
answer13 = pd.Series(hashtags13).value_counts()     #count the hastags
print(answer13[1:11])   # print the top 10 hastags

'''
# 13

#destinationdragons    76      # the answer, top-10 hashtags in terms of the number of times each appears
#fail                  64
#jetblue               44
#unitedairlines        43
#customerservice       34
#usairways             30
#usairwaysfail         26
#neveragain            26
#americanairlines      25
#united                25
'''





