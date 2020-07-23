import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#Usage : pyhton {sys.argv[0]} [txt]")
        sys.exit()

f = sys.argv[1]
try:
    with open(f, 'r') as handle:
        read = handle.readlines()

    print(read)
except FileNotFoundError:
    print("Please check you diretory")
    sys.exit() 
