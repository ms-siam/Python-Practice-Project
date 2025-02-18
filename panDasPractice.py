import pandas as pd

print(pd.DataFrame({'Apples': [30], 'Bananas': [21]}, index= ['Box 1']))

#If a DataFrame is a table, a Series is a list
print(pd.Series([1,2,3,4,5]))

#We can assign row labels to the series using index parameter
print(pd.Series([30, 40, 45], index=['2015 Sales', '2020 Sales', '2025 Sales'], name='Product A'))
