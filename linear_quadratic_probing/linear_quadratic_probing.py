a=int(input("enter the size of table : "))
hash_table=[-1]*a

def linear_probing():
    for i in range(0,a):
        b=int(input("\n enter telephone number : "))
        key=b%a

        if hash_table[key]==-1:
            hash_table[key]=b

        if hash_table[key]!=-1:
            while(hash_table[key]!=-1):
                if key==a-1:
                    print("\n overflow")
                key=key+1
            if hash_table[key]==-1:
                hash_table[key]=b

    print(hash_table)

def quadratic_probing():
    i=1
    for i in range(0,a):
        b=int(input("\n enter telephone number : "))
        key=b%a

        if hash_table[key]==-1:
            hash_table[key]=b

        elif hash_table[key]>a:
            print("\n out of range")

        else:
            while hash_table[key]!=-1:
                key=key+i*i
                i=i+1
            if hash_table[key]>a:
                print("\n out of range")
            if hash_table[key]==-1:
                hash_table[key]=b

    print(hash_table)

option=0
while(option==0):
    print("\n choose an oprion to proceed : \n 1) Linear Probing \n 2) Quadratic Probing")
    option1=int(input("\n enter the option : "))
    if option1==1:
        linear_probing()
    if option1==2:
        quadratic_probing()