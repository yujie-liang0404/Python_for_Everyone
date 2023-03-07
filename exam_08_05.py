fh = open('mbox-short.txt')
count = 0
for line in fh:
  line = line.rstrip()
  list = line.split()
  # can't find any word in blank line->blow up
  # Gardian should write behind code ('or' only check one code)
  if len(list) < 1 or list[0] != 'From':
      continue
  print(list[1])
  count = count + 1
print('There were', count, 'lines in the file with From as the first word')
