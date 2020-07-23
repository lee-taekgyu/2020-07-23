cnt = 0
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        cnt += 1

print(cnt)
