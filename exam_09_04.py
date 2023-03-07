fh = open('mbox-short.txt')

lst = list()
for line in fh:
  line = line.rstrip()
  words = line.split()
  if len(words) < 1 or words[0] != 'From':
      continue
  lst.append(words[1])
print(lst)
counts = dict()
for person in lst:
    counts[person] = counts.get(person, 0) + 1 # If the person shows up in the dictionary for the first time, then put 0, and add 1; else, add 1 to the stored value
bigcount = None
bigperson = None
for person, count in counts.items():
    if bigcount is None or count > bigcount:
        bigperson = person
        bigcount = count
print(bigperson, bigcount)
