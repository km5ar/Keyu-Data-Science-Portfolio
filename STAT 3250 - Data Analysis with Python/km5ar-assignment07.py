
##
## File: assignment07.py (STAT 3250)
## Topic: Assignment 7 
##  name: keyu chen - km5ar

##  This assignment requires data from four files: 
##
##      'movies.txt':  A file of over 3900 movies
##      'users.dat':   A file of over 6000 reviewers who provided ratings
##      'ratings.dat': A file of over 1,000,000 movie ratings
##      'zips.txt':    A file of zip codes and location information
##
##  The file 'readme.txt' has more information about the first three files.
##  You will need to consult the readme file to answer some of the questions.

##  Note: 
## You will need to convert the zip code information in 
## 'users.dat' into state (or territory) information 
##  for one or more of the questions below.
##  You must use the information in 'zips.txt' for this purpose, you cannot
##  use other conversion methods. 

import numpy as np
import pandas as pd

user = open('users.dat').read().splitlines()   # import user.data
userS = pd.Series(user)   # turn it into series 

rating = open('ratings.dat').read().splitlines()  # import 'rating.dat'
ratingS = pd.Series(rating)   # turn it into series

movie = open('movies.txt').read().splitlines()  # import movies.text
movieS = pd.Series(movie)  # turn it into series

zips = open('zipcodes.txt').read().splitlines()  # import zipcode.text
zipS = pd.Series(zips)   # turn it into series

zips1 = pd.read_csv('zipcodes.txt',   # another way import zipcode, only keep 1 and 4 column
                  usecols = [1,4],
                  converters={'Zipcode':str})
zips12 = zips1.drop_duplicates()  # drop the duplicates

## 1.  Determine the percentage of users that are female.  Do the same for the
##     percentage of users in the 35-44 age group.  In the 18-24 age group,
##     determine the percentage of male users.

userGender = userS.str.split('::').str[1]  # gender only
sum(userGender.str.contains('F'))/len(userS)*100 # percentage of user are female

userAge = userS.str.split('::').str[2]   # user age
numberUser35to44 = userAge[userAge.str.contains('35')]  # 35 age group in all user
len(numberUser35to44)/len(userS)*100    # age group 35-44

# 18-24 are group, the percentage of male user
male = userS[userS.str.contains('M')]   # subset the data which contains male only
maleAge = male.str.split('::').str[2]   # male age data
male18to24 = maleAge[maleAge.str.contains('18')]  # 18-24 under maleage
numberUser18to24 = userAge[userAge.str.contains('18')] # 18-24 under all user 
len(male18to24)/len(numberUser18to24)*100   # male out of age group 18-24

'''
1,

28.294701986754966    # Female
19.751655629139073    # age group 35-44
72.98277425203989     # male out of agegroup 18-24
'''

## 2.  Give a year-by-year table of counts for the number of ratings, sorted by
##     year in ascending order.

ratingColumn = ratingS.str.split('::').str[-2]   # rating from ratings
timeColumn = ratingS.str.split('::').str[-1].astype(float)  # timestamp
timeColumn1 = pd.to_datetime(timeColumn, unit='s')  # covert to year

list = []   # new list 
for i in range (len(timeColumn1)):   # for loop
    x = timeColumn1[i].year     # change to year
    list.append(x)   # append it into list
list1 = pd.DataFrame(list)  # turn it into a data frame

df2 = pd.concat([ratingColumn,list1],axis=1)  # concat the ratingcolumn and list1 together
df2.columns = ['rating','year']  # rename the column
df2a = df2['rating'].groupby(df2['year'])  # rating groupby year
df2a.count()  # count the number of ratings

'''
2.

year                      # the number of ratings per year
2000    904757
2001     68058
2002     24046
2003      3348
Name: rating, dtype: int64
'''

## 3.  Determine the average rating for females and the average rating for 
##     males.

female3 = userS[userS.str.contains('F')]  # female
female3Id = female3.str.split('::').str[0]  # userID
female3Id1 = pd.DataFrame(female3Id)  # turn it into dataframe  
female3Id1.columns = ['userID']   # rename the column

male3 =userS[userS.str.contains('M')]  # male
male3Id = male3.str.split('::').str[0]  # user ID
male3Id1 = pd.DataFrame(male3Id) # turn it into data frame
male3Id1.columns = ['userID']  # rename the column

