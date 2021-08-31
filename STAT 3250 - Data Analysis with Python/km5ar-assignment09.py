##
## File: assignment09.py (STAT 3250)
## Topic: Assignment 9 
## name: keyu chen - km5ar

##  This assignment requires data from the file 
##
##      'ncaa.csv':  NCAA Men's Tournament Scores, 1985-2019
##
##  The organization of the file is fairly clear.  Each record has information
##  about one game, including the year, the teams, the final score, and each 
##  team's tournament seed.  All questions refer only to the data in this
##  file, not to earlier tournaments.

import numpy as np
import pandas as pd

df = pd.read_csv('ncaa.csv')

##  Note: The data set is from Data.World, with the addition of the 2019
##  tournament provided by your dedicated instructor.


## 1.  Find all schools that have won the championship, 
# and make a table that incluldes 
# the school 
# and number of championships, 
# sorted from most to least.

df['winner'] = np.where(df['Score'] > df['Score.1'], df['Team'], df['Team.1'])   # when Score larger than Score.1, print out 'Team', if Score smarller then Score.1, print 'Team.1'
Champ = df.loc[(df['Region Name'] == 'Championship')]   # keep the data with school 
Champ['winner'].value_counts()      # value count on 'winner'
'''
1. 

Duke              5
North Carolina    4
Connecticut       4
Kentucky          3
Villanova         3
Florida           2
Louisville        2
Kansas            2
Virginia          1
Arkansas          1
Arizona           1
Maryland          1
Michigan St       1
Indiana           1
Syracuse          1
UNLV              1
Michigan          1
UCLA              1
Name: school, dtype: int64

'''

## 2.  Find the top-10 schools based on number of tournament appearances.
##     Make a table that incldes the school name and number of appearances,
##     sorted from most to least.  Include all that tie for 10th position
##     if necessary.

df2 = df[df['Round'] == 1]    # only look at the 'Round' == 1 
df2a = pd.concat([df2['Team'],df2['Team.1']],axis= 0)  # concate 'Team' and 'Team.1' based on rows not column
df2a.value_counts().head(11)   # bc there is is a tie, so use head(11)

'''
2. 

Duke              34
Kansas            34
Arizona           32
North Carolina    32
Kentucky          30
Michigan St       29
Syracuse          28
Purdue            26
Louisville        26
Texas             26
Oklahoma          26
dtype: int64
'''

## 3.  Determine the average tournament seed for each school, 
# then make a table with the 10 schools 
# that have the lowest average (hence the best teams). 
# Sort the table from smallest to largest, 
# and include all that tie for 10th position if necessary.

df3 = pd.concat([df2['Seed'],df2['Seed.1']],axis= 0)  # concat 'Seed' and 'Seed.1' based on row not column  
df3a = pd.concat([df2a,df3],axis=1)   # concate 'df2a' 'df3'on column 
df3a.columns = ['School','Seed']      # rename the columns
SeedTeam = df3a['Seed'].groupby(df3a['School'])   # group 'Seed' with 'School'
SeedTeam.mean().sort_values().head(10)  # mean of SeedTeam, then sort the value, and keep the top 10 lowest average 


'''
3.

School                          # the answer, the 10 schools that have the lowest average
Duke               2.176471
Kansas             2.500000
North Carolina     2.718750
Kentucky           3.566667
Connecticut        3.950000
Loyola Illinois    4.000000
Massachusetts      4.375000
Syracuse           4.428571
Arizona            4.437500
Ohio St            4.450000
Name: Seed, dtype: float64

'''



## 4.  Give a table of the average margin of victory by round, sorted by
##     round in order 1, 2, ....

df['margin']= abs(df['Score'] - df['Score.1']) # create a new column 'margin', which is the absolute value of ('Score'-'Score.1')
group4 = df['margin'].groupby(df['Round'])   # group 'margin' with 'Round'
group4.mean()  # the answer, the average margin of victory by round

'''
4.

Round               # the answer, the average margin of victory by round
1    12.956250
2    11.275000
3     9.917857
4     9.707143
5     9.485714
6     8.257143
Name: margin, dtype: float64
'''

## 5.  Give a table of 
# the percentage of wins 
# by the higher seed by round,
# sorted by round in order 1, 2, 3, ...

