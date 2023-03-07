fh = open('mbox-short.txt')
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != 'From':
        continue
    x = words[5]
    x = x.split(':')
    lst.append(x[0])
counts = dict()
for time in lst:
    if time not in counts:
        counts[time] = 1
    if time in counts:
        counts[time] = counts[time] + 1
counts = sorted(counts.items())
for k, v in counts:
    print(k, v-1)
