# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:51:35 2020

@author: nnickelson
"""

import matplotlib.pyplot as plot
from pandas import DataFrame
import cdc_old_data
import cdc_new_data
import extract_data


def main():
    
    x=9#testing first change commit
    
    old_data = cdc_old_data.CDCHistoricData()
    rec_data = cdc_new_data.CDCRecentData()
    
    old_row_data, older_col = old_data.get_data()
    rec_row_data, rec_col = rec_data.get_data()
    now_row_data = extract_data.now_data()
       
    finalColumns = [older_col[0], older_col[8]]
    
    old_rows = [[x[0],x[8]] for x in old_row_data]
    rec_rows = [[x[0],x[7]] for x in rec_row_data]
        
    finalData = now_row_data + old_rows + rec_rows
    df = DataFrame(finalData, columns=finalColumns)
    df2 = df.groupby('Season').sum().sort_values('No.', ascending=False).reset_index()
    print(df2)
    
    df2.plot(kind='barh', x='Season', y='No.', figsize=(15,15)).invert_yaxis()
    plot.xlabel('CDC Flu Season Deaths (missing 07-08,08-09,09-10)', fontsize='25')
    plot.ylabel('Season', fontsize='30')
    plot.yticks(fontsize=12)
    plot.grid()
    
    
if __name__ == "__main__":
    main()