userID = ratingS.str.split('::').str[0]   # user ID from rating file
rating3 = ratingS.str.split('::').str[2].astype(float)   # rating from rating file
df3 = pd.concat([userID,rating3],axis=1)  # concate userID and rating3 by column
df3.columns = ['userID','rating']  # rename the column
df3a = pd.merge(df3,female3Id1)  # merge the df3 and female3Id1
df3a.mean()  # for female, mean
df3b = pd.merge(df3,male3Id1)  # merge df3, male#Id1
df3b.mean()  # for male, mean

'''
3.

gender    AverageR   # the answer             
F         3.620366   # for female, the average rating 
M         3.568879   # for male, the average rating 
dtype: float64
'''

## 4.  Find the top-10 movies based on average rating.  (Movies and remakes 
##     should be considered different.)  Give a table with the movie title
##     (including the year) and the average rating, sorted by rating from
##     highest to lowest.  (Include ties as needed.)

MovieID = ratingS.str.split('::').str[1]  #MovieID from rating file
df4 = pd.concat([rating3,MovieID],axis=1)  # concat rating3 and movieID by column
df4.columns = ['rating','MovieID']   # rename the column
movieTitle = movieS.str.split('::').str[1]  # moviesID 
movieIDb = movieS.str.split('::').str[0] # movieID from file movies file
df4movies = pd.concat([movieTitle,movieIDb],axis=1) # concate moviesTitle and MoviesIDb
df4movies.columns = ['movieTitle','MovieID'] # rename the columns
merge4 = pd.merge(df4,df4movies) # merge df4 and df4movies
group4 = merge4['rating'].groupby(merge4['movieTitle'])  # group rating by movieTitle
group4.mean().sort_values(ascending=False).head(10) # top-10 movies based on average rating, sort from high to low

'''
4,

movieTitle                                          # the answer, top-10 movies based on average rating, sort from high to low
Gate of Heavenly Peace, The (1995)           5.0
Lured (1947)                                 5.0
Ulysses (Ulisse) (1954)                      5.0
Smashing Time (1967)                         5.0
Follow the Bitch (1998)                      5.0
Song of Freedom (1936)                       5.0
Bittersweet Motel (2000)                     5.0
Baby, The (1973)                             5.0
One Little Indian (1973)                     5.0
Schlafes Bruder (Brother of Sleep) (1995)    5.0
Name: rating, dtype: float64
'''

## 5.  Determine the number of movies listed in 'movies.txt' for which there
##     is no rating.  Determine the percentage of these unrated movies for
##     which there is a more recent remake.

movieIDM = pd.DataFrame(movieS.str.split('::').str[0])  # moviesID and turn it into a data frame
IDM = np.array(np.unique(movieIDM)) #array of movie IDs (movies)
movieID_ratings = pd.DataFrame(ratingS.str.split('::').str[1]) #movie IDs
IDs_ratings = np.array(np.unique(movieID_ratings)) #array of movie IDs (ratings)
un = np.setdiff1d(IDM, IDs_ratings)  # setdiff IDM with IDS_ratings
len(un)  # question1, the number of movie without rating

movieIDM.columns = ['IDnumber1'] #change the column name
un = pd.DataFrame(un) # unrat movies df
un.columns = ['IDnumber2'] #column name
unmovie = movieS[movieIDM.IDnumber1.isin(un.IDnumber2)]  # find unrate movie
unmovie = pd.Series(unmovie)  # turn it into series
unmovieT = unmovie.str.split('::').str[1] # keep titles and years 
unmovieT = unmovieT.str[:-7] # titles only
remake = movieS[-movieIDM.IDnumber1.isin(un.IDnumber2)] # remakes(maybe)

remake = pd.Series(remake ) # turn it into  series 
remakeT = remake.str.split('::').str[1] #keep titles and years
remakeT = remakeT.str[:-7] #titls
sum(unmovieT.isin(remakeT))/len(unmovieT)*100 # percentage of unrated movies for which there is a more recent remake


'''
5.

177    # the number of unrated movies

0.0    # the percentage of these unrated movies for which there is a more recent remake
'''


## 6.  Determine the average rating for each occupation classification 
##     (including 'other or not specified'), and give the results in a
##     table sorted from highest to lowest average and including the
##     occupation title.

userOccupation = userS.str.split('::').str[3]  # user file/ occupation
userID6 = userS.str.split('::').str[0]  # user file/ userID
df5a = pd.concat([userOccupation,userID6],axis=1)  # concate userOccupation and userID6
df5a.columns = ['userOccupation','userID']  # rename the columns
userID6b = ratingS.str.split('::').str[0]  # userID from rating file
df5b = pd.concat([rating3,userID6b],axis=1) # user ID and rating from ratings file
df5b.columns = ['rating','userID']  # rename the column
merge6 = pd.merge(df5a,df5b)   # merge df5a and df5b
df6c = pd.DataFrame({'userOccupation':['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'],
                    'occupationTitle':['other or not specified','academic/educator','artist','clerical/admin','college/grad student',
                                       'customer service','doctor/health care','executive/managerial','farmer','homemaker',
                                       'K-12 student','lawyer','programmer','retired','sales/marketing','scientist','self-employed',
                                       'technician/engineer','tradesman/craftsman','unemployed','writer']})
