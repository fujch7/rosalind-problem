n , k = eval(input("please enter n and k separated by comma:"))
def rab(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return rab(n-2)*k+rab(n-1)
print(rab(n))