# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:35:04 2020

@author: nnickelson
"""
import requests
from bs4 import BeautifulSoup

def column_extractor(elements, col):
    for t in elements[0]:
        name=(t.text_content()).strip()
        col.append(name)
    return col

def row_extractor(data_rows, T):
    
    rowData=[]
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        #numerical data on this site uses commas to separate thousands
        data=str(data).strip().replace(',','')
        #If data is numeric then convert its value to integers
        try:
            data=int(data)
        except:
            pass
        rowData.append(data)

    data_rows.append(rowData)
    return data_rows

#Current google data listed 
#Used BeautifulSoup here because scraping with lxml was proving troublesome
def now_data():
    URL='https://www.google.com/search?q=coronavirus+deaths&oq=coronavirus+deaths&aqs=chrome..69i57j69i60j69i61j69i60.3535j0j7&sourceid=chrome&ie=UTF-8'
      
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36' }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    #This was the div line for the information I was looking for
    title = soup.findAll("div",{"class":"yeRnY sz9i9"})
    #There were several div lines matching the one above. This is the correct one and extracts the numerical data
    now_num = int((title[8].text).strip().replace(',',''))
    print( now_num)
    return [["**COVID-19**", now_num]]