merge6a = pd.merge(merge6,df6c)  # merge the 'merge6' and df6c
group7 = merge6a['rating'].groupby([merge6a['userOccupation'],merge6a['occupationTitle']])  # group 'rating' by 'userOccupation' and 'occupationTitle'
group7.mean().sort_values(ascending=False)  # mean and sort from highest to lowerest

'''
6.

userOccupation  occupationTitle                     # the answer, average rating for each occupation classification  
13              retired                   3.781736
15              scientist                 3.689774
6               doctor/health care        3.661578
9               homemaker                 3.656589
3               clerical/admin            3.656516
12              programmer                3.654001
14              sales/marketing           3.618481
11              lawyer                    3.617371
17              technician/engineer       3.613574
7               executive/managerial      3.599772
16              self-employed             3.596575
1               academic/educator         3.576642
2               artist                    3.573081
0               other or not specified    3.537544
5               customer service          3.537529
4               college/grad student      3.536793
10              K-12 student              3.532675
18              tradesman/craftsman       3.530117
20              writer                    3.497392
8               farmer                    3.466741
19              unemployed                3.414050
Name: rating, dtype: float64
'''


## 7.  Determine the average rating for each genre, and give the results in
##     a table listing genre and average rating in descending order.

df7a = pd.concat([MovieID,rating3],axis=1)  # concate movieID and rating3 by column
df7a.columns = ['movieID','rating']  # rename  the column
genre = movieS.str.split('::').str[2]  # genre from movies
df7b = pd.concat([genre,movieIDb],axis=1)  # concate genre and moviesIDb by column
df7b.columns = ['genre','movieID']  # rename the column
merge7 = pd.merge(df7a,df7b)   # merge df7a and df7b

movieIDM = pd.DataFrame(movieS.str.split('::').str[0])  # movieID
genres = pd.DataFrame(movieS.str.split('::').str[-1])  # subset the genre
movieIDgenre = pd.concat([movieIDM, genres], axis=1)  # concate movieIDM and genres by column
movieIDgenre.columns = ['MovieID', 'genres']   # rename the column
df7 = pd.merge(df4, movieIDgenre, on='MovieID')  # merge the df4 and movieIDgenre
genreD = df7.genres.str.get_dummies('|')  # create dummy variable
df7 = pd.concat([df7, genreD], axis = 1)  # concate df7 and genreD by column
L7 = ['Action', 'Adventure', 'Animation', "Children's",'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical','Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']  
list7 = []  # create a empty list 
for i in range(len(L7)):   # for loop, set the range
    genre = df7[df7[L7[i]] == 1]   #  if L[i] = 1, if movie has genre
    average_rating = genre['rating'].mean()  # mean of the rating
    list7.append(average_rating)    # add it into the L7
data = {'Genre': L7,'Average Rating':list7}         # create a data frame
df7c = pd.DataFrame(data, columns=['Genre','Average Rating'])   # rename column
df7c.sort_values(ascending = False, by='Average Rating')  # sort average rating,in descending order

'''
7.
               
          Genre  Average Rating     # sort average rating,in descending order
9     Film-Noir        4.075188
6   Documentary        3.933123
16          War        3.893327
7         Drama        3.766332
5         Crime        3.708679
2     Animation        3.684868
12      Mystery        3.668102
11      Musical        3.665519
17      Western        3.637770
13      Romance        3.607465
15     Thriller        3.570466
4        Comedy        3.522099
0        Action        3.491185
1     Adventure        3.477257
14       Sci-Fi        3.466521
8       Fantasy        3.447371
3    Children's        3.422035
10       Horror        3.215013
'''

## 8.  For the user age category, assume that the user has age at the midpoint
##     of the given range.  (For instance '35-44' has age (35+44)/2 = 39.5)
##     For 'under 18' assume an age of 16, and for '56+' assume an age of 60.
##     For each possible rating (1-5) determine the average age of the raters.

