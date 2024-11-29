data = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 20},
    {"name": "王五", "age": 22},
]
import pymysql  

db = pymysql.connect(host='localhost',user='root', password='123456', port=3306)  
cursor = db.cursor()
sql = 'INSERT INTO students(name, age) values( %s, %s)'
for data_item in data: 
    try:
        cursor.execute(sql, (data_item["name"], data_item["age"]))
        db.commit()
    except:
        db.rollback()
db.close()