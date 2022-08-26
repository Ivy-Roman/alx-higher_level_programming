#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user_input = argv[1:]
    items = []
    for index, arg in enumerate(user_input):
        item = int(arg)
        items.append(item)
        print(sum(items))
