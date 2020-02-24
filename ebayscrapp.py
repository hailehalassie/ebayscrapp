from bs4 import BeautifulSoup
import requests
import csv
from tkinter import *
import tkinter
import os

def click():
    with open("ebaymjuII.csv", "w",encoding='utf-8') as csvFile:
        csvWriter = csv.writer(csvFile)
        header = ("Camera", "Price", "Type", "Shipping")
        csvWriter.writerow(header)
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=olympus+mju+ii&_sacat=0'
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')

        ad_cont = soup.findAll('div', {"class": "s-item__wrapper clearfix"})

        for ads in ad_cont:
            adName_cont = ads.findAll("h3", {"class": "s-item__title"})
            adName = adName_cont[0].text

            adPrice_cont = ads.findAll("span", {"class": "s-item__price"})
            adPrice = adPrice_cont[0].text

            adType_cont = ads.findAll("span", {"class": "s-item__purchase-options-with-icon"})
            try:
                adType = adType_cont[0].text
            except:
                adType = "bidding"

            adShipping_cont = ads.findAll("span", {"class": "s-item__shipping s-item__logisticsCost"})
            try:
                adShipping = adShipping_cont[0].text
            except:
                adShipping = "Not Specified"

            table_list = (adName, adPrice, adType, adShipping)
            csvWriter.writerow(table_list)
    csvFile.close()
    os.startfile('C:\\Users\\hailehalassie\\PycharmProjects\\ebayscrapp\\ebaymjuII.csv')


top = Tk()
L1 = Label(top, text="Ebay Olympus Mju II",).grid(row=0,column=1)
B = Button(top, text="Generate", command= click).grid(row=1,column=1)

top.mainloop()