import os
import pandas as pd
import json

folder_path = r"C:\WORK\Prooktatas\2024-november-project\data"
json_folder = r"C:\WORK\Prooktatas\2024-november-project\tutorials\jsons"

files = os.listdir(folder_path)

for item in files:
    file_path = f"{folder_path}/{item}"
    json_path = "{json_folder}/{file_name}.json"

    df = pd.read_csv(file_path)

    

    data = df.to_dict(orient="records")

    for idx, i in enumerate(data):
        file_name = f"{item[0:-4]}_{idx}.json"
        final_path = json_path.format(json_folder=json_folder, file_name=file_name)
        with open(final_path, "w", encoding="utf-8") as f:
            json.dump(i, f)
        
        if idx == 100:
            break