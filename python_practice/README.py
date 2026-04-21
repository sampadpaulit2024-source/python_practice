"""python_practice
my 1st repo
maker - Sampad Paul"""
# fizzbuzz
num1 = int(input("enter start of the renge: "))
num2 = int(input("enter end of renge: "))
num = range(num1, num2)
for i in num:
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
print("end")
