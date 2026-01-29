import threading
import time

# def task():
#     print("Task running")


# p1 = threading.Thread(target=task)
# p2 = threading.Thread(target=task)

# p1.start()
# p2.start()


# def greet(name):
#     print(f"Hello{name}")


# t1 = threading.Thread(target=greet, args=("Meet",))
# t2 = threading.Thread(target=greet, args=("Raj",))

# t1.start()
# t2.start()

def greet():
    time.sleep(2)
    print("Done")


t1 = threading.Thread(target=greet)
t2 = threading.Thread(target=greet)

t1.start()
t2.start()

t1.join()
t2.join()     

print("All tasks completed")





