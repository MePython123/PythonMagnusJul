from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='root',
                                   database='pythonmagnus')
c1 = myDbConnection.cursor()
# cursor is a pointer which locates processing area/Temporary Memory area.
#c1.execute("drop table if exists emp")
#c1.execute("create table emp (empno int,ename varchar(20),sal int,deptno int)")
#c1.execute("insert into emp values(101,'abc',1000,10)")
#c1.execute("insert into emp values(102,'bcd',1200,20)")
sql = "insert into emp values(%s,%s,%s,%s)"
data = (103,'cde',2000,30)
c1.execute(sql,data)
myDbConnection.commit()
myDbConnection.close()