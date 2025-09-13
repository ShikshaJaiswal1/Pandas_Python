import pandas as pd   
# head(n)  tail(n)  if n is not passed then it will give default 5 rows

df = pd.read_csv("netflix_titles.csv",encoding="latin1")

print("Display 10 rows of first") 
print(df.head(10))


print("Display 10 rows of Last") 
print(df.tail(10))