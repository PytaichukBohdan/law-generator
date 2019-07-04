import json
import pandas as pd


with open('data_final.json', 'r') as f:
    data = json.load(f)

print(len(data.keys()))

new_data = {}
for k, v in data.items():
    if not (('JFIF' in v) or (not v)):
        new_data[k] = v


with open('law_texts.txt', 'w') as f:
    for k, v in new_data.items():
        print(k)
        f.writelines(v)
        f.writelines("\n <|endoftext|> \n")

# df_1 = pd.read_json('data_with_stop_words.json', typ='series')

# print(df_1.head())