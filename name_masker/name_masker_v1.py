

name = input("Enter Your name: ")
masked = name[0] + "*" * (len(name) - 2) + name[-1]
print("Masked Name: ", masked)
