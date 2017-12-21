# Author: yangvipguang
import getpass

_username = "yangguang"
_password = 123456

username = input("Username:")
# password = getpass.getpass("password:")
password = input("password:")
print(username, password)

if username == _username and password == _password:
    print("Welcome User {name} to login".format(name=username))
else:
    print("Invalid User or Password")
