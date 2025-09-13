import pandas as pd
# read data from CSV file into a dataframe

# df = pd.read_csv("netflix_titles.csv",encoding="UTF-8")
df = pd.read_csv("netflix_titles.csv",encoding="latin1")
print(df) 
# we can also read data of json, xlsx, sql or something else with syntax basically like read_typeofdata

# We can face three types of error while reading the data
# 1. We can get encoding error which can be fixed by UTF-8 or latin1
# 2. We can get large data set error which can basically be fixed by for loop
# 3. If we are trying to read dataset from cloud platform can be resolved using libarary : gcsfs


