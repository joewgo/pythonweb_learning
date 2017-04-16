import sqlite3
conn = sqlite3.connect('SimpleDB.sqlite')
cursor = conn.cursor()
sqlstr = 'INSERT INTO user ("id", "username") VALUES ("2", "MyStar2")' #新增 INSERT　INTO

cursor.execute(sqlstr)

#cursor = conn.execute('SELECT * FROM user') #查詢　SELECT FROM
#rows = cursor.fetchall()
#print(rows)

#cursor = conn.execute('UPDATE user SET username="Jack" WHERE username="Leo"') #更新 UPDATE SET WHERE

#cursor.execute('DELETE FROM user WHERE username="Jack"') #刪除　DELETE FROM

conn.commit()
conn.close()
