d = {"SNP":0, "DEL":0, "INS":0}

with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        
        splitted = line.strip().split("\t")
        Ref = splitted[3]
        Alt = splitted[4].split(",")
        print(Ref)
        print(Alt)
        for alt in Alt:
            if len(Ref) == len(alt):
                d['SNP'] += 1
            elif len(Ref) > len(alt):
                d['DEL'] += 1
            elif len(Ref) < len(alt):
                d['INS'] += 1 
print(d)        
        
