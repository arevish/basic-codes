# Print fibonacci number at that position give by user
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        #for fibonacci number at n possition 
        # return fibo(n-1)+fibo(n-2)
    # for fibonacci series
        a=0
        b=1
        print(f"{a},{b}", end='')
        for i in range (2,n+1):
            c=a+b
            print(",{}".format(c), end='')
            a,b = b,c
numb= int(input("Enter a number "))
fibo(numb)
# print(fibo(numb))