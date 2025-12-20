
attempt = 3

while attempt > 0:
    user_name = input("Enter your Username: ")
    password = input("Enter your Password: ")

    if user_name == "admin" and password == "python123":
        print("Access Granted")
        break
    else:
        attempt -= 1
print("Wrong Password or Username")

