from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='root',
                                   database='pythonmagnus')
c1 = myDbConnection.cursor()
vempno = int(input("Enter the Empno Value: "))
vename = input("Enter the Ename Value: ")
vsal = int(input("Enter the Sal Value: "))
vdeptno = int(input("Enter the Deptno Value: "))

c1.execute("insert into emp (empno,ename,sal,deptno) values(%s,%s,%s,%s)",(vempno,vename,vsal,vdeptno))

myDbConnection.commit()
myDbConnection.close()