import pymysql
con=pymysql.connect(host="localhost",database="VenkyDB",user="root",password="sunny@369")
cursor=con.cursor()
cursor.execute('SELECT * FROM employees')
records=cursor.fetchall()
for record in records:
    print('Employee number:',record[0])
    print('Employee name:',record[1])
    print('Employee salary:',record[2])
    print('Employee Address:',record[3])
