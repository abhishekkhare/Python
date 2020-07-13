import pandas as pd
import sys

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df = pd.read_csv('friends.csv')
print("***** Data Frame *******")
print(df)
print("Data Frame Shape --> ",df.shape)
print("Data Frame Info --> ",df.info())

print("***** Data Frame Head *******")
print(df.head())

print("***** Data Frame Head 7*******")
print(df.head(7))

print("***** Data Frame Tail *******")
print(df.tail())

print("***** Data Frame Tail 7 *******")
print(df.tail(7))

print("***** Read File into dictionary *******")
dfd = pd.read_csv('friends.csv', index_col=0, squeeze=True).to_dict()
print(dfd)

print("***** Dictionary to Data Frame *******")
dfnew = pd.DataFrame(dfd)
dfnew1 = pd.DataFrame(dfd)
print(dfnew)
print(dfnew['Email'])
print("Type:",type(dfnew['Email']))

print("as attribute:\n",dfnew.Email)

print("multiple columns:\n", dfnew[['Name','Email']])
print("List columns names:\n", dfnew.columns)
print("1st Row: \n", dfnew.iloc[0])
print("1st and 2nd Row: \n", dfnew.iloc[[0, 2]])
print("1st and 2nd Row only 3rd column: \n", dfnew.iloc[[0, 2], 2])

print("Row with index 1 :\n",dfnew.loc[1])
print("Row with index 1 and 5:\n",dfnew.loc[[1,5]])
print("Row with index 1 and 5 only Email column:\n",dfnew.loc[[1,5], 'Email'])
print("Row with index 1 and 5 only Name and Email column:\n",dfnew.loc[[1,5], ['Name','Email']])
# dfnew.loc[0] --> will not work as no index 0 present in the data frame.
print("Each city and how many times it occurs \n", dfnew['City'].value_counts())

print("Get range of columns and rows")
print(dfnew.loc[[1, 2, 3, 11],'City'])
print(dfnew.loc[3:11,'City'])
print(dfnew.loc[3:11,'Age':'Email'])

sys.exit()