df['seed'] = np.where(df['Seed'] < df['Seed.1'], df['Team'], df['Team.1'])  # if 'Seed' smaller than 'Seed.1', print team, if larger, prince team.1 
df['higherSeed'] = np.where(df['seed'] == df['winner'], True, False)  # keep if 'seed' == 'winner', print True, if not, False
group5 = df['higherSeed'].groupby(df['Round']) # group higherSeed with Round
group5.mean()*100     # then calculate the mean of the group5 and times 100 get the percentage

'''
5.

Round                  # the answer, the percentage of wins by the higher seed by round
1    74.285714
2    71.250000
3    71.428571
4    55.000000
5    61.428571
6    71.428571
Name: higherseed, dtype: float64
'''



## 6.  Determine the average seed for all teams in the Final Four for each
##     year.  Give a table of the top-5 in terms of the lowest average seed
##     (hence teams thought to be better) that includes the year and the
##     average, sorted from smallest to largest.

f = df.loc[(df['Region Name'] == 'Final Four')]  # Region Name
f1 = f[['Seed','Seed.1']].groupby(f['Year']).sum()   # group 'Seed' and 'Seed.1' with 'Year' then do the sum
f1['averageSeed'] = (f1['Seed']+f1['Seed.1'])/4   # bc it is final four, so (Seed + Seed.1)/4
f2 = f1.sort_values(by = 'averageSeed').head(8)   # sort values based on average seed, becasue there is a tie, print out head(8)
f2['averageSeed']   # the answer, keep the average seed and year only

'''
6.

Year           # the answer, top-5 in terms of the lowest average seed in the Final Four (top 8 due to the tie)
2008    1.00
1993    1.25
2007    1.50
2001    1.75
1999    1.75
1997    1.75
1991    1.75
2009    1.75
Name: avg seed, dtype: float64
'''
## 7.  For the first round, determine the percentage of wins by the higher
##     seed for the 1-16 games, for the 2-15 games, ..., for the 8-9 games.
##     Give a table of the above groupings and the percentage, sorted
##     in the order given.

df2['games'] = np.where(df2['Score'] > df2['Score.1'], True, False)   # creat a new columns, if Score larger than Score.1, print True, if smaller, False
def games(x):                       # create a function
    if x == 1: # when x equal to 1
        return('1-16') # return '1-16'
    elif x == 2:  # when x equal to 2
        return('2-15')  # return '2-15'
    elif x == 3: # when x equal to 3
        return('3-14')  # return 3-14
    elif x == 4:    # when x equal to 4
        return('4-13') # return 4-13
    elif x == 5:   # when x equal to 5
        return('5-12') # return '5-12'
    elif x == 6: # when x equal 6
        return('6-11')   # retrun '6-11'
    elif x == 7:   # when x equal to 7
        return('7-10')  # return '7-10'
    elif x == 8:  # when x equal to 8
        return('8-9')    # return '8-9'
df2['round'] = df2['Seed'].apply(games)     # created a new column, which equal apply function on 'Seed'
group7= df2['games'].groupby(df2['round'])  # group 'games' with 'round'
group7.mean()*100   # calculate the mean and times 100 to get the percentage of wins  by the higher seed for the 1-16 games .


'''
7.

round                     # the answer, for first round, percentage of wins by the higher seed for the 1-16 games .....
1-16    99.285714
2-15    94.285714
3-14    85.000000
4-13    79.285714
5-12    64.285714
6-11    62.857143
7-10    60.714286
8-9     48.571429
Name: games, dtype: float64
'''

## 8.  For each champion, 
# determine the average margin of victory in all games played by that team.  
# Make a table to the top-10 in terms of
##     average margin, sorted from highest to lowest.  Include all that tie
##     for 10th position if necessary.

