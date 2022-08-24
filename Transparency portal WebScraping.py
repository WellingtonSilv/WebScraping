#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################################
# Wellington Silva                                        #
# https://www.kaggle.com/gatunnopvp                       #
# https://github.com/WellingtonSilv                       #
# https://www.linkedin.com/in/jwellingtonsilva/           #
###########################################################

# loading required libraries
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os

# defyning driver path
PATH = "put your driver path here"

# defyning the driver
driver = webdriver.Chrome(PATH)

# defyning months and years to bee scraped
month = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO",
         "JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"]

year = ["2016","2017","2018","2019","2020","2021","2022"]

for i in year:
    
    for j in month:
        
        driver.implicitly_wait(180)
        
        # accessing the mainPage to be scraped
        driver.get("https://www.municipioonline.com.br/al/prefeitura/campoalegre/cidadao/servidor")
        
        # locating and sending keys to payment year field
        input_pay_year = driver.find_element(by="id", value= "ddlAnoFolhaPagamento")
        input_pay_year.send_keys(i)

        # locating and selecting the payer
        Payer = driver.find_element(by = "id",
                                value = "ddlUnidGestoraFolhaPagamento"
                                   )
        
        drop = Select(Payer)
        drop.select_by_value("12264628000183")

        # locating and sending keys to month field
        input_month = driver.find_element(by = "id", value = "ddlMesFolhaPagamento")
        input_month.send_keys(j)

        # locating and clicking on search bottom
        search_bottom = driver.find_element(by = "id", value = "btnFiltrarFolhaPagamento")
        time.sleep(3)
        search_bottom.click()
        
        # locating and clicking on csv download bottom
        csv_download_bottom = driver.find_element(by = "xpath", value = "/html/body/form/div[5]/section/div/div/section[2]/div[2]/div/div/div/div/div/div[1]/div/div[6]/div/div/div/div/div[2]/div/div/div/div[1]/a[2]")
        time.sleep(3)
        csv_download_bottom.click()
        
        # defyning directory where the download data where storaged
        os.chdir("PUT THE DOWNLAOD DIRECTORY HERE")
        
        time.sleep(3)
        
        csv = pd.read_csv("Município Online.csv", delimiter = ",")
        
        # removing previuos download file
        os.remove('PUT THE DOWNLAOD DIRECTORY HERE/Município Online.csv')

        csv.rename(columns = {
            'ï»¿""':"month",
            "Nome":"name",
            "Matrícula":"subscription",
            "Cargo":"jobPosition",
            "Nível":"jobLevel",
            "Valor Base":"baseValue",
            "Proventos":"income",
            "Descontos":"discounts",
            "Líquido":"liquidIncome"
        }, inplace = True)

        csv["month"] = j+"/"+i
        
        if (j=="JANEIRO") & (i=="2016"):

            csv.to_csv('PUT THE DOWNLAOD DIRECTORY HERE/mainBase.csv', index = False)

        else:
        
            mainBase = pd.read_csv("mainBase.csv", delimiter = ",")
            mainBase = pd.concat([mainBase,csv])

            mainBase.to_csv('PUT THE DOWNLAOD DIRECTORY HERE/mainBase.csv', index = False)
            
print("Files downdload finished")