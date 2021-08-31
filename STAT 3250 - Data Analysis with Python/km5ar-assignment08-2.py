
##
## File: assignment08.py (STAT 3250)
## Topic: Assignment 8 
## Name: Keyu Chen - Km5ar
##



# Directions: Please submit your Python code file, formatted as in previous assignments.
# The grader should be able to run your code when it is placed in the same directory as the input data file. 
# Be sure that your code loads any libraries you are using.

# Background: The folder Stocks.zip contains nearly 300 files, each including daily data for a specific stock, 
# with stock ticker symbol given in the file name. Each observation includes the following:

# Date = date information recorded Open = opening stock price
# High = high stock price Low = low stock price Close = closing stock price
# Volume = number of shares traded
# Adj Close = closing price adjusted for stock splits (ignored for this assignment)


# The time interval covered varies from stock to stock. There are some missing records, 
# so the data is incomplete. Note that some dates are not present because the exchange is closed on weekends and holidays. 
# Those are not missing records. Answer the questions below based on the data available in the files.
import pandas as pd
import glob
import numpy as np

# Reminder: Change to directory 'Stocks'

filelist = glob.glob('*.csv') # 'glob.glob' is the directory search
# put all the file in one folder named "Stocks", then change directory to 'Stocks', '*.csv' selects files ending in '.csv', which is all the stock file
filelist

df = pd.DataFrame() #formed dataframe that will contain all data
for f in filelist:
    df2 = pd.read_csv(f) #imported each file and added a new column with their name
    df2['Name'] = f  
    df = pd.concat([df,df2]) #added the new files to the big dataframe
df['Date'] = pd.to_datetime(df['Date']) # turn 'Date' into datetime

# 1.	Find the mean for the Open, High, Low, and Close entries for all records for all stocks.
 
df.loc[:,'Open':'Close'].mean() # subset the Open, High, Low, and Close entries for all records for all stocks.
 
'''
1.

Open     50.863852       # the answer, the mean for the Open, High, Low, and Close entries for all records for all stocks.
High     51.459412
Low      50.253368
Close    50.876482
dtype: float64
'''

# 2.	Find the top-5 and bottom-5 stocks in terms of their average Close price. 
# Give tables showing the stock ticker symbol and the average Close price.

group2 = df['Close'].groupby(df['Name'])   # group 'Close' by 'Name'
group2a = group2.mean().sort_values(ascending=False)  # mean on group2 and sort the value from largest from smallest
print(group2a.head(5),group2a.tail(5))  # top-5 and bottom-5 stocks in terms of their average Close price. 


'''
2.

Name                        # the answer, the top-5 and bottom-5 stocks in terms of their average Close price.
CME.csv     253.956017
AZO.csv     235.951950
AMZN.csv    185.140534
BLK.csv     164.069088
GS.csv      139.146781
Name: Close, dtype: float64 Name
HBAN.csv    13.697483
ETFC.csv    12.808103
XRX.csv     11.291864
F.csv       11.174158
FTR.csv      8.969515
Name: Close, dtype: float64
'''
# 3.	Find the top-5 and bottom-5 stocks in terms of the day-to-day volatility of the price, 
# which we define to be the mean of the daily di↵erences High - Low for each stock. 
# Give tables for each, as in the previous problem.

df['dailyDifferences'] = df['High'] - df['Low'] # create a new column, which equal 'High'-'Low'
group3 = df['dailyDifferences'].groupby([df['Name']]) # group 'dailyDifferences' by 'Name'
group3a = group3.mean().sort_values(ascending=False) # mean on group3, sort value from largest to smallest
group3a.head(5) # top-5 stocks in terms of the day-to-day volatility of the price
group3a.tail(5) # bottom-5 stocks in terms of the day-to-day volatility of the price, 


'''
Name                            # the top-5 stocks in terms of the day-to-day volatility of the price
CME.csv     7.697287
AMZN.csv    4.691407
BLK.csv     4.470693
AZO.csv     4.330294
ICE.csv     4.056189
Name: dailyDifferences, dtype: float64 Name

# bottom-5

NI.csv      0.363250               #  the bottom-5 stocks in terms of the day-to-day volatility of the price
HBAN.csv    0.343893
F.csv       0.323567
XRX.csv     0.308743
FTR.csv     0.205275
Name: dailyDifferences, dtype: float64
'''
# 4.	Repeat the previous problem, this time using the relative volatility, 
# which we define to be the mean of
# 	High — Low / 0.5(Open + Close)
#for each day. As above, provide tables.

