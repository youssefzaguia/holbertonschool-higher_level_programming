#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) <= 1:
        print("{}".format(len(argv) - 1))
    else:
        j = 0
        for i in range(1, len(argv)):
            j += int(argv[i])
        print("{}".format(j))
