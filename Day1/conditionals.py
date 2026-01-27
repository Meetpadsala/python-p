# day = input("Enter the day of week : ").lower()
# print(day)

# if day == "saturday" or day == "sunday":
#     print("I will learn live DevOps")
# else:
#     print("I will practice DevOps")




num1 = int(input("Enter First Number : "))
num2 = int(input("Enter second Number : "))

choice = input("Enter the operation: (options +, -, *, /, %)")

if choice == "+":
    sum = num1+num2
    print(sum)
elif choice == "-":
    sum = num1-num2
    print(sum)
elif choice == "*":
    sum = num1*num2
    print(sum)
elif choice == "/":
    sum = num1/num2
    print(sum)
elif choice == "%":
    sum = num1%num2
    print(sum)
else:
    print("Invalid choice")