def ageF(x):   #define age function 
    if x == 1:   # if x is in age gourp of 1
        return(16)   # return 16
    elif x == 18:  # if x is in age gourp of18
        return((18+24)/2)   # return
    elif x == 25:  # if x is in age gourp of 25
        return((25+34)/2)   # return
    elif x == 35: # if x is in age gourp of 35
        return((35+44)/2)   # return
    elif x == 45:  # if x is in age gourp of 40
        return((45+49)/2)   # return
    elif x == 50: # if x is in age gourp of 50
        return((50+55)/2)   # return
    elif x == 56: # if x is in age gourp of 56
        return(60)         # return
age = userS.str.split('::').str[2]   # age only
age = pd.DataFrame(age.astype(int))  # turn it into interger than dataframe
age.columns = ['age']   # change the name of column
ageF1 = age['age'].apply(ageF)   # apply the function on the age['age']
useruser8 = pd.DataFrame(userS.str.split('::').str[0])   # subset the userID
uages8 = pd.concat([useruser8, ageF1], axis=1)  # concate useruser8 and ageF1
uages8.columns = ['userID', 'ages']  # change the column name
df8 = pd.merge(uages8, df3, on='userID') #merge uages8 with ratings by column 'userID'
group8 = df8['ages'].groupby([df8['rating']]) # 'ages' grouped by 'ratings' 
group8.mean() #mean of the group8
'''
8.

rating            # the answer, the average age of the each possible rating
1.0    31.710783
2.0    32.769485
3.0    33.840672
4.0    34.270909
5.0    34.368274
Name: ages, dtype: float64
'''

## 9.  Find all combinations (if there are any) of occupation and genre for 
##     which there are no ratings.  

IDR = pd.DataFrame(ratingS.str.split('::').str[0]) #userIDs
IDR.columns = ['userID']   # column name
df9 = pd.concat([df7, IDR], axis=1)    # concate df7 and IDR
dfLoop = pd.merge(df9, df5a, on='userID')  # merge df9 and df5a by column 'userID'
counts_df = pd.DataFrame()   #create a empty df 
for i in range(len(L7)):   #set the range as L7
    genre = dfLoop[dfLoop[L7[i]] == 1]   # if movie has specific genre 
    grouping = genre[L7[i]].groupby([genre['userOccupation']]) #group by occupation
    occupation = grouping.value_counts()   # find value counts 
    occupation = pd.DataFrame(occupation)  # turn it into data frame 
    counts_df = pd.concat([counts_df, occupation], axis=1) #add to data frame
data9 = counts_df[counts_df.isnull().any(axis=1)] # check rows and columns of NA values
data9['non'] = data9.apply(lambda x: ','.join(x[x.isnull()].index),axis=1)  # subset the data which don't have a value
data9['non']  # print out the answer, all combination of ccupation and genre for which there are no ratings

'''

9.

13  1                              Documentary    # the answer, 7 combinations of genre-occupation with no ratings
19  1                                Film-Noir
8   1    Documentary,Film-Noir,Musical,Western
9   1                                  Mystery
Name: new, dtype: object
'''
## 10. For each age group, determine the occupation that gave the lowest 
##     average rating.  Give a table that includes the age group, occupation,
##     and average rating.  (Sort by age group from youngest to oldest) 

userAge1 = userAge.replace(['1'], 'Under 18')  # replace Under 18 for 1 
userAge2 = userAge1.replace(['18'], '18-24')   # replace 18-24 for 18
userAge3 = userAge2.replace(['25'], '25-34')   # replace 25-34 for 25
userAge4 = userAge3.replace(['35'], '35-44')   # replace 35-44 for 35
userAge5 = userAge4.replace(['45'], '45-49')   # replace 45-49 for 45
userAge6 = userAge5.replace(['50'], '50-55')   # replace 50-55 for 50
userAge7 = userAge6.replace(['60'], '56+')     # replace 56+ for 60
df10 = pd.concat([userID6,userAge],axis=1)  # concate userID and 
df10.columns = ['userID','midpointAge']   # rename the columns
df10a = pd.concat([userID6,userAge7,userOccupation],axis=1)  # userID(userID from users file),userOccupation(occupation from users file)
df10a.columns = ['userID','ageGroup','occupation']  # rename the column
df10b = pd.concat([userID,rating3],axis=1) # userID(user ID from rating file), rating3(rating from rating file)
df10b.columns = ['userID','rating'] # rename the column
merge10 = pd.merge(df10a,df10b)  # merge df10a and df10b
group10 = merge10['rating'].groupby([merge10['ageGroup'],merge10['occupation']])  # group 'rating' by 'ageGroup' and 'occupation'
group10.mean().groupby(level=0,group_keys=False).nsmallest(1)  # the answer, the loweest average rating for each age group

