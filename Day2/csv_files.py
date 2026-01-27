import csv


with open("students.csv", "w", newline="") as file:
    wr = csv.writer(file)
    wr.writerow(["Name", "Age"])
    wr.writerow(["Meet", "20"])
    wr.writerow(["Raj", "20"])

