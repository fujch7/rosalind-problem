a, b, c = eval(input('请输入各个基因型的数量,中间用逗号分开:'))
m = a + b + c
q = (c * (c - 1))/ (m * (m - 1))
w = (b * c) / (m * (m - 1))
e = ((b * (b - 1)) / (m * (m - 1))) / 4
r = round(1 - (q + w + e),5)
print(r)
