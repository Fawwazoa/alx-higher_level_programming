#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    namfun = dir(hidden_4)
    for i in namfun:
        if i[:2] != '__':
            print("{}".format(i))
