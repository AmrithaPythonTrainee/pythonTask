lower=int(input("Please, Enter the lowest range value:"))
upper=int(input("Please, Enter the upper range value:"))
print("the prime numbers in the range are:")
for num in range(lower,upper+1):
    if num >1:
        for i in range(2,num):
            if(num % i)==0:

                break
        else:
            print(num)