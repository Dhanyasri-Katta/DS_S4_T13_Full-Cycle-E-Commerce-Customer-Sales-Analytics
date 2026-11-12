#A) Handling Missing Values
#1.Mean/Median/Mode Imputation
import pandas as pd
import numpy as np
#Sample Dataset
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})
#Display Original Dataset
print("Original Dataset (With Missing Values):")
print(df)
#Mean for Numeric
df['Age'] = df['Age'].fillna(df['Age'].mean())
#Mode for Categorical
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
print(df)



#2nd program
import pandas as pd
import numpy as np
#Sample Dataset
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})
#Display Original Dataset
print("Original Dataset (With Missing Values):")
print(df)
#Forward Fill
df_ffill=df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)
#Backward fill
df_bfill=df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)

#3. Deletion 
import pandas as pd
import numpy as np
#Sample Dataset
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})
#Display Original Dataset
print("Original Dataset (With Missing Values):")
print(df)
#Drop rows with Missing values
df_drop_rows=df.dropna()
print("After droping rows:\n",df_drop_rows)
#Drop cloumns with Missing values
df_drop_cols=df.dropna(axis=1)
print("After droping clounmns:\n",df_drop_cols)

#3. Removing duplicates(Exact Match removal)
import pandas as pd
#sample datset with duplicates
df=pd.Dataframe({
    'ID': [1,2,2,3,4,4],
    'Name': ['Alice','Bob','Bob','Charlie','David','David'],
    'Age':[25,30,30,35,40,40]
})
print("Original Dataset:\n",df)
#Remove exact duplicates
df_exact=df.drop_duplicates()
print()

import pandas as pd
import numpy as np
df=pd.DataFrame({
    'Name':['Alice','Bob','charlie','David']
})
print("Original Data:\n",df)
df['Name_lower']=df['Name'].str.lower()
df['Name_upper']=df['Name'].str.upper()
print("\n",df)