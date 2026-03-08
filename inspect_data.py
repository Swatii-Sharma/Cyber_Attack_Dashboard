import pandas as pd
import json

def inspect_data():
    file_path = 'project/dataset/microparticledata.xlsx'
    xl = pd.ExcelFile(file_path)
    
    all_info = {}
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        all_info[sheet] = {
            "columns": df.columns.tolist(),
            "head": df.head(5).to_dict()
        }
    
    with open('data_info_all.json', 'w') as f:
        json.dump(all_info, f, indent=4)

if __name__ == "__main__":
    inspect_data()
