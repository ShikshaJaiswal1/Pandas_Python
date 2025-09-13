import pandas as pd

data = {
    "Name" : ['Shiksha', 'Rishu', 'Shivam'],
    "Age" : [21, 22, 23],
    "City" : ['Kanpur', 'Mumbai', 'Delhi']
    
}


df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
# df.to_json("output.json", index=False)