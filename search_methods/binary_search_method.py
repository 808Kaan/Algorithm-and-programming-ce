import random 


sayi_listesi=[]    

n=int(input("How many numbers would you like to be generated ?"))

for i in range(n):
    sayi=random.randint(1,1000)
    sayi_listesi=sayi_listesi+[sayi]

sayi_listesi.sort()
print (sayi_listesi)

target_value=random.choice(sayi_listesi)
print (target_value)


def binary_search(liste, target):
    if len(liste) == 0:
        return -1

    mid_index = len(liste) // 2
    mid_value = liste[mid_index]

    if target == mid_value:
        return mid_index

    if target < mid_value:
        return binary_search(liste[:mid_index], target)

    else:
        result = binary_search(liste[mid_index+1:], target)
        if result == -1:
            return -1
        else:
            return mid_index + 1 + result

index = binary_search(sayi_listesi, target_value)
print("Located place:", index+1 )



        
        
        






