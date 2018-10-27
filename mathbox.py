#Factorial

def factorial(number):
    if number>1:
        return number*factorial(number-1)
    else:
        return 1


print(3)
print(3*2*1)
for number in range(19,20):
    print(factorial(number))

print(factorial(0))