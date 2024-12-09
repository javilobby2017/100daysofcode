def username():
   while True:
    username = input("what is your username?:")  
    password = input("what is your password?")
    if username == "javi" and password == "baldies4life":
      print("welcome javi!")
      break
    else:
      print("the username or pasword is incorrect try again!")
      continue  

print("replit login system")
username()