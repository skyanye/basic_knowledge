import pymysql

conn = pymysql.connect("172.16.50.44", username='root', passwd='', charset='utf-8', db='test')
cur = conn.cursor()
cur.execute("USE test")
cur.execute("select * from test")
content = cur.fetchall()
print(content)
cur.close()
conn.close()
