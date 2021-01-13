
# =============================================================================
# 
# Keyu Chen - KM5AR
# Homework: Python and Web Scraper
# 
# =============================================================================

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# 
# ask user to input a stock ticker
get_ticker = input('Which stock do you want to check?(please type in ticker)' )

# turn the ticker into yahoo finance link
ticker_link = 'https://finance.yahoo.com/quote/' + str(get_ticker) +'/'+ 'key-statistics?p=' + str(get_ticker)

# use webdriver to open the website
#Chrome_webdriver = webdriver.Chrome()
Chrome_webdriver = webdriver.Chrome(ChromeDriverManager().install())
Chrome_webdriver.get(ticker_link) # open the link with Chrome
script = Chrome_webdriver.execute_script('return document.body.innerHTML;') # turn into HTML
linkBeautifulSoup = BeautifulSoup(script,'lxml') # use beautifulsoup to make it better

# find all the data which is 'td' with class 'Ta(c)'
features = linkBeautifulSoup.find_all('td', class_='Ta(c)')
list1 = []  # create a empty list to hold list1 from the for loop
final = [] # create a empty list to hold the final result
for i in features:  # for loop to obtain all the text and append it into 'final'
    for line in features:
        list1.append(line.text)
    final.append(list1)

final3 = final[0][0:45] # slicing out all the data we need 

df3 = pd.DataFrame(np.array(final3).reshape(9,5)) 
# turn it into 9 row and 5 column and turn it into a data frame

# rename the row and column of data-frame
df4 = df3.rename(columns={0:'Current',1:'3/31/2020',2:'12/31/2019',3:'9/30/2019',4:'6/30/2019'}, \
           index = {0:'Market Cap',1:'Enterprise Value',2:'Trailing P/E',3:'Forward P/E',4:'PEG Ratio (5 yr expected)',
                    5:'Price/Sales(ttm)',6:'Price/Book(mrq)',7:'Enterprise Value/Revenue',8:'Enterprise Value/EBITDA'})

# data clearning 
df5 = df4.replace('B','',regex=True) # replace B(billions) with nothing
df6 = df5.rename(index = {'Market Cap':'Market Cap(Billions)', 'Enterprise Value': 'Enterprise Value(Billions)'})
df7 = df6.replace('N/A', 0 ,regex=True)
df8 = df7.apply(pd.to_numeric)  # turn the data from string into numeric
df9 = df8.replace(0, 'N/A' ,regex=True)

# if you want a csv file, uncomment following two line
# =============================================================================
# df9.to_csv('ticker_financial_info2.csv')    # if you want to output the csv file right now
# pd.read_csv('ticker_financial_info.csv')   # read in the csv file 
# =============================================================================


# below is additional calculation 
df10 = df9.T    
# add two column
# 1) percentage change in market cap from previous year
df10['Changing in Market Cap from Previous Year']= df10['Market Cap(Billions)'].diff(periods=-1)
# 2) add second column, changing in Enterprise Value from Previous year
df10['Changing in Enterprise Value(Billions) from Previous Year'] = df10['Enterprise Value(Billions)'].diff(periods=-1)
close_price = [entry.text for entry in linkBeautifulSoup.find_all('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]

print('The close price of ' + str(get_ticker).upper() + ' today is: ' + str(close_price)) 
# if you want to know the close stock price of the ticker
df10.to_csv('ticker_financial_info2.csv')  # output the final dataframe into CSV file with index

