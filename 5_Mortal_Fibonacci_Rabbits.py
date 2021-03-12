n , m = eval(input("please enter n and m separated by comma:"))
a = [0,1]
t = 1
while t < m:
    new = a[t] + a[t-1]
    a.append(new)
    t = t + 1
    if t == m:
        new = a[t] + a[t-1] - 1
        a.append(new)
        del a[0]
i = len(a) - 1
while i <= n - 2:
      new = a[i] + a[i-1] - a[i - m]
      a.append(new)
      i = i + 1
print(a[-1])