import random 

number_list=[]

# Random list creation 
for i in range(10):
    selected_number=random.randint(1,100)
    number_list.append(selected_number)

# Printing list for test
print (number_list)

def insertion_sort(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1

        while j >= 0 and key < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1

        liste[j + 1] = key

    return liste


insertion_sort(number_list)
print (number_list)         # Sorted list