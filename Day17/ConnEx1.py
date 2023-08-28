from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='root')

print(myDbConnection)