df['relativeVolatility'] = (df['High'] - df['Low'])/(0.5*(df['Open']+df['Close'])) # create a new column 'relativeVolatility', equal High — Low / 0.5(Open + Close)
group4 = df['relativeVolatility'].groupby([df['Name']]) # group 'relativeVolatility' with 'Name'
group4a = group4.mean().sort_values(ascending=False)  # mean on group4, sort from largest to smallest
group4a.head(5) # top 5 interms of the relative colatility
group4a.tail(5) # bottom 5 interms of the relative colatility

'''
4.

Name                       # answer, top 5 interms of the relative colatility
AAL.csv     0.055533
LVLT.csv    0.054870
EQIX.csv    0.051295
REGN.csv    0.048172
ETFC.csv    0.045381
Name: relativeVolatility, dtype: float64

Name                       # bottom 5 interms of the relative colatility
WEC.csv    0.015761
CL.csv     0.015521
K.csv      0.014992
PG.csv     0.014192
GIS.csv    0.013966
Name: relativeVolatility, dtype: float64
'''

# 5.	For each day the market was open in October 2008, find the average daily Open, High, Low, Close, and Volume for all stocks.

Oct2008= df[(df['Date'] <= '2008-10-31') & (df['Date'] >= '2008-10-01')].loc[:,'Date':'Volume'] #masked all the entries that occured in October 2008, then got columns from Open to Close and then found their mean
answer = Oct2008.loc[:,'Open':'Volume'].groupby(Oct2008['Date']).mean()  # group Open, High, Low, Close, and Volume with Volumn
answer  # print out the answer

'''
5.

Date	       Open	                 High	              Low	            Close	           Volume            #each day the market was open in October 2008, the average daily Open, High, Low, Close, and Volume for all stocks.
2008-10-01	43.14787400732602	44.08999856043957	41.84549306593402	43.09509038095238	7319004.395604395
2008-10-02	43.03347829670328	43.44399110622708	40.64223306959706	41.12695831135535	9555246.886446886
2008-10-03	41.55553353505535	42.923983723247225	39.882175778597805	40.26438967527678	9184641.328413283
2008-10-06	39.408826967032965	40.56424815750916	36.73087815750916	39.17673917948716	11763387.545787545
2008-10-07	39.427267915129164	40.29394697047975	36.64457458302583	36.93387325461259	10918507.3800738
2008-10-08	36.10659142592592	38.78522094814816	35.06244334444445	36.67651724444444	13786255.185185185
2008-10-09	37.250108575091595	38.00215989743591	33.43717845787545	33.84860700732601	12810936.263736263
2008-10-10	32.581401221402196	35.952581863468666	30.43228679335793	33.99210245387452	18201515.86715867
2008-10-13	35.486543029411756	38.041322360294124	34.12238866176469	37.54819737500002	11483441.911764706
2008-10-14	38.581369155555564	39.62696194074074	35.5134432074074	36.78488779999998	12409278.888888888
2008-10-15	36.14959584615384	36.75710519780221	32.879339615384616	33.197031853479864	10516973.26007326
2008-10-16	33.48571331868131	35.09662886446887	31.415127234432234	34.59919290109891	12583982.051282052
2008-10-17	33.735344309090905	36.18436249818181	32.72996245818183	34.40065339636363	9973754.181818182
2008-10-20	34.98933961904764	36.35772752014653	33.96849689743589	35.90933936263735	7657442.49084249
2008-10-21	35.39047664705881	36.34474131985297	34.189520654411766	34.665476536764665	7599813.235294118
2008-10-22	33.75194015750915	34.34468756043956	31.386152673992658	32.373295498168474	9425614.285714285
2008-10-23	32.88951736296296	33.9870356962963	30.561443285185206	32.51636930000001	11898901.851851853
2008-10-24	30.04602829044118	32.498307753676464	29.403748908088268	31.395146113970608	9726575.0
2008-10-27	30.638139687732348	31.924868081784386	29.50141110780668	29.87717310408922	8362392.19330855
2008-10-28	30.86022182527882	33.14538910780668	29.345017643122684	32.95557508921932	10916998.141263941
2008-10-29	32.86487073260072	34.88758112087914	31.85439454578754	33.179376131868146	10369443.223443223
2008-10-30	34.27394056934307	35.29207922262774	32.88426908394161	34.2848166131387	8928568.613138687
2008-10-31	33.99577088970591	35.761028069852934	33.29463118750001	34.97691048897058	9213692.647058824

'''

