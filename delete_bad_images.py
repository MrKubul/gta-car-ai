import pandas as pd
import os


path = r"C:\Users\kubad\Desktop\Data_1\balanced_data2.csv"
origin_path = r'C:\Users\kubad\Desktop\Data_1'
final_path = r'C:\Users\kubad\Desktop\images_balanced'

df = pd.read_csv(path, sep=';')
df = df.reset_index()

images = []
for index, row in df.iterrows():
    print(int(row['ID']))
    images.append(int(row['ID']))

for i in range(37160):
    if i not in images:
        for y in sorted(os.listdir(origin_path)):
            if y.startswith(str(i)+'_'):
                os.remove(os.path.join(origin_path, y))
                print("removed", os.path.join(origin_path, y))
                break
