#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################################
# Wellington Silva                                        #
# https://www.kaggle.com/gatunnopvp                       #
# https://github.com/WellingtonSilv                       #
# https://www.linkedin.com/in/jwellingtonsilva/           #
###########################################################

# Loading required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import html5lib
import warnings
warnings.filterwarnings('ignore')

# Creating essencial functions
def getdata(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html5lib")
    return soup

# creating a DataFrame to storage all data
coinDf = pd.DataFrame(columns = ["rank",
                                 "symbol",
                                 "price",
                                 "1hVariation",
                                 "24hVariation",
                                 "24hVolume",
                                 "7dVariation",
                                 "MktCap",
                                 "FDV"]
                     )

# creating a loop to navegate througt coingecko main pages
for page in range(1,130):
    
    # getting page URL
    mainPage = getdata("https://www.coingecko.com/?page="+str(page))
    
    # finding the table data
    tableHtml = mainPage.find('table',{'class':'sort table mb-0 text-sm text-lg-normal table-scrollable'})

    # defyning start and end variables to help 
    # assist with for loop and localize the correct data
    start = 1
    end = 10

    # creating the first loop that runs through all page
    for i in range(1,101):
    
        # creating a DataFrame to storage scraped text and help with coinDf apprend data
        text = pd.DataFrame(["x"],columns = ["test"])
    
        # a loop that gos through all 9 columns from coinGecko coinstable
        for n in range(start,end):
        
            # this line gets and treat the text from the select column and storage
            # into a new column on text DataFrame
            text[str(n)] = tableHtml.tbody.find_all("td")[n].text.replace("\n","")
     
        # appending all variables using append function and .iloc to locate the
        # data previous storaged into text DataFrame
        coinDf = coinDf.append({"rank":text.iloc[0,1],
                                "symbol":text.iloc[0,2],
                                "price":text.iloc[0,3],
                                "1hVariation":text.iloc[0,4],
                                "24hVariation":text.iloc[0,5],
                                "24hVolume":text.iloc[0,6],
                                "7dVariation":text.iloc[0,7],
                                "MktCap":text.iloc[0,8],
                                "FDV":text.iloc[0,9]}, ignore_index=True)
    
        # incrementing
        start = start+11
        end = end+11

coinDf