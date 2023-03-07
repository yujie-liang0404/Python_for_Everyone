xh = input("enter hour: ")
xr = input('enter rate: ')
try:
    fh = float(xh)
    fr = float(xr)
except:
    print('Error, please enter numeric input')
    quit()
# Calculating the price based on hour of usage and rate
if fh > 40:
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print('pay:', xp)