# 6.	For 2011, find the date 
# with the maximum average relative volatility for all stocks 
# and the date with the minimum average relative volatility for all stocks. 
# (Consider only days when the market is open.)

df2011 = df[df['Date'].dt.year == 2011]   # subset the data of 2011
group6 = df2011['relativeVolatility'].groupby(df2011['Date'])  # group 'relativeVolatility' with  
group6a = group6.mean().sort_values(ascending = False)  # find the mean and sort from largest to smallest
group6a.head(1)  # maximum average relative colatility for all stocks
group6a.tail(1)  # minimum average relative colatility for all stocks


'''
6.

Date                                
2011-08-08    0.073087             # the answer, the date with the maximum average relative colatility for all stocks
Name: relativeVolatility, dtype: float64

2011-12-30    0.014162              # # the answer, the date with the minimum average relative colatility for all stocks
Name: relativeVolatility, dtype: float64
'''

# 7.	For 2010-2012, 
# for each day of the week, 
# find the average relative volatility for all stocks. 
# (Consider only days when the market is open.)

df2010to2012 = df[(df['Date'].dt.year >= 2010) & (df['Date'].dt.year <= 2012)]   # subset the data from 2010 - 2012
group7 = df2010to2012['relativeVolatility'].groupby(df2010to2012['Date'].dt.dayofweek)  # group 'relativeVolatility' with 'day of week'
group7.mean()  # mean of gourp7

'''
7.

Date                     # the answer, for each day of the week, the average relative volatility for all stocks
0    0.022109
1    0.023836
2    0.023443
3    0.024865
4    0.023018
Name: relativeVolatility, dtype: float64
'''

# 8.	For each month of 2009, determine which stock had the maximum average relative volatility. Give a table with the month (number is fine), stock ticker symbol, and average relative volatility.

df2009 = df[(df['Date'].dt.year == 2009)]   # subset the data of 2009
group8= df2009['relativeVolatility'].groupby([df2009['Date'].dt.month,df2009['Name']]) # group 'relativeVolatility' with 'Date'
group8.mean().groupby(level=0,group_keys=False).nlargest(1) # each month of 2009,which stock had the maximum average relative volatility

'''
8.

Date  Name                         # each month of 2009,which stock had the maximum average relative volatility
1     GGP.csv     0.190686
2     HBAN.csv    0.275587
3     GGP.csv     0.241744
4     GGP.csv     0.212291
5     GGP.csv     0.187383
6     GGP.csv     0.131522
7     AIG.csv     0.121527
8     AIG.csv     0.141233
9     GGP.csv     0.103328
10    AAL.csv     0.071610
11    GGP.csv     0.089010
12    GGP.csv     0.112847
Name: relativeVolatility, dtype: float64
'''


# 9.	The “Python Index” is designed to capture the collective movement of all of our stocks. 
# For each date, this is defined as the average price for all stocks for which we have data on that day, 
# weighted by the volume of shares traded for each stock. 
# That is, for stock values S1, S2,. .. 
# with corresponding sales volumes V1, V2,. . ., 
# the average weighted by volume is
# S1V1 + S2V2 + ·· ·/ V1 + V2 + ·· ·
# Find the Open, High, Low, and Close f
# or the Python Index for each day the market was open in January 2013. 
# Give a table the includes 
# the Date, Open, High, Low, and Close, with one date per row.

jan2013 = df[(df['Date'] >= '2013-01-01') & (df['Date'] <= '2013-01-31')].loc[:,'Date':'Volume']  # subset the data of 2013-01-01 to 

