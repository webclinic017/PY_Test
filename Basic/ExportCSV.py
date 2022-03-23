
import pandas as pd

data = {'Product': ['Desktop Computer','Tablet','Printer','Laptop'],
        'Price': [850,200,150,1300]}

df = pd.DataFrame(data, columns= ['Product', 'Price'])
df.to_csv(r'export_dataframe.csv', index=False, header=True)
print(df)