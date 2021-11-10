s = "abcabcbb"
emp_s = ''
long_str = ''
sub_dict = {}

if len(s )== 1:
    print(1)

for i,k in enumerate(s):
    # print(i,k)
    if k not in sub_dict:
        sub_dict[k] = 1
        emp_s += k
        # print(sub_dict,emp_s)
    else:
        if len(emp_s) >= len(long_str):
            long_str = emp_s
            sub_dict[emp_s] = len(emp_s)
            emp_s = ''
            sub_dict = {}
            sub_dict[k] = 1 
            emp_s += k

print(sub_dict,long_str,len(long_str))