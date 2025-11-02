s = '111222333'
i = len(s) - 3
while i > 0:
    s = s[:i] + ',' + s[i:]
    i -= 3
print(s)

