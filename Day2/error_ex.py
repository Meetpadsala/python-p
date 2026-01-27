#try → risky code
#except → error handle
#else → runs only when no error occurs



# try:
#     num = int(input("Enter Number :"))
#     print(10 / num)

# except ValueError:
#     print("Only Number")

# except  ZeroDivisionError:
#     print("NO zero division")





# try:
#     num = int(input("Enter your number :"))
#     print(num)
# except:
#     print("Only Number ")
# else:
#     print("your number : ", num)





# try:
#     f = open("text.txt")
#     print(f.read())
# except:
#     print("File not found")
# finally:
#     print("Program complete")

try:
    x = int("10")
except:
    print("error")
else:
    print("NO error")
finally:
    print("Always run")
    









