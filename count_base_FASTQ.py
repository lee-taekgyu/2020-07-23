import sys

class FASTQ():
    def __init__(self, file_name):
        self.file_name = file_name
        self.count = {}
        self.length = 0

    def count_readnum(self):
        cnt = 0
        with open(file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 == 0:
                    header = line.strip()
                    self.length += 1
                elif cnt % 4 == 1:
                    seq = line.strip()
                    print(seq)
                    for s in seq:
                        if s in self.count:
                            self.count[s] += 1
                        else:
                            self.count[s] = 1
                elif cnt % 4 == 3:
                    qual = line.strip()
                cnt += 1


if __name__=="__main__":
    if len(sys.argv) !=2:
        print(f"#usage: python{sys.argv[0]}[fasta]")
        sys.exit()

    file_name = sys.argv[1]
    f = FASTQ(file_name)
    f.count_readnum()
    print(f.count)
