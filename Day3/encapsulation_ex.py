import os

# class Bank:
#     def __init__(self):
#         self.__balance = 500000

#     def get_balance(self):
#         return self.__balance


# b = Bank()
# print(b.get_balance())



class Bank:
    def __init__(self):
        self.__balance = 50000

    def get_balance(self):
        return self.__balance
    
    def add_balance(self,amount):
        if amount > 0:
            self.__balance += amount


b = Bank()
b.add_balance(50000)
print(b.get_balance())
        
    

       




