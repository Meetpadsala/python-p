# class File:
#     def __enter__(self):
#         self.file = open("demo.txt","w")
#         return self.file
    

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()


# with File() as f:
#     f.write("Hello")


class File:
    def __enter__(self):
        print("Enter")
        return self
    

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Done")
        return self


with File():
    print("No Error")





