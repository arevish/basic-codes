# factorial program by reccursive approch

def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
numb= int(input("Enter the number "))
print(fact(numb))


