import irisnative

# Modify connection info based on your environment
ip = "iris"
port = 51773
namespace = "USER"
username = "SuperUser"
password = "InterSystems"

# create database connection and IRIS instance
connection = irisnative.createConnection(ip,port,namespace,username,password)
dbnative = irisnative.createIris(connection)

print("[1. Setting and getting a global]")
# setting and getting a global
# ObjectScript equivalent: set ^testglobal("1") = 8888
dbnative.set(8881, "testglobal", "1")
dbnative.set(8821, "testglobal", "2","21")
dbnative.set(8822, "testglobal", "2","22")
dbnative.set(8831, "testglobal", "3","31")
dbnative.set(8832, "testglobal", "3","32")
dbnative.set(8833, "testglobal", "3","33")

# ObjectScript equivalent: set globalValue = $get(^testglobal("1"))
globalValue = dbnative.get("testglobal","1")

print("The value of testglobal is ", globalValue)
print()

print("[2 Iterating over a global]")
# modify global to iterate over

Iter = dbnative.iterator("testglobal")
print("walk forwards")
for subscript, value in Iter.items():
    print("subscript= {}, value={}".format(subscript, value))
print()

print("[3. Calling a class method]")
# calling a class  method
# ObjectScript equivalent: set returnValue = ##class(%Library.Utility).Date(5)
returnValue = dbnative.classMethodValue("%Library.Utility", "Date", 5)
print("%Library.Utility('Date', 5)")
print(returnValue)

# close connection
connection.close()