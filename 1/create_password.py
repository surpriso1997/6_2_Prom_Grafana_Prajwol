 import getpass
 import bcrypt 


 password= getpass.getpass("password: ")

 hashed_pass= bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

 print(hashed_password.decode())


