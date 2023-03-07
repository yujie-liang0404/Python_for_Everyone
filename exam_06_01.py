text = "X-DSPAM-Confidence:    0.8475"
x = text.find(':')
y = text[x + 1:]
sli = y.strip()
num = float(sli)
print(num)
