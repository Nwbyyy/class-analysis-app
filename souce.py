import numpy as np
import pandas as pd
import openpyxl
#import matplotlib.pyplot as plt
#from sklearn.preprocessing import StandardScaler
#from imblearn.over_sampling import RandomOverSampler

#pip install xlrd


def read_file(file_name):
    wb = openpyxl.loadworkbook(file_name)
    ws = wb.active

    values = []
    headers = ['Student Name', 'Year', 'Major', 'GPA']

    def createarrays(worksheet, headers, num_columns):
        column_arrays = [[] for _ in range(num_columns)]
    
        for row in worksheet.iter_rows(min_row=2, values_only=TRUE):
            for col_idx, value in enumerate(row):
                column_arrays[col_idx].append(value)

        return column_array

    num_columns = len(headers)
    column_arrays = create_arrays(ws, headers, num_columns)
    print(column_arrays)
    wb.close()
