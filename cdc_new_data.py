# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:16:40 2020

@author: nnickelson
"""

import requests
import lxml.html as lh
import extract_data


class CDCRecentData():

    url='https://www.cdc.gov/flu/about/burden/index.html'
        
    page = requests.get(url)
    doc=lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    
    #Create empty list
    col=[]
    data_rows=[]
    
    def get_data(self):
        
        self.tr_elements.pop(0)
        
        self.col = extract_data.column_extractor(self.tr_elements, self.col)
       
        #collect row data, skip the first because it is header data   
        for j in range(1,len(self.tr_elements)):
            #T is our j'th row
            T=self.tr_elements[j]
            
            #The rows we need have 9 elements. Row 8 is an informative row
            if len(T)!=9 or j==8:
                continue
            
            self.data_rows = extract_data.row_extractor(self.data_rows, T)
        return self.data_rows, self.col