#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user_input = argv[1:]
    num_of_arg = len(user_input)
    print("{:d} {:s}{:s}".
          format(num_of_arg,
                 "arguments" if (num_of_arg) != 1 else "argument",
                 "." if (num_of_arg) == 0 else ":"))
    for index, arg in enumerate(user_input):
        print("{:d}: {:s}".format(index + 1, arg))
