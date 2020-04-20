# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:37:12 2020

@author: nnickelson
"""

import requests
import lxml.html as lh
import extract_data

class CDCHistoricData():

    url='https://www.cdc.gov/mmwr/preview/mmwrhtml/mm5933a1.htm'
        
    page = requests.get(url)
    doc=lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
        
    #Create empty list
    col=[]
    data_rows=[]

    def get_data(self):
        
        #There's split header on this table. 'Season' and 'Prominent Strain' 
        self.tr_elements = self.tr_elements[2:]
        self.col.append('Season')
        self.col.append('Prominent Strain')
        
        #Column extractor function
        self.col = extract_data.column_extractor(self.tr_elements, self.col)
        
        #collect row data    
        for j in range(1,len(self.tr_elements)):
            #T is our j'th row
            T=self.tr_elements[j]
            
            #There are two tables, we are concerned with the second table with rows of length 10
            if len(T)!=10 or j<35:
                continue          
            
            #Row extractor function
            self.data_rows = extract_data.row_extractor(self.data_rows, T)
            
        return self.data_rows, self.col