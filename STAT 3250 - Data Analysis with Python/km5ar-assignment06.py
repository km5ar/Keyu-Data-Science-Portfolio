##
## File: assignment06.py (STAT 3250)
## Topic: Assignment 6
## name: keyu chen - km5ar

import numpy as np # load numpy as np
import pandas as pd # load pandas as pd
movies = open('movies.txt').read().splitlines()    # read in the data
# put each line from the text file into a list element.

##  This assignment requires the data file 'movies.txt'.  
# This file contains records for nearly 4000 movies, 
# including a movie ID number, 
# the title (with year of release, which is not part of the title), 
# and a list of movie genre classifications (such as Romance, Comedy, etc). 

##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  

## 1.  Are there any repeated movies in the data set?  A movie is repeated 
##     if the title is exactly repeated and the year is the same.  List any 
##     movies that are repeated, along with the number of times repeated.

moviesSeries = pd.Series(movies)   # convet it into Series
moviesSeries1 = moviesSeries.str.split('::')   # split it by '::'
moviesSeries2 = moviesSeries1.str[1]    # subset the title and the year
moviesSeries2Count = moviesSeries2.value_counts()   # value counts on moviesSeries2 and renamed it as moviesSeries2Count
moviesSeries2Count[moviesSeries2Count>1]  # keep the data which the movies is repeated.

'''
1,

0      # there is no any repeated movies in the data set
'''

## 2.  Determine the number of movies included in genre "Action", the number
##     in genre "Comedy", and the number in both "Children's" and "Animation".

genre= moviesSeries1.str[2]   # subset the genre 
sum(genre.str.contains('Action'))    # number of moveis included in "Action"
sum(genre.str.contains('Comedy'))    # Comedy
both = sum(genre.str.contains("Children's") & genre.str.contains("Animation"))  # both "Children's" and "Animation"
print(both) # print out the both 

'''
2.

503      # Action
1200     # Comedy
84      # in both Children's and Animation
'''

## 3.  Among the movies in the genre "Horror", what percentage have the word
##     "massacre" in the title?  What percentage have 'Texas'? (Upper or lower
##     cases are allowed here.) 

moviesSeriesLower = moviesSeries.str.lower()   # turn all data into lower case first
horror = moviesSeriesLower[moviesSeriesLower.str.contains('horror')] # subset the data, keep data contains 'horror'
nMassacre = horror[horror.str.contains('massacre')]   # keep the data which contains 'massacre'
nTexas = horror[horror.str.contains('texas')]   # keep the data which contains 'texas'
100*len(nMassacre)/len(horror)  # percentage have the word "massacre" in the title among the movies in "Horror"
100*len(nTexas)/len(horror)   # percentage have the word "Texas" in the title among the movies in "Horror" (upper and lower case together)

'''
3. 

2.623906705539359    # percentage have the word "massacre" in the title among the movies in "Horror"

1.1661807580174928    # percentage have the word "Texas" in the title among the movies in "Horror" (upper and lower case together)
'''

## 4.  How many titles are exactly one word?

moviesSeries_4 = moviesSeries.str.split('::')   # split the MoviesSeries by '::'
moviesSeries_41 = moviesSeries_4.str[1]   # subset the movies titles
moviesSeries_41Count = moviesSeries_41.str.count(' ') # count the number of words 
len(moviesSeries_41Count[moviesSeries_41Count == 1])   # count the number of titiles are exactly one word

'''
4.

690    # the answer, the number of titles are exactly one word
'''
## 5.  Among the movies with exactly one genre, determine the top-3 genres in
##     terms of number of movies with that genre.

moviesSeries5 = moviesSeries.str.split('::')   # split it by '::'
moviesSeries51 = moviesSeries5.str[2]        # took out only the genre column
moviesSeries52 = moviesSeries51.str.split('|')  # split it by '|'
oneGenre = moviesSeries52[moviesSeries52.apply(len) == 1]  # keep the movies which only has one genre
oneGenre.value_counts().head(3)     # find out the top-3 genres in terms of number of movies

'''
5.

[Drama]     843           # the answer, top-3 genres in terms of number of movies
[Comedy]    521
[Horror]    178
dtype: int64
'''

## 6.  Determine the number of movies with 0 genres, with 1 genre, with 2 genres,
##     and so on.  List your results in a table, with the first column the number
##     of genres and the second column the number of movies with that many genres.

moviesSeries53 = moviesSeries51.str.split('|',expand = True)    # split moviesSeries51 by '|', then the split elements will expand out into separate columns
moviesSeries53.count(axis=1).value_counts()      # the answer, first count the number of genra per row, then do a value count on it.

'''
6.

# left: number of genres, right: number of movies      

0                 0      # the the number of movies with 0 genres, with 1 genre, with 2 genres, and so on.
1              2025
2              1322
3               421
4               100
5                14
6                 1
'''

## 7.  How many remakes are in the data?  A movie is a remake if the title is
##     exactly the same but the year is different. (Count one per remake.  For
##     instance, 'Hamlet' appears 5 times in the data set -- count this as one
##     remake.)

