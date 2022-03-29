def CheckPrime(a):
    for i in range(2,a):
        if a%i!=0:
            return True
            break
        else:
            return False
            break

if __name__=="__main__":
    a = int(input("Enter any number"))
    result = CheckPrime(a)
    print(result)

