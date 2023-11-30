#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numargs = len(sys.argv)
    listargs = sys.argv
    if numargs == 1:
        print("{} arguments.".format(numargs - 1))
    elif numargs == 2:
        print("{} argument:".format(numargs - 1))
        print("{}: {}".format(1, listargs[1]))
    else:
        print("{} arguments:".format(numargs - 1))
        for i in range(1, numargs):
            print("{}: {}".format(i, listargs[i]))
