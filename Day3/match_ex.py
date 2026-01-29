# command = "start"

# match command:
#     case "start":
#         print("Program started")
#     case "stop":
#         print("Program stopped")
#     case _:
#         print("Unknown command")






# num = 2

# match num:
#     case 1 | 2 | 3:
#         print("Small number")
#     case 4 | 5:
#         print("Medium number")
#     case _:
#         print("Large number")



data = [1, 2]

match data:
    case [1, 2]:
        print("Exactly 1 and 2")
    case [x, y]:
        print("Two values:", x, y)
    case _:
        print("No match")
