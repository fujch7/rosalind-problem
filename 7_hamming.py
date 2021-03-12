with open('7_hamling.fasta') as file:
    file = file.readlines()
str1 = file[0]
str2 = file[1]
n = len(str1)
m = 0
for i in range(n-1):
    if str1[i] != str2[i]:
        m = m + 1
print('value of hamling was:', m)
print(n)