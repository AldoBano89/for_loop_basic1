#Detyra 1
for i in range(0,151):
    print(i)
#Detyra 2
for i in range(5,1001,5):
    print (i)
#Detyra 3
myList =['Coding', 'Dojo']
for i in range(0,101):
    if i%10 == 0:
        print(myList[0]+myList[1])
    elif i%5 == 0:
        print(myList[0])
    else : print(i)
#Detyra 4
sum=0
for i in range(0,500001):
    sum=sum+i
print(sum)
#Detyra 5
for i in range(2018, 0 , -4):
    print(i)
#Detyra 6

def counter(lowNum , highNum , mult):
    for i in range(lowNum , highNum):
        if i % mult == 0:
            print(i)
counter(2,9,3)