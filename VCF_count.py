with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith('##'):
            continue
        if line.startswith('#'):
            header = line.strip().split("\t")
            INDEX = header.index('ID')

        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        rsID = splitted[2]
        ret = splitted[3]
        alt = splitted[4]
    
        if splitted[INDEX] != '.':
            print(f" {chrom}\t, {pos}\t, {rsID}\t, {ret}\t, {alt}\t")
