# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
ori = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
    a = line.find(':')
    print(a)
    b = line.find(" ", a+2) # Find the first space from the position a+2
    print(b)
    ex = line[a + 1 : b]
    print(ex)
    va = ex.strip()
    print(va)
    fl = float(va)
    ori = ori + fl
    count = count + 1
    avr = ori / count
print("Average spam confidence:",avr)
print("Done")
