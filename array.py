#array.py

arr = list()
n = int(input('Enter number of elements (1-15):'))
while 0 >= n or 16 <= n:
    n = int(input('Wrong input. Enter number of elements (1-15):'))

for i in range(n):
    tmp = input("Enter element: ")
    while not tmp.isdigit():
        tmp = input('Wrong input. Enter correct element (number): ')
    arr.append(int(tmp))

print('Array:')
for i in range(n):
    print(arr[i], end = " ")
print('Succesful!')
