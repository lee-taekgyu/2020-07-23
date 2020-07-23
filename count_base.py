import sys

class FASTA():
    def __init__(self, file_name):
        self.file_name = file_name
        self.count = {}
        self.length = 0
    
    def base_count(self):
        with open(file_name, 'r') as handle:
            for line in handle:
                if line.startswith('>'):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1 

    def base_length(self):
        for k,v in self.count.items():
            self.length += v

if __name__ =="__main__":
    if len(sys.argv) != 2:
        print(f" #usage : python {sys.argv[0]} [FASTA]")
        sys.exit()

    file_name = sys.argv[1]
    t = FASTA(file_name)
    t.base_count()
    t.base_length()
    print(t.count)
    print(t.length)

