import pandas as pd
import os

image_num = 37160
path = r"C:\Users"
origin_path = r'C:\Users'
final_path = r'C:\Users'

df = pd.read_csv(path, sep=';')
df = df.reset_index()

images = []
for index, row in df.iterrows():
    print(int(row['ID']))
    images.append(int(row['ID']))

for i in range(image_num):
    if i not in images:
        for y in sorted(os.listdir(origin_path)):
            if y.startswith(str(i)+'_'):
                os.remove(os.path.join(origin_path, y))
                print("removed", os.path.join(origin_path, y))
                break