for i in jan2013.columns[1:5]:   # for loop
    jan2013[i] = jan2013[i]* jan2013['Volume']  # Open,Low, and Close times Volume
group9 = jan2013.loc[:,'Open':'Volume'].groupby(jan2013['Date'])  #group 'open':'Volume' with 'Date'
group9a = group9.sum()  # sum of group9
group9a[['Open','High','Low','Close']].div(group9a['Volume'].values,axis=0)  # 'Open','High','Low','Close' divded by 'Volume' , the Date, Open, High, Low, and Close, with one date per row.
    
'''
9.

                 Open       High        Low      Close    # the Date, Open, High, Low, and Close, with one date per row.
Date                                                  
2013-01-02  37.218240  37.669825  36.804244  37.394700
2013-01-03  36.683928  37.175883  36.309854  36.730561
2013-01-04  37.735301  38.197961  37.471489  37.969676
2013-01-07  39.433973  39.952425  39.087880  39.596959
2013-01-08  39.403554  39.748143  38.922081  39.354890
2013-01-09  35.033924  35.411876  34.651302  35.014333
2013-01-10  37.137210  37.527043  36.757483  37.295754
2013-01-11  37.932903  38.256677  37.579063  37.991448
2013-01-14  38.348330  38.759699  37.980530  38.388938
2013-01-15  38.323527  38.880771  38.003460  38.487561
2013-01-16  39.353471  39.731879  38.887220  39.347620
2013-01-17  35.884004  36.233690  35.551895  35.877188
2013-01-18  40.277388  40.652477  39.865453  40.376961
2013-01-22  40.567323  41.068261  40.241281  40.851074
2013-01-23  44.417554  45.121563  44.065735  44.770209
2013-01-24  48.814446  49.728573  48.237470  49.174833
2013-01-25  58.340138  62.089706  58.052795  61.453043
2013-01-28  50.844625  51.450083  49.590466  50.007070
2013-01-29  41.631649  42.499318  41.221507  42.174208
2013-01-30  45.212780  45.587135  44.354852  44.792994
2013-01-31  44.310451  45.061372  43.789490  44.518366
'''

# 10.	For the years 2007-2012 determine the top-5 months and years 
# in terms of average relative volatility of the Python Index. 
# Give a table with the month, year, and average relative volatility.

df2007to2012= df[(df['Date'].dt.year >= 2007) & (df['Date'].dt.year <= 2012)].loc[:, 'Date':'relativeVolatility']  # subset the data from 2007 to 2012
df10 = df2007to2012[['Date','relativeVolatility','Volume']]  # keep columns 'Data' 'relativeVolatility' and 'Volume'
df10['Month'] = df10['Date'].dt.month   # create a new column 'Month', which is the month of the data
df10['Year'] = df10['Date'].dt.year     # create a new column 'Year', which is the month of the data 
df10a = df10[['Month','Year','relativeVolatility','Volume']]   # reorder the column

for i in df10a.columns[2:3]:   # set the for loop
    df10a[i] = df10a[i]*df10['Volume']       # times 'volume' for all the data of column 'relativeVolatility'
x = df10a[['relativeVolatility','Volume']].groupby([df10a['Year'],df10a['Month']])   # group 'RelativeVolatility' and 'Volume' with 'Year' and 'Month'
x1 = x.sum() # sum the data 
# x2 = x1['relativeVolatility'].div(x1['Volume'].values,axis=0

#x1['percentage'] = x1['relativeVolatility'].div(x1['Volume'].values,axis=0)  
# x2 = x1['percentage'].groupby(level=0, group_keys=False)
# x2.nlargest(5)

x2 = x1['relativeVolatility'].div(x1['Volume'].values,axis=0)  # divided relativeVolatility by Volume
x2.sort_values(ascending=False)[0:5]     # rank the top 5 months and years for the year 2007-2012

'''
10.

Year  Month                      # the answer,  # rank the top 5 months and years for the year 2007-2012
2008  10       0.119632
      11       0.105276
2009  2        0.095824
      3        0.089684
2008  12       0.082751
dtype: float64

'''





