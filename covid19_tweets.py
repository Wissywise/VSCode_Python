import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\Data_Collections\covid19_tweets.csv')
#df = pd.read_csv('covid19_tweets.csv')
#print(df.head(10))  # Display the first 10 rows of the DataFrame


## Access elements in the DataFrame using column names
print(df.iloc[0, 0])  # Access the first row of the DataFrame
print(df.loc[0, 'user_location'])  # Access the first row of the DataFrame using loc
##print(df['user_name'])  # Access the 'user_name' column of the DataFrame

## Add a new column to the DataFrame

## Add rows to the DataFrame


## Remove (( pop and drop )) columns and rows from the DataFrame

## Rename columns and rows in the DataFrame

## Set an index for the DataFrame