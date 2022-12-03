print('******************************************************************')
print('*WELCOME TO THE MINI PORJECT OF FINDING PRIME OR COMPOSITE NUMBER*')
print('*       NAME - KARISHMA YADAV                                    *')
print('*       REGISTRATION NO. - 12200279                              *')
print('*       SECTION - K22FG GROUP-2                                  *')
print('*       ROLL NO. - 63                                            *')
print('******************************************************************')
def num(a,b):
    total_prime=0
    total_composite=0
    for i in range (a,b+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i," is Prime number")
            total_prime+=1
        elif count==0:
            print(i," is neither prime nor composite")
        else :
            print(i,"is Composite number")
            total_composite+=1
    print(total_prime,"prime ","and",total_composite,"composite numbers in the range")
a=int(input("Enter the starting number  :"))
b=int(input("Enter the ending number :"))
num(a,b)

    
    


