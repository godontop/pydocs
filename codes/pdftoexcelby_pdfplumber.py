# pdfplumber 适合处理结构清晰、表格明确的PDF。
import pdfplumber
import pandas as pd


with pdfplumber.open('documents/2024-2025学年深圳市罗湖区幼儿园办学基本信息表.pdf') as pdf:
    table_data = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            df = pd.DataFrame(table[1:], columns=table[0])
            table_data.append(df)


final_df = pd.concat(table_data, ignore_index=True)
final_df.to_excel('documents/幼儿园pdfplumber.xlsx', index=False)

