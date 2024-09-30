n1 = int(input('Primer numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Tercer numero: '))
n4 = int(input('Cuarto numero: '))
i = 0
while i < n1+1:
    print('+', end = '')
    j = 0
    while j < n3:
        print('-', end = '')
        j = j + 1
    i= i + 1
print('+')
k = 0
while k < n4:
    i = 0
    while i < n1 + 1:
        print('|', end = '')
        j = 0
        while j < n3:
            print(' ', end = '')
            j = j + 1
        i = i + 1
    print('|')
    k = k + 1
