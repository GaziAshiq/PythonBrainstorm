import re


def reg(string):
    s = 'my 1st mobile number: 01837267082'
    f = re.search(string, s)
    print(f.group() if f is not None else f)


reg('\d{11}')
