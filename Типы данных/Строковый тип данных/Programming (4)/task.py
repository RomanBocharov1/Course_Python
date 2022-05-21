a, b, c = input(), input(), input()
a_len = len(a)
b_len = len(b)
c_len = len(c)
len_max = max(a_len, b_len, c_len)
len_min = min(a_len, b_len, c_len)
len_avg = (a_len + b_len + c_len) - (len_max + len_min)
if len_max - len_avg == len_avg - len_min:
    print('YES')
else:
    print('NO')

