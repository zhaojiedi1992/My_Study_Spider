data = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 20},
    {"name": "王五", "age": 22},
]

# 写csv文件
import csv 
fieldnames = data[0].keys()
with open("data.csv", mode='w', newline='', encoding='utf-8') as csvfile:
    # 创建DictWriter对象
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    # 写入表头
    writer.writeheader()
 
    # 写入数据
    for row in data:
        writer.writerow(row)

# 写json
import json
with open("data.json", "w") as f:
    json.dump(data, f, indent=4,ensure_ascii=False)

# 写excel

import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
# 写入表头
ws.append(["name", "age"])
 
# 写入数据
for item in data:
    ws.append([item["name"], item["age"]])
 
# 保存工作簿到文件
wb.save("output.xlsx")

