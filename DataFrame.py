import pandas as pd
import numpy as np
# Create a pandas DataFrame

# From dictionary of Series
dict_data = {'A': pd.Series([1, 2, 3]), 'B': pd.Series([4, 5, 6]), 'tweet': pd.Series([7, 8, 9]), 'user_name': pd.Series(['Wisdom', 'John', 'mark'])}
            

df_from_dict_of_series = pd.DataFrame(dict_data)
print(df_from_dict_of_series)


# From dictionary of Series
dict_data = {'A': pd.Series([1, 2, 3]), 'B': pd.Series([4, 5, 6]), 'tweet': pd.Series([7, 8, 9]),  'user_name': pd.Series(['Wisdom', 'John', 'mark']) }


# from dict of ndarray/list/tuple
data = {'a': 1, 'b': 2, 'c': 3}
df_from_dict = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df_from_dict)

df = pd.read_csv('covid19_tweets.csv')

df.head(10)  # Display the first 10 rows of the DataFrame