import pandas as pd

file_path = 'project/dataset/microparticledata.xlsx'
xl = pd.ExcelFile(file_path)

with open('structure.txt', 'w') as f:
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        f.write(f"Sheet: {sheet}\n")
        f.write(f"Columns: {df.columns.tolist()}\n")
        f.write("-" * 50 + "\n")
