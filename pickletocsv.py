import pickle
import pandas as pd
import numpy as np

scalefactor = 0.001

output_path = '../coordinates.csv'

with open('/home/owpo6214/Desktop/DynamicVis/DYNAMIC_xyz_coordinates.pkl', 'rb') as file:
    data = pickle.load(file)

df = pd.DataFrame(data, columns=["Timestamp", "Coordinates"])

df[['X', 'Y', 'Z']] = pd.DataFrame(df['Coordinates'].tolist(), index=df.index)
df.drop(columns=['Coordinates'], inplace=True)

df[['X', 'Y', 'Z']] = scalefactor * df[['X', 'Y', 'Z']]

# Assuming `df` is the DataFrame from earlier
df.to_csv(output_path, columns=['Timestamp', 'X', 'Y', 'Z'], index=False)

print(df.shape)
