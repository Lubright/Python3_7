import sys


def main():
    list1 = list(sys.argv[1:])
    print(list1.count(list1[0]))


if __name__ == '__main__':
    main()
