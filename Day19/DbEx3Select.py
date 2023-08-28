from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='root',
                                   database='pythonmagnus')
c1 = myDbConnection.cursor()

c1.execute("select * from emp where deptno=10")

result = c1.fetchall() # fetchall , fetchone

for i in result:
    print(i)

myDbConnection.close()