# def number():
#     yield 1
#     yield 2
#     yield 3
# for i in number():
#     print(i)



def number():
    yield 10
    yield 20
    yield 30

gen = number()

print(next(gen))
print(next(gen))
print(next(gen))



