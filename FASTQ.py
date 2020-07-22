import sys

class FASTQ():
    def __init__(self, file_name):
        self.file_name  = file_name
        self.read = 0

    def count(self):
        cnt = 0
        with open(file_name, 'r') as handle:
            for i in handle:
                if cnt % 4 == 0:
                    header =i.strip()
                    self.read += 1
                elif cnt % 3 ==0:
                    seq = i.strip()
                elif cnt % 2 ==0:
                    qual = i.strip()
                cnt += 1

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [fasta]")
        sys.exit()

    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count()
    print(t.read)


