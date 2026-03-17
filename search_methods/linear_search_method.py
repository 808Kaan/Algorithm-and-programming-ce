import random 


sayi_listesi=[]    

n=int(input("How many numbers would you like to be generated ?"))

for i in range(n):
    sayi=random.randint(1,1000)
    sayi_listesi=sayi_listesi+[sayi]
print (sayi_listesi)

target_value=random.choice(sayi_listesi)
print (target_value)

def linear_search(liste,target):
    for index in range(len(liste)):
        if liste[index]== target:
            return index 
    return -1 

finded_value= linear_search(sayi_listesi,target_value)
print ("Target value located place:",finded_value+1)




