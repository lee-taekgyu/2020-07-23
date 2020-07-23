import sys

if __name__ =="__main__":
    if len(sys.argv) != 2:
        print(f"#usage : python {sys.argv[0]} [num]")
        sys.exit()

try:
    num = int(sys.argv[1])
    print(10/num)
except ValueError:
    print("Input not valid")
    sys.exit()
except ZeroDivisionError:
    print("Can't divide as Zero")
    sys.exit()
