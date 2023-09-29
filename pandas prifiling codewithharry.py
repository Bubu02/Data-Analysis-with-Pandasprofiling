import pandas as pd
# from pandas_profiling import ProfileReport # this is outdated
from ydata_profiling import ProfileReport

df = pd.read_excel('fruit_data_with_color.xlsx')
print(df)

# Generate a report
profile = ProfileReport(df)
# profile = ProfileReport(df, minimal= True)
profile.to_file(output_file="fruit data.html")