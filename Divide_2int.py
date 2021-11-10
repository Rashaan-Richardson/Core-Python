dividend = -2147483648
divisor = -1
ans = 0 
if (-2**31 <= dividend <= 2**31 -1
    and -2**31 <= divisor <= 2**31 and divisor !=0):
    if divisor < 0:
        ans = dividend//abs(divisor)
        ans = ans * -1
    else:
        ans = dividend//divisor
else:
    ans = (2**31)-1
print(ans) 