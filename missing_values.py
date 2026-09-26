import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\Data_Collections\pokemon.csv')

#print(df.head(10))  # Display the first 10 rows of the DataFrame

print(df.shape)  # Display the shape of the DataFrame (rows, columns)

## isnull() and notnull() methods to check for missing values in the DataFrame
print(df.isnull())  # Check for missing values in the DataFrame