'''
10.

ageGroup  occupation                         # the loweest average rating for each age group
Under 18  11            3.066667
18-24     6             3.235525
25-34     19            3.366426
35-44     8             2.642045
45-49     4             3.280000
50-55     8             3.437610
56        14            3.291755
Name: rating, dtype: float64
'''

## 11. Find the top-5 states in terms of average rating.  Give in table form
##     including the state and average rating, sorted from highest to lowest.
##     Note: If any of the zip codes in 'users.dat' includes letters, then we
##     classify that user as being from Canada, which we treat as a state for
##     this and the next question.

zipcode11 = userS.str.split('::').str[-1]   # zip-code from users file
zipcode112 = zipcode11.str.split('-').str[0] # strip off last two number keep the first 5
df11a = pd.concat([userID6,zipcode112],axis=1) # userID6(userID from user file)
df11a.columns = ['userID','zipcode']  # rename the columns
rating11 = ratingS.str.split('::').str[2]     # rating from rating file 
df11b = pd.concat([userID,rating3],axis=1) # concat userid and rating3, userID(userID from rating), rating3(rating from rating file )
df11b.columns = ['userID','rating']   # rename the column
df11c = pd.merge(df11a,df11b)  # merge df11a and df11b
zipS1 = zipS.str.split(',').str[4].str.split('"').str[1]  # state from zipcode file
zipS1a =zipS.str.split(',').str[1].str.split('"').str[1]  # zipcode from zipcode file
zipS1a = zipS1a.str.split('-').str[0]  # zipcode
df11d = pd.concat([zipS1,zipS1a],axis=1)  # concat zipS1 and zipS1a
df11d.columns = ['state','zipcode']   # renmae the columns
df11c.columns = ['userID','Zipcode','rating']  # rename the columns
df11e = pd.merge(df11c,zips12)  # merge df11c and zips12
df11f = df11e['rating'].groupby(df11e['State'])  # group rating by 'State'
df11f.mean().sort_values(ascending=False).head(5)  # top 5 states in terms of average rating, sort from highest to lowest


'''
11.

State                     # the answer,  the top-5 states in terms of average rating.
GU    4.236842
MS    3.996409
AK    3.985730
AP    3.938967
SC    3.807748
Name: rating, dtype: float64

'''

## 12. For each genre, determine which state produced the most reviews.  
##     (Include any ties.)

zipUser = userS.str.split('::').str[-1] #zipcodes 
zipUser = pd.DataFrame(zipUser.str.split('-').str[0])  # drop the digits after - , if they have
IDuser = pd.DataFrame(userS.str.split('::').str[0]) #user ID only
IDzipcode = pd.concat([IDuser, zipUser], axis=1) #concat with userID
IDzipcode.columns = ['userID', 'Zipcode']   # change the column name
usersss = pd.merge(IDzipcode, zips1, on='Zipcode')   # merge IDzipcode and zips1 by column 'Zipcode'
df12 = pd.merge(df9, usersss, on='userID')   # merge df9 and usersss by column userID

counts2 = pd.DataFrame()   # create a df 
holdlargest = pd.DataFrame() # create a df
for i in range(len(L7)):   #range of L7
    genre2 = df12[df12[L7[i]] == 1]   #if movie has specific genre 
    grouping2 = genre2[L7[i]].groupby([genre2['State']]) # group by 'State'
    state_counts = grouping2.value_counts() # find value counts of the grouping2 
    state_counts2 = pd.DataFrame(state_counts) # turn state_counts into data frame 
    counts2 = pd.concat([counts2, state_counts2], axis=0) # concate counts2 and state_counts2
    n_largest = counts2[L7[i]].nlargest(1) #take state with largest value per genre
    holdlargest = pd.concat([holdlargest, n_largest], axis=0) #add to df 'holdlargest'
holdlargest['Genre']= L7 #add genre's names to df 
holdlargest #answer, For each genre, state produced the most reviews.

'''
12.

Genres       State          # answer, For each genre, state produced the most reviews.
Action       CA       46705
Adventure    CA       24018
Animation    CA        7880
Children's   CA       12506
Comedy       CA       62619
Crime        CA       14556
Documentary  CA        1669
Drama        CA       65710
Fantasy      CA        6358
Film-Noir    CA        3645
Horror       CA       12893
Musical      CA        7513
Mystery      CA        7515
Romance      CA       27031
Sci-Fi       CA       28755
Thriller     CA       34431
War          CA       12436
Western      CA        3737
Name: Ratings, dtype: int64
'''


