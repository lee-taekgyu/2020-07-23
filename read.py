import sys
import json

def read_txt(file_name : str) -> str:
    mark = ""
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith('>'):
                continue
            mark += line.strip()
    return mark

def read_csv(file_name : str) -> list:
    mark = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith('#'):
                header = line.strip().split(",")
            else:
                splitted = line.strip().split(",")
        d = dict(zip(header, splitted))
        mark.append(d)
    return mark

def read_tsv(file_name :str) -> list:
    mark = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith('#'):
                header = line.strip().split("\t")
            else:
                splitted = line.strip().split("\t")
        d = dict(zip(header, splitted))
        mark.append(d)
    return mark

def to_json(l :list, file_name : str) -> None:
    with open("switch_to_json.json", 'w') as handle:
        json.dump(l,handle,indent = 4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#Usage : python {sys.argv[0]}[txt]")
        sys.exit()

    file_name = sys.argv[1]
    #txt = read_txt(file_name)
    #print(txt)

    mark = read_csv(file_name)
    #print(mark)

    #mark = read_tsv(file_name)
    #print(mark)

    to_json(makr, "switch_to_json.json")       
