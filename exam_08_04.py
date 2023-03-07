fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    print(line.rstrip())
    words = line.split()
    print(words)
    print('done')
    for element in words:
        if element in lst:continue
        lst.append(element)
lst.sort()
print(lst)
