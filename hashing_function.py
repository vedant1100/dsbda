# creating hash table
n=int(input("\n enter the size of table : "))
key=[]
for i in range(n):
    key.append(i)

hash_table={}
for i in key:
    hash_table[i]=[]
print(hash_table)


# adding elements in hash table
def add(hash_table,n):
    value=int(input("\nenter value : "))
    i=int(value%n)
    hash_table[i].append(value)
    print(hash_table)


# finding element in hash table
def find(hash_table,n):
    temp=0
    value1=int(input("\nenter value to be found : "))
    j=int(value1%n)
    for x in hash_table[j]:
        if x==value1:
            temp=1
            break

    if temp==1:
        print(value1, " is found at ", hash_table[j].index(x)," at key number ", j)
    else:
        print(value1 ," is not found ")


# deleting an element in hash table
def delete(hash_table,n):
    temp=0
    value=int(input("\nenter the value to be deleted : "))
    k=int(value%n)
    if value in hash_table[k]:
        hash_table[k].remove(value)
        temp = 1

    if temp==1:
        print(value, " is deleted from the hash table ")
    else:
        print("hash value not found")


print("\nOperations : \n 0) exit \n 1) Print hash table  \n 2) insert element  \n 3) find an element  \n 4) delete an element \n")
while(True):
    option=int(input("\n\nchoose an operation to perform : "))
    if option==1:
        print(hash_table)

    if option==2:
        add(hash_table,n)

    if option==3:
        find(hash_table,n)

    if option==4:
        delete(hash_table,n)

    elif option==0:
        break

