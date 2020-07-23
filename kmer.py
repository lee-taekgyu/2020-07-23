import sys

l1 = ['A','T','C','G']
l2 = ['A','T','C','G']

def kmer(l1, l2, n:int):
    l_kmer = []
    if n ==1 :
        return l2
    for i in l1:
        for j in l2:
            l_kmer.append(i+j)
    return kmer(l1, l_kmer, n-1)

n = int(sys.argv[1])
print(kmer(l1,l2,n))