df8 = df[['Team','margin','Year']]    # subset the new data frame, column of 'Team', 'margin' and 'Year'
df8a = df[['Team.1','margin','Year']]  # subset the new data frame, column of 'Team.1', 'margin' and 'Year'
df8a.columns = ['Team', 'margin', 'Year'] # rename the columns 
df8b = pd.concat([df8,df8a],ignore_index=True)  # concate the df8 and df8a 
df8c = df8b['margin'].groupby([df8b['Team'],df8b['Year']]).mean() # group margin with 'Team' and 'Year' and find the mean
df8d = df8c.reset_index() # reset the index
df8e= Champ[['winner', 'Year']]   # subset the 'winner' and 'Year'
df8f = pd.merge(df8d,df8e, how = 'left')  # merge df8d and df8e
df8g = df8f.loc[(df8f['winner']==df8f['Team'])]  # find the winner in average margin
k8h = df8g.sort_values(by = 'margin', ascending = False) # sort the value by 'margin', from high to low, re
k8i = k8h.reset_index()  # reset the index 
k8i[['winner','Year','margin']].head(10)  # top 10 average margin of victory in all games played by that team. 

'''
8.

           winner  Year     margin    # top 10 average margin of victory in all games played by that team. , from highest to lowest
0        Kentucky  1996  21.500000
1       Villanova  2016  20.666667
2  North Carolina  2009  20.166667
3            UNLV  1990  18.666667
4       Villanova  2018  17.666667
5            Duke  2001  16.666667
6      Louisville  2013  16.166667
7         Florida  2006  16.000000
8  North Carolina  1993  15.666667
9            Duke  2015  15.500000
'''

## 9.  For each champion, determine the average seed of all opponents of that team.  
## Make a table of top-10 in terms of average seed, 
# sorted from highest to lowest.  
# Include all that tie for 10th position if necessary.
# Then make a table of the bottom-10, sorted from lowest to highest.
# Again include all that tie for 10th position if necessary. 

df9 = df[['Team', 'Seed.1','Year']]    # create a new data frame which contain 'Team', 'Seed.1', 'Year', team with seed of opponent team
df9a = df[['Team.1','Seed','Year']]    # create a new data frame which contain 'Team.1','Seed', 'Year', team with seed of opponent team
df9a.columns = ['Team', 'Seed.1','Year'] # rename the column of df9a
df9b = pd.concat([df9,df9a],ignore_index=True)  # concat 'df9' and 'df9a'
df9c = df9b['Seed.1'].groupby([df9b['Team'],df9b['Year']]) # group 'Seed.1' with 'Team' and 'Year'
df9d = df9c.mean().reset_index()  # calculate the mean and reset the index
df9e = pd.merge(df8e,df9d,how = 'left')  # merge the df8e and df9d
df9f = df9e.loc[(df9e['winner']==df9e['Team'])] # winner in mean seed
df9g = df9f.sort_values(by = 'Seed.1',ascending=False) # sort it by 'Seed.1',high to low
df9g1 = df9g.reset_index() # reset the index
df9g1[['winner','Year','Seed.1']].head(11)  # due to the tie, use head(11)
df9h= df9f.sort_values(by = 'Seed.1',ascending = True) # sort it by 'Seed.1, low to high
df9h1 = df9h.reset_index()  # reset the index 
df9h1[['winner','Year','Seed.1']].head(11)  # due to the tie, use head(11)

'''
9.

            winner  Year    Seed.1     # the answer, top 10, sort from highest to lowerest
0             UNLV  1990  9.000000
1       Louisville  2013  8.500000
2         Virginia  2019  8.000000
3           Kansas  2008  8.000000
4          Florida  2006  7.666667
5      Connecticut  1999  7.500000
6       Louisville  1986  7.500000
7         Arkansas  1994  7.333333
8      Michigan St  2000  7.166667
9          Indiana  1987  7.000000
10  North Carolina  2005  7.000000

            winner  Year    Seed.1      # bottom 10, from lowest to highest
0        Villanova  1985  3.333333
1      Connecticut  2014  4.666667
2        Villanova  2016  4.833333
3   North Carolina  1993  5.500000
4   North Carolina  2017  5.666667
5         Syracuse  2003  5.666667
6   North Carolina  2009  5.833333
7          Florida  2007  6.000000
8         Kentucky  1996  6.000000
9         Maryland  2002  6.000000
10        Michigan  1989  6.000000
'''

## 10. Determine the 2019 champion.

Champ[['winner', 'Year']].loc[(Champ['Year'] == 2019)]   # winner and year of 2019 championship   

'''
10.                        
        winner  Year              # the answer, 2019 champion
2204  Virginia  2019
'''