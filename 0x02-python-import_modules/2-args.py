#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user_input = argv[1:]
    num_of_arg = len(user_input)
    if num_of_arg == 0:
        print("0 arguments.")
    elif num_of_arg == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(num_of_arg))
        for index, arg in enumerate(user_input):
            print("{}: {}".format(index + 1, argv[index]))