moviesSeries77 = moviesSeries.str.split('::')  # split the data by '::'
moviesSeries78 = moviesSeries77.str[1]   # subset the data and year 
moviesSeries79 = moviesSeries78.str[:-7]  # keep the name only
moviesSeries80 = moviesSeries79.value_counts()   # value count the name
len(moviesSeries80[moviesSeries80>1])   # movies which are remake

'''
7.

38              # the answer, number of remakes
'''

## 8.  List the top-5 most common genres in terms of percentage of movies in
##     the data set.  Give the genre and percentage, from highest to lowest.

moviesSeries52List = moviesSeries52.tolist()  # turn moviesSeries52 into a list
genresL = sum(moviesSeries52List,[])   # turn it into a big list
genresS = pd.Series(genresL)     # change it into a series
countsGenreS = genresS.value_counts()    #  value counts the series
answer = countsGenreS/len(movies)*100   # genres in percentage of movies in the data set
answer.head(5)   # the top 5 most common genres in terms of percentage of movies in the data set

'''
8.

# Genre    Percentage

Drama       41.282514    # the answer, the top-5 most common genres in terms of percentage of movies in the data set.
Comedy      30.903940
Action      12.953902
Thriller    12.670616
Romance     12.129797
dtype: float64
'''

## 9.  Besides 'and', 'the', 'of', and 'a', what are the 5 most common words  
##     in the titles of movies classified as 'Romance'? (Upper and lower cases
##     should be considered the same.)  Give the number of titles that include
##     each of the words.

moviesSeriesL= moviesSeriesLower.str.replace(',','')   # use moviesSeriesLower from Q3, replace ',' by ' ' because some words "xxx," will be count as another words
moviesSeries9 = moviesSeriesL[moviesSeriesL.str.contains('romance')]  # keep the data which contians 'romance'
movies9Split = moviesSeries9.str.split('::')   # split moviesSeries9 by '::'
movies9Split1 = movies9Split.str[1]  # subset the title and year
movies9Split2 = movies9Split1.str.split('(') # split the title by '('
movies91 = movies9Split2.str[0]   # keep the title
movies92 = movies91.str.split(' ')  # slipt the title by ' '
list3 = pd.concat([movies92.str[0],movies92.str[1],movies92.str[2],movies92.str[3],movies92.str[4],
                   movies92.str[5],movies92.str[6],movies92.str[7],movies92.str[8],movies92.str[9],
                   movies92.str[10],movies92.str[11],movies92.str[12],movies92.str[13],movies92.str[14],
                   movies92.str[15],movies92.str[16]])   # concatenate it together
list9 = list3.value_counts()   # value_counts all the words
list9Dand = list9.drop('and',axis=0)   # drop the "and"
list9Dthe = list9Dand.drop('the',axis=0)  # drop the "the"
list9Dof = list9Dthe.drop('of',axis=0) # drop the "of"
list9Da = list9Dof.drop('a',axis=0)  # drop the "a"
list9Da.head(6)   # top 5 most common words in the titles of movies classified as 'romance'
        
'''
9.

in       27    # top 5 most common words in the titles of movies classified as 'romace' Besides 'and', 'the', 'of', and 'a',
love     24
to       14
you      13
on       10
dtype: int64
'''

## 10. It is thought that musicals have become less popular over time.  We 
##     judge that assertion here as follows: Compute the mean release years 
##     for all movies that have genre "Musical", and then do the same for all
##     the other movies.  Then repeat using the median in place of mean.

## for musical
moviesSeriesL = moviesSeries.str.lower()   # lower the case of all data 
moviesSeriesLM =  moviesSeriesL[moviesSeriesL.str.contains('musical')]  # keep the data which only contains 'musical'
moviesSeriesL11 = moviesSeriesLM.str.split('::')   # split the data by '::'
moviesSeriesL22 = moviesSeriesL11.str[1]       # subset movies title 
moviesSeriesL33 = moviesSeriesL22.str.split('(')   # split it by '('
moviesSerlesL44 = moviesSeriesL33.str[-1]     # subset the data
moviesSeriesL55 = moviesSerlesL44.str[0:4]    # subset the numbers out
np.mean(moviesSeriesL55.astype(float))         # change the number into float, and calcualte the mean
np.median(moviesSeriesL55.astype(float))      #  change the number into float, and calcualte the median

## for non musical
moviesSeriesLM =  moviesSeriesL[-moviesSeriesL.str.contains('musical')]  # keep the data which are non 'musical'
moviesSeriesL11 = moviesSeriesLM.str.split('::')   # split the data by '::'
moviesSeriesL22 = moviesSeriesL11.str[1]       # subset movies title 
moviesSeriesL33 = moviesSeriesL22.str.split('(')   # split it by '('
moviesSerlesL44 = moviesSeriesL33.str[-1]     # subset the data
moviesSeriesL55 = moviesSerlesL44.str[0:4]    # subset the numbers out
np.mean(moviesSeriesL55.astype(float))         # change the number into float, and calcualte the mean
np.median(moviesSeriesL55.astype(float))      #  change the number into float, and calcualte the median

'''
10.

# musical 
1968.7456140350878    # mean for musical

1967.0    # median for musical

# non-musical
1986.5908729105863   # mean for non-musical

1994.0    # median for non-musical
'''


