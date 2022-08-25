Username = "Natalie"
Password = "pass"
for i in range(3):
    print ("Enter username")
    Inputusername = str(input())
    print ("Enter password")
    Inputpassword = str(input())
    if i == 2:
        print ("Locked Out")
    elif Username == Inputusername and Password == Inputpassword:
        print ("Correct Welcome")
        break
    else:
        print ("Have another go")