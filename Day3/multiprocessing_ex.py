import multiprocessing

def task():
    print("Task running")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

