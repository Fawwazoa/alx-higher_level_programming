#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numofargs = len(sys.argv)
    listargs = sys.argv
    sums = 0
    if numofargs == 1:
        print("0")
    elif numofargs == 2:
        print("{}".format(listargs[1]))
    else:
        for i in range(1, numofargs):
            sums = int(listargs[i]) + sums
        print("{}".format(sums))
