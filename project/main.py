import sys


def inputType(name):
    if sys.argv == 0:
        print("random")
    elif sys.argv == 1:
        print("document")
    elif sys.argv > 1:
        print("numbers")


if __name__ == '__main__':
    print()

