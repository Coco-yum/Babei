import pandas as pd
import numpy as np

# 读取Excel文件
df = pd.read_excel('EASON成长路.xlsx', sheet_name='Sheet1')

# 重命名列名
df.columns = ['日期', '身高', '体重', '记录']

# 填充空值，将相同日期的记录合并
df_merged = df.groupby('日期').agg({
    '身高': 'first',
    '体重': 'first',
    '记录': lambda x: '; '.join([str(i) for i in x if pd.notna(i)])
}).reset_index()

# 添加babyname列
df_merged['babyname'] = 'EASON'

# 保存为CSV文件
df_merged.to_csv('Babydata.csv', index=False, encoding='utf-8-sig')

print("Babydata.csv生成成功！")
